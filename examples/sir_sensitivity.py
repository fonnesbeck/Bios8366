datasets = [cancer.drop(i).values.T for i in range(len(cancer))]

def sir(data, var=var, mode=mode, samples=1000):
    
    y, n = data
    
    # Sample from q
    theta = rmvt(5, var, mode, size=samples)
    
    f_theta = np.array([betabin_trans(t, n, y) for t in theta])
    
    q_theta = mvt(theta, 4, var, mode)
    
    w = np.exp(f_theta - q_theta - max(f_theta - q_theta))
    
    p_sir = w/w.sum()
    
    theta_sir = theta[np.random.choice(range(len(theta)), size=samples, p=p_sir)]
    
    logK_sample = theta_sir[:,1]
    
    return logK_sample
    
samples = [sir(d) for d in datasets]

_ = plt.boxplot(samples)