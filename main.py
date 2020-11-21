from state import state
from quantum_operator import operator
import numpy as np
from math import sqrt

#Test application - Entanglement

cur = state( np.array( [ 0, 1 ] ) )
hadamard = operator( np.array( [ [ 1/sqrt(2), 1/sqrt(2) ], [ 1/sqrt( 2 ), -1/sqrt(2) ] ] ) )
cur.apply_operator( hadamard )
cur.add_state( state( [ 1, 0 ] ) )

cnot = operator( np.array( [ [ 1, 0, 0, 0 ], [ 0, 1, 0, 0 ], [ 0, 0, 0, 1 ], [0 ,0, 1, 0 ] ] ) )

cur.apply_operator( cnot )

print( cur.evaluate_results() )
cur.plot_results()