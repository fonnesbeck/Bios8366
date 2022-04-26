import os
import dask.dataframe as dd

df = dd.read_csv(os.path.join('data', 'nycflights', '*.csv'),
                 parse_dates={'Date': [0, 1, 2]},
                 dtype={'TailNum': str,
                        'CRSElapsedTime': float,
                        'Cancelled': bool})

# In total, how many non-cancelled flights were taken from each airport?

df[~df.Cancelled].groupby('Origin').Origin.count().compute()

# What was the average departure delay from each airport?

df.groupby("Origin").DepDelay.mean().compute()