import numpy as np

from node import node

class operator( node ):
    def __init__( self, name, matrix = None ):
        super().__init__( name, matrix )
        assert self.valid_operator()

    def valid_operator( self ):
        for ( r1, r2 ) in zip( np.linalg.inv( self.matrix ), self.matrix ):
            for x, y in zip( r1, r2 ):
                if abs( x - y ) > 1e-5:
                    return False
        return True

    def apply( self, operator ):
        print( self.matrix )
        print( operator.get_matrix( ) )
        self.matrix = self.matrix.dot( operator.get_matrix() )

    def get_matrix( self ):
        return self.matrix