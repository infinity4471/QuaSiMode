from state import state
from quantum_operator import operator
import numpy as np
from math import sqrt

#Test application

cur = state( np.array( [ 0, 1 ] ) )
op = operator( np.array( [ [ 1.0, 0.0], [ 0.0, 1.0 ] ] ) )
cur.apply_operator( op )
print( cur.get_state() )

op.apply( operator( np.array( [ [ 1/sqrt(2), 1/sqrt(2) ], [ 1/sqrt( 2 ), -1/sqrt(2) ] ] ) ) )
cur.apply_operator( op )

print( cur.get_state() )
cur.add_state( state( np.array( [ 0, 1 ] ) ) )
print( cur.get_state() )
cur.add_state( state( np.array( [ 1/sqrt(2), 1/sqrt(2) ] ) ) )
print( cur.measure() )
print( cur.evaluate_results() )
cur.plot_results()