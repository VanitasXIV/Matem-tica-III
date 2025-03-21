# 1. Relizar la transformación lineal de *v* = [1, 2] 
# si *î* = [2, 0] y *j* = [0, 3/2]

import numpy as np

A = np.array([[2,0],
             [0,3/2]])

v = np.array([1,2])

v_trans = np.dot(A,v)

print("The new vector is: ", v_trans)