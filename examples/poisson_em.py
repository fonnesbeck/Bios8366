import numpy as np
from scipy.stats.distributions import poisson

# True parameter values
mu_true = 1.5
psi_true = .4
n = 100

# Simulate some data
data = np.array([np.random.poisson(mu_true)*(np.random.random()<psi_true) for i in range(n)])

def Estep(x, mu, psi):
    a = (1 - psi)*(x==0)
    b = psi * poisson.pmf(x, mu)
    return b / (a + b)
    
def Mstep(x, w):
    psi = np.mean(w) 
    
    mu = np.sum(w * x)/np.sum(w)
    
    return mu, psi
    
# Initialize values
mu = np.random.uniform(0, 5)
psi = np.random.random()

# Stopping criterion
crit = 1e-6

# Convergence flag
converged = False

x = data
# Loop until converged
while not converged:
    
    # E-step
    w = Estep(x, mu, psi)
    # M-step
    mu_new, psi_new = Mstep(x, w)
    
    # Check convergence
    converged = ((np.abs(psi_new - psi) < crit) 
                 & np.all(np.abs((np.array(mu_new) - np.array(mu)) < crit)))
    mu, psi = mu_new, psi_new
 
print(mu, psi)