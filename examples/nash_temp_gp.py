x, y = temps_2010.reset_index().values.T
X = (x - x.min()).astype(int).reshape(-1, 1)

with pm.Model() as temp_model:
    
    ℓ = pm.Gamma("ℓ", alpha=2, beta=1)
    η = pm.HalfCauchy("η", beta=5)
    
    m = pm.gp.mean.Constant(temps_2010.mean())
    cov = η**2 * pm.gp.cov.Matern52(1, ℓ)
    gp = pm.gp.MarginalSparse(cov_func=cov, approx="FITC")
    
    Xu = pm.gp.util.kmeans_inducing_points(15, X)
    
    σ = pm.HalfCauchy("σ", beta=5)
    obs = gp.marginal_likelihood("obs", X=X, Xu=Xu, y=y, noise=σ)
    
    trace = pm.sample(1000, chains=1)
    
# add the GP conditional to the model, given the new X values
with temp_model:
    f_pred = gp.conditional("f_pred", X, pred_noise=True)

# To use the MAP values, you can just replace the trace with a length-1 list with `mp`
with temp_model:
    pred_samples = pm.sample_ppc(trace, vars=[f_pred], samples=10)
    
    
x = X.flatten()
# plot the results
fig = plt.figure(figsize=(12,5)); ax = fig.gca()

# plot the samples from the gp posterior with samples and shading
from pymc3.gp.util import plot_gp_dist
plot_gp_dist(ax, pred_samples["f_pred"], x);

# plot the data and the true latent function
plt.plot(x, y, 'ok', ms=3, alpha=0.5, label="Observed data");
plt.plot(Xu, 10*np.ones(Xu.shape[0]), "co", ms=10, label="Inducing point locations")

# axis labels and title
plt.xlabel("X");
plt.title("Posterior distribution over $f(x)$ at the observed values"); plt.legend();