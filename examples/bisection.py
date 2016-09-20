def bisection(f, a, b, tol=1e-9, max_iter=100):

    # Check initial values
    if a >= b:
        raise ValueError('Right value must be larger than left')

    fa, fb = f(a), f(b)

    if fa*fb > 0:
        raise ValueError('No maximum between specified values')

    i = 0
    while (b - a) > tol:

        # More stable than c = (b + a)/2.
        c = a + (b - a)/2.
        fc = f(c)

        if fa*fc < 0:
            b,fb = c,fc
        else:
            a,fa = c,fc

        i +=1

        if i == max_iter:
            print('The algorithm did not converge in {0} iterations'.format(max_iter))
            return(None)

    return((a+b)/2., i)
    
if __name__ == '__main__':
    bisection(lambda x: -2*x + 5, -10, 10)