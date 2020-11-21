import numpy as np

class operator:
    def __init__( self, matrix = None ):
        if matrix is None:
            self.matrix = np.ones( (2, 2 ) )
        else:
            self.matrix = matrix
    def apply( self, operator ):
        self.matrix = self.matrix.dot( operator.get_matrix() )
    def get_matrix( self ):
        return self.matrix