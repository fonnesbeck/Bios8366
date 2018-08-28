def fixed_point(func, a0, tol=1e-10):
    
    a = func(a0)
    
    while np.abs(a - a0) > tol:
        a0 = a
        a = func(a0)
        
    return a

g = lambda x: dlgamma(x) + x

fixed_point(g, 3)