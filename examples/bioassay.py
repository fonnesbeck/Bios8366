# Formula for LD 50
ld50 = lambda alpha, beta: -alpha/beta

# Inverse-logit transformation
invlogit = lambda x: 1/(1. + np.exp(-x))

dbinom = distributions.binom.logpmf
dnorm = distributions.norm.logpdf

def bioassay_post(alpha, beta):

    logp = dnorm(alpha, 0, 10000) + dnorm(beta, 0, 10000)

    p = invlogit(alpha + beta*np.array(log_dose))

    logp += dbinom(deaths, n, p).sum()

    return logp

def metropolis_bioassay(n_iterations, initial_values, prop_var=1,
                     tune_for=None, tune_interval=100):

    n_params = len(initial_values)

    # Initial proposal standard deviations
    prop_sd = [prop_var] * n_params

    # Initialize trace for parameters
    trace = np.empty((n_iterations+1, n_params))

    # Set initial values
    trace[0] = initial_values
    # Initialize acceptance counts
    accepted = [0]*n_params

    # Calculate joint posterior for initial values
    current_log_prob = calc_posterior(*trace[0])

    if tune_for is None:
        tune_for = n_iterations/2

    for i in range(n_iterations):

        if not i%1000: print 'Iteration', i

        # Grab current parameter values
        current_params = trace[i]

        for j in range(n_params):

            # Get current value for parameter j
            p = trace[i].copy()

            # Propose new value
            theta = rnorm(current_params[j], prop_sd[j])

            # Insert new value
            p[j] = theta

            # Calculate log posterior with proposed value
            proposed_log_prob = calc_posterior(*p)

            # Log-acceptance rate
            alpha = proposed_log_prob - current_log_prob

            # Sample a uniform random variate
            u = runif()

            # Test proposed value
            if np.log(u) < alpha:
                # Accept
                trace[i+1,j] = theta
                current_log_prob = proposed_log_prob
                accepted[j] += 1
            else:
                # Reject
                trace[i+1,j] = trace[i,j]

            # Tune every 100 iterations
            if (not (i+1) % tune_interval) and (i < tune_for):

                # Calculate aceptance rate
                acceptance_rate = (1.*accepted[j])/tune_interval
                if acceptance_rate<0.2:
                    prop_sd[j] *= 0.9
                elif acceptance_rate>0.5:
                    prop_sd[j] *= 1.1

                accepted[j] = 0

    return trace[tune_for:], accepted

# Run MCMC
tr, acc = metropolis_bioassay(10000, (0,0))

for param, samples in zip(['intercept', 'slope'], tr.T):
    fig, axes = plt.subplots(1, 2)
    axes[0].plot(samples)
    axes[0].set_ylabel(param)
    axes[1].hist(samples[len(samples)/2:])

a, b = tr.T
print('LD50 mean is {}'.format(ld50(a,b).mean()))