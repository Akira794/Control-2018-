#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np              # Numerical library
from scipy import *             # Load the scipy functions
from control.matlab import *    # Load the controls systems library
from matplotlib import pyplot as plt
#from control import acker

# System matrices
A = matrix([[0, 1], [-5, -6]])
B = matrix([[0], [1]])
C = matrix([[1, 0]])
sys = ss(A, B, C, 0);

print(sys)
# Controllability
Uc = ctrb(A, B)
a = np.mat(A)
print("Uc = ", Uc)
if np.linalg.matrix_rank(Uc) != a.shape[0]:#行列Aの行数 shape[1]は行列Aの列数
   print ("System not Controllability\n")
else :
   print ("System Controllability\n")


# Eigenvalue placement
#from slycot import sb01bd
K = place(A, B, [-2, -3])
#K = acker(A, B, [-2, -3])
print ("Pole place: K = ", K)
print ("Pole place: eigs = ", np.linalg.eig(A - B * K)[0])

#impulse respo
sys_fb = ss(sys.A-sys.B*K, sys.B, sys.C, sys.D)
out_fb, t_fb =  impulse(sys_fb, T = arange(0, 10, 0.01))
plt.plot(t_fb, out_fb)
plt.ylim([-1,1])
plt.grid()
plt.show()
