from circuit import circuit
from quantum_operator import operator
from node import node
from state import state

import numpy as np
from math import sqrt

#Test application - Entanglement

q0 = state( "q0", np.array( [ 1, 0 ] ) )
hadamard = operator( "H", np.array( [ [ 1/sqrt(2), 1/sqrt(2) ], [ 1/sqrt( 2 ), -1/sqrt(2) ] ] ) )
cnot = operator( "CX", np.array( [ [ 1, 0, 0, 0 ], [ 0, 1, 0, 0 ], [ 0, 0, 0, 1 ], [0 ,0, 1, 0 ] ] ) )
q1 = state( "q1", np.array( [1, 0 ] ) )

q0.apply_operator( hadamard )
q0.add_state( q1 )
q0.apply_operator( cnot )

print( q0.evaluate_results() )
q0.plot_results()
