class node:
    def __init__( self, name, matrix ):
        self.matrix = matrix
        self.name = name
        self.next = []

    def get_next( self ):
        return self.next

    def get_name( self ):
        return self.name

    def get_matrix( self ):
        return self.matrix

    def add_gate( self, gate ):
        self.next.append( gate )