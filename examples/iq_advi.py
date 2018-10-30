μ_m = y.value.mean()
μ_s = y.value.std() * 2
σ_low = 1
σ_high = 10

with pm.Model() as model:
    group1_mean = pm.Normal('group1_mean', μ_m, sd=μ_s)
    group2_mean = pm.Normal('group2_mean', μ_m, sd=μ_s)

    group1_std = pm.Uniform('group1_std', lower=σ_low, upper=σ_high)
    group2_std = pm.Uniform('group2_std', lower=σ_low, upper=σ_high)
    
    ν = pm.Exponential('ν_minus_one', 1/29.) + 1
    
    diff_of_means = pm.Deterministic('difference of means', group1_mean - group2_mean)


    λ1 = group1_std**-2
    λ2 = group2_std**-2

    group1 = pm.StudentT('drug', nu=ν, mu=group1_mean, lam=λ1, observed=y1)
    group2 = pm.StudentT('placebo', nu=ν, mu=group2_mean, lam=λ2, observed=y2)
    
with model:
    tr = pm.sample(1000, tune=2000, chains=1)
    
with model:
    
    approx = pm.fit(method='fullrank_advi')
    
plt.hist(tr['difference of means'], label='mcmc', alpha=0.4, bins=np.arange(-2, 4, step=0.2))
plt.hist(approx.sample(1000)['difference of means'], label='vi', alpha=0.4, bins=np.arange(-2, 4, step=0.2))
plt.legend()