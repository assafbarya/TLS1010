import numpy as np
from copy import deepcopy

def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

@memoize
def subTourCost( m, citiesToVisit, startingCity, endingCity ):
    if not citiesToVisit:
        return m[ startingCity ][ endingCity ]

    combinations = np.full( len( citiesToVisit ), np.nan )
    for idx, firstInTrip in enumerate( citiesToVisit ):
        listCopy = tuple( x for x in citiesToVisit if x is not firstInTrip )
        combinations[ idx ] = m[ startingCity ][ firstInTrip ] + subTourCost( m, listCopy, firstInTrip, endingCity )

    return float( combinations.min() )

def main():

    size = 10
    m = np.random.random_integers(0,100,( size,size))
    print (m)

    m = m + m.T - np.diag(m.diagonal())
    print (m)

    mm = tuple( tuple(r) for r in m )
    cities = tuple( range(size))

    print(subTourCost(mm,cities,0,0))






main()

