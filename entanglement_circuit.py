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

## Circuit to implement entanglement

mycir = circuit()
mycir.add_state( q0 )
mycir.add_state( q1 )
mycir.add_gate( q0, hadamard )
mycir.add_gate( hadamard, cnot )
mycir.add_gate( q1, cnot )
print( mycir.export() )

mycir.visualize()
res_state = mycir.execute_circuit()

res_state.evaluate_results()

print( res_state.nqubits )
print( res_state.get_results() )
res_state.plot_results()
