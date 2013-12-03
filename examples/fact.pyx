cdef extern from "fact.h":
    int _fact "fact"(int)

def fact(int n):
    return _fact(n)