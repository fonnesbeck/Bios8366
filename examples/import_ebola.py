ebola_dirs = !ls ../data/ebola/

import glob

filenames = {data_dir[:data_dir.find('_')]: glob.glob('../data/ebola/{0}/*.csv'.format(data_dir)) for data_dir in ebola_dirs[1:]}

datasets = []
for country in filenames:
    
    country_files = filenames[country]
    for f in country_files:
        
        data = pd.read_csv(f)
        
        
        # Convert to lower case to avoid capitalization issues
        data.columns = data.columns.str.lower()
        # Column naming is inconsistent. These procedures deal with that.
        keep_columns = ['date']
        if 'description' in data.columns:
            keep_columns.append('description')
        else:
            keep_columns.append('variable')
            
        if 'totals' in data.columns:
            keep_columns.append('totals')
        else:
            keep_columns.append('national')
            
        # Index out the columns we need, and rename them
        keep_data = data[keep_columns]
        keep_data.columns = 'date', 'variable', 'totals'
        
        # Extract the rows we might want
        lower_vars = keep_data.variable.str.lower()
        # Of course we can also use regex to do this
        case_mask = (lower_vars.str.contains('new') 
                     & (lower_vars.str.contains('case') | lower_vars.str.contains('suspect') 
                                                        | lower_vars.str.contains('confirm')) 
                     & ~lower_vars.str.contains('non')
                     & ~lower_vars.str.contains('total'))
        
        keep_data = keep_data[case_mask].dropna()
        
        # Convert data types
        keep_data['date'] = pd.to_datetime(keep_data.date)
        keep_data['totals'] = keep_data.totals.astype(int)
        
        # Assign country label and append to datasets list
        datasets.append(keep_data.assign(country=country))

all_data = pd.concat(datasets)
all_data.head()       