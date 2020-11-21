import numpy as np
import matplotlib.pyplot as plt
from math import log2

from operations import tensor_product, tobinary

class state:
    def __init__( self, init_state = None ):
        if state is None:
            self.vector = np.array( [ 1., 0. ] )
        else:
            init_state = np.array( list( map( float, init_state ) ) )
            self.vector = np.array( init_state )
        self.nqubits = int( log2( len( self.vector ) ) )
        self.results = {}

    def set_state( self, new_state ):
        self.vector = new_state
    
    def add_state( self, new_state ):
        self.vector = tensor_product( self.vector, new_state.get_state() )
        self.nqubits += new_state.nqubits

    def get_state( self ):
        return self.vector
    
    def get_results( self ):
        return self.results

    def apply_operator( self, operator ):
        self.vector = operator.get_matrix().dot(  self.vector )    
    
    def measure( self ):
        distribution = np.square( self.vector )
        return np.random.choice( range( len( self.vector ) ), p = distribution )
    
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