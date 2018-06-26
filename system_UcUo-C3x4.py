#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np              # Numerical library
from scipy import *             # Load the scipy functions
from control.matlab import *    # Load the controls systems library
from matplotlib import pyplot as plt
from scipy import arange

# System matrices
A = matrix([[0, 1], [-5, -6]])
B = matrix([[0], [1]])
C = matrix([[1, 0]])
sys = ss(A, B, C, 0);

print("system =\n", sys)

#controllability
Uc = ctrb(A,B)
a  = np.mat(A)
print("Uc = ", Uc)
if np.linalg.matrix_rank(Uc) != a.shape[0]:
    print("System not Controllability\n")
else :
    print("System Controllability")

#Observability
Uo = obsv(A,C)
print("Uo = ", Uo)
if np.linalg.matrix_rank(Uo) != a.shape[0]:
    print("System not Observability\n")
else :
    print("System Observability")
