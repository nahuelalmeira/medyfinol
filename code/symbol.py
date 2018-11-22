"""

Methods for performing symbol analysis

"""
import numpy as np
from itertools import permutations

def symbolCount(data, D):
    """ 
    Performs symbol analysis of the data
    using words of length D 
    
    Parameters:

    ---- (array-like) data: series to be analyzed
    ---- (int)           D: Word length

    >>> data = [0.1, 0.2, 0.3, 0.4]
    >>> symbolCount(data, 2)
    [3, 0]
    >>> symbolCount(data, 3)
    [2, 0, 0, 0, 0, 0]
    >>> data = [0.2, 0.1, 0.3, 0.4]
    >>> symbolCount(data, 2)
    [2, 1]
    >>> symbolCount(data, 3)
    [1, 0, 1, 0, 0, 0]

    """

    N = len(data)
    perm_dict = {}
    Permutations = list(permutations(range(D)))
    for i, perm in enumerate(Permutations):
        perm_dict[perm] = i
    n_words = len(Permutations)  # number of different words (n_words = D!)

    Z = [0] * n_words
    for i in range(N - (D - 1)):
        perm = np.argsort(data[i:i + D])
        perm = tuple(int(elem) for elem in perm)
        Z[perm_dict[perm]] += 1

    return Z


if __name__ == "__main__":
    import doctest
    doctest.testmod()