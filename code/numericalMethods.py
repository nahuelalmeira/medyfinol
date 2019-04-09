"""

Auxiliary numerical methods for finding a function's zeros

"""

import sys
import numpy as np

def bisection(f, a, b, error=1E-7):
    """
    
    Finds a zero for function f in the interval (a, b).
    f is supposed to be continuos. 
    If a and b have the same sign, it returns np.NaN.

    >>> f = lambda x: x**3 - 1
    >>> x = bisection(f, 0.1, 3.5)
    >>> np.fabs(1 - x) < 1E-7
    True
    >>> f = lambda x: np.log2(x)
    >>> x = bisection(f, 0.1, 3.5)
    >>> np.fabs(1 - x) < 1E-7
    True
    
    """
    
    if(f(a)*f(b) > 0):
        print('f(a) and f(b) have same sign', file=sys.stderr)
        return np.NaN

    p = (a + b)/2
    error = np.fabs(f(p))
    while error > 1E-7:
        
        if f(a)*f(p) < 0:
            b = p
        else:
            a = p         

        p = (a + b)/2
        error = np.fabs(f(p))

    return p


if __name__ == "__main__":
    import doctest
    doctest.testmod()