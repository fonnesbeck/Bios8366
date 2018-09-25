import pandas as pd
DATA_DIR = '../data/microbiome/'

files = !ls $DATA_DIR
metadata = pd.read_excel(DATA_DIR + files[0], index_col=0)

dataframes = []
for filename in files[1:]:
    barcode = filename.split('.')[0]
    group, sample = metadata.loc[barcode]
    df = pd.read_excel(DATA_DIR + filename, 
                       header=None,
                      names=['taxon', 'count'])
    df['group'] = group
    df['sample'] = sample
    dataframes.append(df)
    
pd.concat(dataframes)
