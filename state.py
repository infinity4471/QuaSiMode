import numpy as np
import matplotlib.pyplot as plt
from math import log2

from node import node
from operations import tensor_product, tobinary

class state( node ):
    def __init__( self, name, init_state = None ):
        super().__init__( name, init_state )
        if not init_state is None:
            self.nqubits = int( log2( len( self.matrix ) ) )
        else:
            self.nqubits = 0
        self.results = {}

    def set_state( self, new_state ):
        self.matrix = new_state
        self.nqubits = int( log2( len( self.matrix ) ) )

    
    def add_state( self, new_state ):
        if self.matrix is None:
            self.nqubits = new_state.nqubits
            self.matrix = new_state.get_matrix()
            return
        self.matrix = tensor_product( self.matrix, new_state.get_matrix() )
        self.nqubits += new_state.nqubits

    def get_matrix( self ):
        return self.matrix

    def apply_operator( self, operator ):
        self.matrix = operator.get_matrix().dot(  self.matrix )    
    
    def measure( self ):
        distribution = np.square( self.matrix )
        return np.random.choice( range( len( self.matrix ) ), p = distribution )
    
    def evaluate_results( self, shots = 1024 ):
        self.results = {}
        for _ in range( shots ):
            measured = tobinary( self.measure(), self.nqubits )
            if not measured in self.results.keys():
                self.results[ measured ] = 0
            else:
                self.results[ measured ] += 1
        return self.results
    
    def plot_results( self ):
        plt.bar(self.results.keys(), self.results.values(), color='b')
        plt.show()
    
    def get_results( self ):
        return self.results