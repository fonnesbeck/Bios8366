n = 980
y = 437

from scipy.stats import binom, beta
import numpy as np
import matplotlib.pyplot as plt

xvalues = np.linspace(0.3, 0.6, num=1000)
prior = beta(49, 53).pdf(xvalues)
plt.plot(xvalues, prior/prior.max(), label='prior')

like = binom(n, xvalues).pmf(y)
plt.plot(xvalues, like/like.max(), label='likelihood')

post = beta(y+49, n-y+53).pdf(xvalues)
plt.plot(xvalues, post/post.max(), label='posterior')

plt.legend()