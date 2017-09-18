cdef float ff(float x):
    return 2*x*x + 3*x + 1

def trapez(float a, float b, int n):
    cdef float h, x, sumy
    cdef int i
    h = (b-a)/float(n)
    sumy = 0
    x=a
    for i in range(n):
        x += h
        sumy += ff(x)
    sumy += 0.5*(ff(a) + ff(b))
    return sumy*h