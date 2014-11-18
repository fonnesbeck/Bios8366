import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import cross_validation, linear_model


vlbw = pd.read_csv("../data/vlbw.csv", index_col=0)

y = vlbw.pop('ivh')

def brier(mod, X, y): 
    return ((mod.fit(X,y).predict_proba(X) - y)**2).mean()

C = np.logspace(-3, 2, 20)

scores = np.empty(len(C))
scores_std = np.empty(len(C))


for i,c in enumerate(C):
    lr = linear_model.LogisticRegression(C=c)
    s = cross_validation.cross_val_score(lr, vlbw, y, scoring=brier, n_jobs=-1)
    scores[i] = s.mean()
    scores_std[i] = s.std()

plt.semilogx(alphas, scores)
plt.semilogx(alphas, np.array(scores) + np.array(scores_std)/20, 'b--')
plt.semilogx(alphas, np.array(scores) - np.array(scores_std)/20, 'b--')
plt.yticks(())
plt.ylabel('Brier score')
plt.xlabel('alpha')
plt.axhline(np.max(scores), linestyle='--', color='.5')
plt.text(5e-2, np.max(scores)+1e-4, str(np.max(scores).round(3)))



from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import normalize

y = vlbw.pop('ivh').values
X = vlbw

from sklearn.grid_search import GridSearchCV
cvalues = [0.1, 1, 10,100]
grid = GridSearchCV(LogisticRegression(), 
    param_grid={'C': cvalues}, scoring='average_precision')
gf = grid.fit(X, y)
gf.grid_scores_

grid = GridSearchCV(LogisticRegression(), 
            param_grid={'C': cvalues}, scoring='roc_auc')
gf = grid.fit(X, y)
gf.grid_scores_