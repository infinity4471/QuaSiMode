import numpy as np

class operator:
    def __init__( self, matrix = None ):
        if matrix is None:
            self.matrix = np.array( [ [ 1., 0. ], [ 0., 1. ] ] )
        else:
            self.matrix = matrix
        assert self.valid_operator()

    def valid_operator( self ):
        for ( r1, r2 ) in zip( np.linalg.inv( self.matrix ), self.matrix ):
            for x, y in zip( r1, r2 ):
                if abs( x - y ) > 1e-5:
                    return False
        return True

    def apply( self, operator ):
        self.matrix = self.matrix.dot( operator.get_matrix() )

    def get_matrix( self ):
        return self.matrix