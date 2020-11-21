class node:
    def __init__( self, outputs = None ):
        if outputs is None:
            self.outputs = []
        else:
            self.outputs = outputs
    def get_outputs( self ):
        return self.outputs
    def add_node( self, node ):
        self.outputs.append( node )