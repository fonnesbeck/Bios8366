precip = pd.read_table("../data/nashville_precip.txt", sep='\s+')

month = 'Sep'

# Calculate statistics
log_mean = precip.mean().apply(np.log)
mean_log = precip.apply(np.log).mean()

from scipy.special import psi

def dlgamma(m): 
    return np.log(m) - psi(m) - log_mean[month] + mean_log[month]
    
fp = lambda x: dlgamma(x) + x

a0 = 4
a = fp(a0)
while np.abs(a-a0) > 1e-6:
    a0 = a
    a = fp(a0)
    
print(a)