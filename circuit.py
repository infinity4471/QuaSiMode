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

class circuit:
    def __init__( self, states = None ):
        if states is None:
            self.roots = []
            self.nodes = []
        else:
            self.nodes = states
            self.roots = states

    def add_state( self, state ):
        self.root.append( state )
        self.nodes.append( state )
    
    def add_gate( self, node, gate ):
        for ( v, idx ) in zip( self.nodes, range( len( nodes ) ) ):
            if v == node:
                self.nodes[ i ].add_node( gate )
    
    def execute_circuit( self ): #returns state
        pass