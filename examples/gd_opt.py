%%cython --annotate
from scipy import optimize

import numpy as np
cimport numpy as np
from numpy cimport *

cdef double f(list x, double epsilon=0.8, int ndim=2):
    cdef:
        np.ndarray[np.float64_t, ndim=1] y = np.copy(x)
    y *= np.power(epsilon, np.arange(ndim))
    return .33*np.sum(y**2)

cdef double f_prime(list x, double epsilon=0.8, int ndim=2):
    
    cdef:
        np.ndarray[np.float64_t, ndim=1] y = np.copy(x)
    
    scaling = np.power(epsilon, np.arange(ndim))
    y *= scaling
    return .33*2*scaling*y


cpdef gradient_descent2(list x0, f, f_prime, adapt=False):
    
    cdef:
        double x_i, y_i
        int i
        list all_x_i=[]
        list all_y_i=[]
        list all_f_i=[]
        
    x_i, y_i = x0

    for i from 1 <= i < 100:
        all_x_i.append(x_i)
        all_y_i.append(y_i)
        all_f_i.append(f([x_i, y_i]))
        dx_i, dy_i = f_prime(np.asarray([x_i, y_i]))
        if adapt:
            # Compute a step size using a line_search
            step = optimize.line_search(f, f_prime,
                                np.r_[x_i, y_i], -np.r_[dx_i, dy_i],
                                np.r_[dx_i, dy_i], c2=.05)
            step = step[0]
        else:
            step = 1
        x_i += -step*dx_i
        y_i += -step*dy_i
        if np.abs(all_f_i[-1]) < 1e-16:
            break
    return all_x_i, all_y_i, all_f_i


x0, y0 = 1.6, 1.1

f, f_prime = quad(0.8)
%timeit gd_x_i, gd_y_i, gd_f_i = gradient_descent2([x0, y0], f, f_prime)