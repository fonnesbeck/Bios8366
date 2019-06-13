def studentized_pivotal_interval(fun, data, R=1000, interval=[97.5, 2.5]):
    
    Tnr = np.array([fun(data.sample(n, replace=True)) for r in range(R)])
    Tn = fun(data)
    se = Tnr.std()
    z = (Tnr - Tn) / se
    zs = np.percentile(z, interval)
    return Tn - zs * se
