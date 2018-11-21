"""

Methods for computing entropy, distance to equilibrium and complexity

"""

import numpy as np


from numericalMethods import bisection

def entropy(px):
    """
    Compute entropy in bits of variable X with 
    probability distribution px.

    Parameters:

    ---- (array-like) px

    Doctest:
    >>> entropy([0.25, 0.25, 0.25, 0.25])
    2.0
    >>> entropy([1, 1, 1, 1, 1, 1, 1, 1])
    3.0
    >>> entropy([1/2, 1/4, 1/8, 1/16, 1/64, 1/64, 1/64, 1/64])
    2.0
    
    """
    N = len(px)
    px = np.array(px) / np.sum(px)
    H = 0
    for x in px:
        if x > 0 and x < 1:
            H -= x*np.log2(x)
    return H

def normEntropy(px):
    """
    Compute normalized entropy in bits of variable X with 
    probability distribution px. Normalized entropy
    is always in the interval [0, 1].

    Parameters:

    ---- (array-like) px

    Doctest:
    >>> normEntropy([0.25, 0.25, 0.25, 0.25])
    1.0
    >>> normEntropy([1, 1, 1, 1, 1, 1, 1, 1])
    1.0
    >>> normEntropy([1/2, 1/4, 1/8, 1/16, 1/64, 1/64, 1/64, 1/64])
    0.6666666666666666
    """

    N = len(px)
    return entropy(px) / np.log2(N)

def desequilibrium(px):
    """
    Compute desequilibrium of variable X with probability
    distribution px.

    Parameters:

    ---- (array-like) px

    Doctest:
    >>> desequilibrium([0.25, 0.25, 0.25, 0.25])
    0.0
    >>> desequilibrium([1, 1, 1, 1, 1, 1, 1, 1])
    0.0

    """

    px = np.array(px) / np.sum(px)
    N = len(px)
    p_eq = 1. / N
    D = np.sum( (px - p_eq)**2 )
    return D

def _f_min(x, N, n, H):
    """
    Eq. (16) in Ref. [1] equaled to zero
    """

    rhm = ( x*np.log2(x) + (1-x)*np.log2( (1-x)/(N-n-1) ) ) / np.log2(N)
    
    return H + rhm

def _f_max(x, N, H):
    """
    Eq. (13) in Ref. [1] equaled to zero
    """

    return _f_min(x, N, 0, H)

def compute_Dmin(N, n, fmin):
    """
    Eq. (17) in Ref. [1]
    """

    fe = 1/N
    aux = (N-n-1)*( (1-fmin)/(N-n-1) - fe )**2

    return (fmin - fe)**2 + aux + n*fe**2

def compute_Dmax(N, fmax):
    """
    Eq. (14) in Ref. [1]
    """

    fe = 1/N
    aux = (N-1)*( (1-fmax)/(N-1) - fe )**2

    return (fmax - fe)**2 + aux

def compute_fmax(_f_max, a, b, N, H, computeZero=bisection):
    _f_max_bisection = lambda x: _f_max(x, N, H)

    return computeZero(_f_max_bisection, a, b)

def compute_fmin(_f_min, a, b, N, n, H, computeZero=bisection):
    _f_min_bisection = lambda x: _f_min(x, N, n, H)

    return computeZero(_f_min_bisection, a, b)


def complexityBounds(N, H_range):

    Cmin_values = []
    Cmax_values = []
    for H in H_range:
        
        a = 0.99
        b = 1 - 1E-8
        while( (_f_max(a, N, H)*_f_max(b, N, H) > 0) and (a > 0.001) ):
            a -= 0.001

        fmax = compute_fmax(_f_max, a, b, N, H)
        Dmax = compute_Dmax(N, fmax)
        Cmax = Dmax*H
        
        Dmin = 10E8
        for n in range(N-1):
                       
            a = 1E-8
            b = 0.001
            while( (_f_min(a, N, n, H)*_f_min(b, N, n, H) > 0) and 
                   (b <= 1) ):
                b += 0.001  

            if(_f_min(a, N, n, H)*_f_min(b, N, n, H) > 0):
                print('No crossing zero for n =', n, ' H =', H, 
                      sys.stderr)
                break

            fmin = compute_fmin(_f_min, a, b, N, n, H)
            Dmin = min(Dmin, compute_Dmin(N, n, fmin))

        Cmin = Dmin*H

        Cmax_values.append(Cmax)
        Cmin_values.append(Cmin)
            
    return Cmin_values, Cmax_values


if __name__ == "__main__":
    import doctest
    doctest.testmod()