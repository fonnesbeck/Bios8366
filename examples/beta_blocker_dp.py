N_dp = 10

def stick_breaking(beta):
    portion_remaining = tt.concatenate([[1], tt.extra_ops.cumprod(1 - beta)[:-1]])
    v = beta * portion_remaining
    return v/v.sum()

with pm.Model() as beta_blockers:
    
    μ = pm.Normal('μ', -1, sd=5)
    
    α = pm.Exponential('α', 1)
    θ = pm.Normal('θ', 0, sd=5, shape=N_dp)
    
    v = pm.Beta('v', alpha=1, beta=α, shape=N_dp)
    
    p = pm.Deterministic('p', stick_breaking(v))
    
    π_c = pm.math.invlogit(μ)
    π_t = pm.math.invlogit(μ + θ)
    
    r_c = pm.Binomial('r_c', n_c_obs, π_c, observed=r_c_obs)
    mixture_dists = [pm.Binomial.dist(n_t_obs, π_t[i]) for i in range(N_dp)]
    r_t = pm.Mixture('r_t', w=p, comp_dists=mixture_dists, observed=r_t_obs)