import theano.tensor as T

def make_vector():
    """
    Create and return a new Theano vector.
    """

    return T.dvector()

def make_matrix():
    """
    Create and return a new Theano matrix.
    """

    return T.dmatrix()

def elemwise_mul(a, b):
    """
    a: A theano matrix
    b: A theano matrix
    
    Calcuate the elementwise product of a and b and return it
    """

    return a * b

def matrix_vector_mul(a, b):
    """
    a: A theano matrix
    b: A theano vector
    
    Calculate the matrix-vector product of a and b and return it
    """

    return T.dot(a, b)

a = make_vector()
b = make_vector()
c = elemwise_mul(a, b)
d = make_matrix()
matrix_vector_mul(d, c)