import numpy as np

def fixed_point(func, a0, tol=1e-10):
    
    a = func(a0)
    
    while np.abs(a - a0) > tol:
        a0 = a
        a = func(a0)
        
    return a

g = lambda x: (5 - x**3) / 5

fixed_point(g, 0.75)