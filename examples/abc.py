import numpy as np
import pandas as pd

def abc(y, N, epsilon):

    trace = []

    while len(trace) < N:

        # Simulate from priors
        mu = np.random.normal(0, 10)
        sigma = np.random.uniform(0, 20)

        x = np.random.normal(mu, sigma, 50)

        #if (np.linalg.norm(y - x) < epsilon):
        if ((abs(x.mean() - y.mean()) < epsilon[0]) &
            (abs(x.std() - y.std()) < epsilon[1])):
            trace.append([mu, sigma])

    return pd.DataFrame(trace, columns=['mu', 'sigma'])

if __name__ == '__main__':
    y = np.random.normal(4, 2, 50)
    N = 20
    epsilon = [0.2, 0.8]
    print(abc(y, N, epsilon).mean(0))