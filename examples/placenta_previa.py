import numpy as np
import seaborn as sns
from scipy.stats import binom, beta


N = 980
F = 437
M = N - F

xvals = np.linspace(0,1)

prior = beta.pdf(xvals, 1, 1)
like = binom.pmf(F, n=N, p=xvals)
like = beta.pdf(xvals, F+1, M+1)

sns.plt.plot(xvals, prior)