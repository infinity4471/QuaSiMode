import numpy as np
from node import node
from operations import make_tuple
import matplotlib.pyplot as plt
from state import state

import networkx as nx

class circuit:
    def __init__( self, states = None ):
        if states is None:
            self.roots = []
            self.nodes = []
        else:
            self.nodes = states
            self.roots = states
        self.name_dict = {}
        for node in self.nodes:
            self.name_dict[ node.get_name() ] = node.get_matrix()

    def add_state( self, state ):
        if state.get_name() in self.name_dict.keys():
            return
        self.roots.append( state )
        self.add_node( state )
    
    def add_node( self, node ):
        if node.get_name() in self.name_dict.keys():
            return
        self.name_dict[ node.get_name() ] = np.ndarray.tolist( node.get_matrix() )
        self.nodes.append( node )

    def add_gate( self, node_name, gate ):
        self.add_node( node( gate.name, gate.get_matrix() ) )
        for ( v, idx ) in zip( self.nodes, range( len( self.nodes ) ) ):
            if node_name == v.name:
                self.nodes[ idx ].add_gate( gate )
    
    def execute_aux( self, node ):
        cur_state = state("R")
        for parent in self.nodes:
            if parent.next is None:
                continue
            if parent.next.get_name() == node.get_name():
                par_state = self.execute_aux( parent )
                cur_state.add_state( par_state )
        if cur_state.get_matrix() is None:
            cur_state.set_state( node.get_matrix() )
        else:
            cur_state.apply_operator( node )
        return cur_state

    def execute_circuit( self ): #returns state
        sinks = []
        for node in self.nodes:
            if node.next is None:
                sinks.append( node )
        cur_state = state( "result" )
        for node in sinks:
            new_state = self.execute_aux( node )
            cur_state.add_state( new_state )  
        return cur_state

    def export( self ):
        circuit = {}
        for node in self.nodes:
            if not node.next is None:
                circuit[ node.get_name() ] = node.next.get_name()
        return circuit
    
    def get_names( self ):
        return self.name_dict

    def visualize( self ):
        edges = []
        for node in self.nodes:
            if not node.next is None:
                edges.append( [ node.get_name(), node.next.get_name() ] )
        graph = nx.DiGraph()
        graph.add_edges_from( edges )
        nx.draw_networkx( graph )
        plt.show()