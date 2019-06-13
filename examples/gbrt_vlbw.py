import pandas as pd

vlbw = pd.read_csv('../data/vlbw.csv', index_col=0)

vlbw['IVH'] = vlbw.ivh.replace({'absent': -1, 'definite': 1, 'possible': 1})
vlbw_complete = vlbw[vlbw.IVH.notnull()]

x_vars = ['bwt', 'gest', 'pneumo', 'lowph', 'delivery', 'inout']
vlbw_complete = vlbw_complete.dropna(subset=x_vars)

X = vlbw_complete[x_vars]

X['transported'] = X.inout.replace({'born at Duke':0, 'transported':1})
X['CS'] = (X.delivery=='abdominal').astype(int)

X = X.drop(['inout', 'delivery'], axis=1)

from sklearn import preprocessing

X = preprocessing.scale(X)
est = GradientBoostingRegressor(n_estimators=3000, max_depth=6, learning_rate=0.04)

X_train, X_test, y_train, y_test = train_test_split(X, vlbw_complete.IVH,
                                                    test_size=0.3,
                                                    random_state=1)
                                                    
est.fit(X_train, y_train)
mean_absolute_error(y_test, est.predict(X_test))