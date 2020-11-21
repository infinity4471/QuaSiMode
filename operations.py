import numpy as np
from collections.abc import Iterable

def tensor_product( v1, v2 ):
    res = []
    for x in v1:
        for y in v2:
            res.append( x * y )
    return np.array( res )

def tobinary( number, len ):
    return ("{0:0" + str( len ) + "b}").format( number )

def make_tuple( item ):
    if not isinstance( item, Iterable):
        return item
    mytuple = []
    for x in item:  
        mytuple.append( make_tuple( x ) )
    return tuple( mytuple )