import numpy as np
import pandas as pd
titanic = pd.read_excel("../data/titanic.xls", "titanic")
titanic.head()


titanic.loc[titanic["sex"] == "male", "sex"] = 0
titanic.loc[titanic["sex"] == "female", "sex"] = 1

titanic["embarked"] = titanic["embarked"].fillna("S")
titanic.loc[titanic["embarked"] == "S", "embarked"] = 0
titanic.loc[titanic["embarked"] == "C", "embarked"] = 1
titanic.loc[titanic["embarked"] == "Q", "embarked"] = 2

features = ["pclass", "sex", "sibsp", "parch", "embarked"]




from sklearn.preprocessing import StandardScaler
X = StandardScaler().fit_transform(titanic[features])
y = titanic.survived


# Set grid of SVC hyperparameters
parameters_svm = {'C':[0.01, 0.1, 1],
                  'kernel':['rbf', 'linear'], 
                  'gamma': [1e-2, 1e-1, 1, 'auto'],
                  'decision_function_shape':['ovo', 'ovr'],
                  'degree':[3, 4, 10]}


# Perform grid search over hyperparameters
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

grid = GridSearchCV(estimator=SVC(), 
                    param_grid=parameters_svm, cv=5, 
                    scoring='accuracy')
grid.fit(X, y)
grid.best_score_, grid.best_estimator_.get_params()


# Calculate mean CV score under best model
clf = SVC(**best_params)
score = cross_val_score(clf, X, y, scoring='accuracy', cv=3, n_jobs=4).mean()
score


# I will use the `fancyimpute` package to do imputation of age. See docs for details.
#!pip install fancyimpute

from fancyimpute import IterativeImputer

age_incomplete = titanic[['age'] + features]

n_imputations = 5

imputed_age = [IterativeImputer(n_iter=5, sample_posterior=True, random_state=i).fit_transform(age_incomplete) 
                       for i in range(n_imputations)]

best_params = grid.best_estimator_.get_params()


from sklearn.model_selection import cross_val_score

accuracies = []
for X in imputed_age:
    X =  StandardScaler().fit_transform(X)
    clf = SVC(**best_params)
    scores = cross_val_score(clf, X, y.values, scoring='accuracy', cv=3, n_jobs=4).mean()
    accuracies.append(scores)

np.mean(accuracies)

