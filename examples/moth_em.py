### EXAMPLE 4.2 EM ALGORITHM (PEPPERED MOTHS)

#########################################################################
# x = observed phenotype counts (carbonaria, insularia, typica)
# n = expected genotype frequencies (CC, CI, CT, II, IT, TT)
# p = allele probabilities (carbonaria, insularia, typica)
# itr = number of iterations
# allele_e = computes expected genotype frequencies
# allele_m = computes allele probabilities
#########################################################################

import numpy as np

C, I, T = 0, 1, 2

## EXPECTATION AND MAXIMIZATION FUNCTIONS
def allele_e(x, p):
    En_cc = (x[C]*(p[C]**2)) / ((p[C]**2) + 2*p[C]*p[I] + 2*p[C]*p[T])
    En_ci = (2*x[C]*p[C]*p[I]) / ((p[C]**2) + 2*p[C]*p[I] + 2*p[C]*p[T])
    En_ct = (2*x[C]*p[C]*p[T]) / ((p[C]**2) + 2*p[C]*p[I] + 2*p[C]*p[T])
    En_ii = (x[I]*(p[I]**2)) / ((p[I]**2) + 2*p[I]*p[T])
    En_it = (2*x[I]*p[I]*p[T]) / ((p[I]**2) + 2*p[I]*p[T])
    
    return(En_cc, En_ci, En_ct, En_ii, En_it, x[2])

CC, CI, CT, II, IT, TT = range(6)

def allele_m (x, n):
    p_c = (2*n[CC] + n[CI] + n[CT]) / (2*x.sum())
    p_i = (2*n[II] + n[IT] + n[CI]) / (2*x.sum())
    p_t = (2*n[-1] + n[CT] + n[IT]) / (2*x.sum())
    
    return(p_c, p_i, p_t)

def run(itr=40):
    
    x = np.array([85, 196, 341])
    n = np.zeros(6)
    p = np.ones(3)*(1/3)
    
    for i in range(itr):
        n = allele_e(x,p)
        p = allele_m(x,n)
    return p

if __name__ == '__main__':
    print(run())