import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import normalize
from sklearn.model_selection import GridSearchCV

vlbw = pd.read_csv("../data/vlbw.csv", index_col=0)
vlbw = vlbw.replace({'inout':{'born at Duke':0, 'transported':1},
             'delivery':{'abdominal':0, 'vaginal':1},
             'ivh':{'absent':0, 'present':1, 'possible':1, 'definite':1},
             'sex':{'female':0, 'male':1}})

vlbw = vlbw[[u'birth', u'exit', u'hospstay', u'lowph', u'pltct', 
      u'bwt', u'gest', u'meth', 
      u'toc', u'delivery', u'apg1', u'vent', u'pneumo', u'pda', u'cld', 
      u'ivh']].dropna()

y = vlbw.pop('ivh').values
X = vlbw.values

def brier(mod, X, y): 
    y_hat = np.argmax(mod.fit(X,y).predict_proba(X))
    return ((y_hat - y)**2).mean()

C = np.logspace(-3, 2, 20)

scores = np.empty(len(C))
scores_std = np.empty(len(C))


for i,c in enumerate(C):
    lr = LogisticRegression(C=c)
    s = cross_val_score(lr, X, y, scoring=brier)
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


cvalues = [0.1, 1, 10,100]
grid = GridSearchCV(LogisticRegression(), 
    param_grid={'C': cvalues}, scoring='average_precision')
gf = grid.fit(X, y)
gf.cv_results_

grid = GridSearchCV(LogisticRegression(), 
            param_grid={'C': cvalues}, scoring='roc_auc')
gf = grid.fit(X, y)
gf.cv_results_