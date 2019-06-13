from sklearn.gaussian_process import GaussianProcess

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

daily_temps = pd.read_table("../data/TNNASHVI.txt", sep='\s+', 
                            names=['month','day','year','temp'], na_values=-99)
                            
temps_2010 = daily_temps.temp[daily_temps.year>2010]

X = np.arange(len(temps_2010))[:, None]

G_temp = GaussianProcess(corr='absolute_exponential', theta0=0.1, nugget=1)
G_temp.fit(X, temps_2010.values)

plt.figure(figsize=(10,6))
y_pred = G_temp.predict(X)
plt.plot(X, y_pred, 'r-')
plt.plot(temps_2010.values, 'b.', alpha=0.4)