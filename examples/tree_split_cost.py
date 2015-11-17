import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes

# Predictors: "age" "sex" "bmi" "map" "tc"  "ldl" "hdl" "tch" "ltg" "glu"
diabetes = load_diabetes()
y = diabetes['target']
bmi, ltg = diabetes['data'][:,[2,8]].T

def rss_cost(data, mask):
    this_cost = ((data[mask] - np.mean(data[mask]))**2).sum()
    that_cost = ((data[~mask] - np.mean(data[~mask]))**2).sum()
    return this_cost + that_cost
    
ltg_space = np.linspace(ltg.min(), ltg.max())
ltg_cost = [rss_cost(y, ltg<c) for c in ltg_space]
ltg_opt = ltg_space[np.argmin(ltg_cost)]
print(ltg_opt)

bmi_space = np.linspace(bmi[ltg>ltg_opt].min(), bmi[ltg>ltg_opt].max())
bmi_cost = [rss_cost(y[ltg>ltg_opt], bmi[ltg>ltg_opt]<c) for c in bmi_space]
bmi_opt = bmi_space[np.argmin(bmi_cost)]
print(bmi_opt)

plt.scatter(ltg, bmi,  c=y)
plt.vlines(ltg_opt, *plt.gca().get_ylim(), linestyles='dashed')
plt.hlines(bmi_opt, ltg_opt, plt.gca().get_xlim()[1], linestyles='dashed')
plt.colorbar()
plt.xlabel('ltg'); plt.ylabel('bmi')
plt.show()