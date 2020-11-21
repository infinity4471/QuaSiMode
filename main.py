from state import state
from quantum_operator import operator
from circuit import circuit
from node import node

import numpy as np
from math import sqrt

#Test application - Entanglement

cur = state( "q0", np.array( [ 1, 0 ] ) )
hadamard = operator( "H", np.array( [ [ 1/sqrt(2), 1/sqrt(2) ], [ 1/sqrt( 2 ), -1/sqrt(2) ] ] ) )
cnot = operator( "CX", np.array( [ [ 1, 0, 0, 0 ], [ 0, 1, 0, 0 ], [ 0, 0, 0, 1 ], [0 ,0, 1, 0 ] ] ) )
new_qubit = state( "q1", np.array( [1, 0 ] ) )

'''
cur.apply_operator( hadamard )
cur.add_state( state( "newzero", [ 1, 0 ] ) )

cur.apply_operator( cnot )

print( cur.evaluate_results() )
#cur.plot_results()
'''

## Circuit to implement entanglement

mycir = circuit()
mycir.add_state( cur )
mycir.add_gate( "q0", hadamard )
mycir.add_state( new_qubit )
mycir.add_gate( "q1", cnot )
mycir.add_gate( "H", cnot )
print( mycir.export() )

res_state = mycir.execute_circuit()
res_state.evaluate_results()
print( res_state.nqubits )
print( res_state.get_results() )
res_state.plot_results()
mycir.visualize()