# Log dose in each group
log_dose = [-.86, -.3, -.05, .73]

# Sample size in each group
n = 5

# Outcomes
deaths = [0, 1, 3, 5]

invlogit = pm.math.invlogit

with pm.Model() as bioassay:
    
    a = pm.Normal('a', 0, 5)
    b = pm.Normal('b', 0, 5)
    
    p = invlogit(a + b*np.array(log_dose))
    
    y = pm.Binomial('y', n=n, p=p, observed=np.array(deaths))
    
    LD50 = pm.Deterministic('LD50', -a/b)