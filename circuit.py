import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

from node import node
from state import state

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

    def add_gate( self, cur_node, gate ):
        self.add_node( node( gate.get_name(), gate.get_matrix() ) )
        added_node = None
        for v in self.nodes:
            if v.get_name() == cur_node.get_name():
                added_node = v
                break
        for ( v, idx ) in zip( self.nodes, range( len( self.nodes ) ) ):
            if v.get_name() == gate.get_name():
                self.nodes[ idx ].add_gate( added_node )

    def execute_aux( self, node ):
        cur_state = state("R")
        for child in node.get_next():
            child_state = self.execute_aux( child )
            cur_state.add_state( child_state )

        if cur_state.get_matrix() is None:
            cur_state.set_state( node.get_matrix() )
        else:
            cur_state.apply_operator( node )
        return cur_state

    def execute_circuit( self ): #returns state
        cur_state = state( "result" )
        for node in self.nodes:
            status = True
            for parent in self.nodes:
                for child in parent.get_next():
                    if child.get_name() == node.get_name():
                        status = False
                        break
            if status:
                new_state = self.execute_aux( node )
                cur_state.add_state( new_state )  
        return cur_state

    def export( self ):
        circuit = {}
        for node in self.nodes:
            for child in node.get_next():
                if not node.get_name() in circuit.keys():
                    circuit[ node.get_name() ] = []
                circuit[ node.get_name() ].append( child.get_name() )
        return circuit
    
    def get_names( self ):
        return self.name_dict

    def visualize( self ):
        edges = []
        for node in self.nodes:
            for child in node.get_next():
                edges.append( [ node.get_name(), child.get_name() ] )
        graph = nx.DiGraph()
        graph.add_edges_from( edges )
        nx.draw_networkx( graph )
        plt.show()