from sklearn.model_selection import GridSearchCV
from sklearn.utils import shuffle
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pandas as pd
import pylab as plt


daily_temps = pd.read_table("../data/TNNASHVI.txt", sep='\s+', 
                            names=['month','day','year','temp'], na_values=-99)
                            
# Transmogrify data
y = daily_temps.temp[daily_temps.year>2010]
X = np.atleast_2d(np.arange(len(y))).T

rf = RandomForestRegressor()
parameters = {'n_estimators':[10, 50, 100, 200, 300],
              'max_leaf_nodes':[3, 5, 7, 9, 11, 13]}

# Warning: be sure your data is shuffled before using GridSearch!
clf_grid = grid_search.GridSearchCV(rf, parameters)
clf_grid.fit(*shuffle(X, y))

rf_best = clf_grid.best_estimator_
X_fit = np.linspace(0, len(X), 1000).reshape((-1, 1))
y_fit_best = rf_best.predict(X_fit)

print((rf_best.n_estimators, rf_best.max_depth))

plt.plot(X.ravel(), y, '.k', alpha=0.3)
plt.plot(X_fit.ravel(), y_fit_best, color='red')