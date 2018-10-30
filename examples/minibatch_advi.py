size = 500000
true_intercept = 1
true_slope = 2
x = np.linspace(0, 1, size)
# y = a + b*x
true_regression_line = true_intercept + true_slope * x
# add noise
y = true_regression_line + np.random.normal(scale=.5, size=size)

batchsize = 5000
x_minibatch = pm.Minibatch(x, batch_size=batchsize)
y_minibatch = pm.Minibatch(y, batch_size=batchsize)

with pm.Model() as model_vi: # 
    # Define priors
    sigma = pm.HalfCauchy('sigma', beta=10, testval=1.)
    intercept = pm.Normal('Intercept', 0, sd=20)
    x_coeff = pm.Normal('x', 0, sd=20)
    #define model mean in terms of minibatch tensor
    mean = intercept + x_coeff * x_minibatch
    # Define likelihood
    likelihood = pm.Normal('likelihood', mu = mean, sd = sigma, observed=y_minibatch, total_size = len(y))