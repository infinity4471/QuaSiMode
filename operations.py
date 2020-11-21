import numpy as np

def tensor_product( v1, v2 ):
    res = []
    for x in v1:
        for y in v2:
            res.append( x * y )
    return np.array( res )

def tobinary( number, len ):
    return ("{0:0" + str( len ) + "b}").format( number )