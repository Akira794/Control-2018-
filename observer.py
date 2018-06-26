#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np              # Numerical library
from scipy import *             # Load the scipy functions
from control.matlab import *    # Load the controls systems library
from matplotlib import pyplot as plt
from scipy import arange
import CtrbObsvCheck as ck
from scipy.linalg import expm

# System matrices
A = matrix([[0, 1],
            [-5, -6]])
B = matrix([[0],
            [1]])

C = matrix([[1, 0]])

sys = ss(A, B, C, 0);

if ck.check_obsv(sys.A, sys.C) == -1:
     print("Not Observability\n")
     exit

f = place(A.T, C.T,[-3, -4]).T

print("Observer_Gain:\n",f)

sys_fb = ss(sys.A - sys.B *f, sys.B, sys.C, sys.D)

N = 1024
x0 = [1.0, 0.0]
t = np.linspace(0, 7, 1024)
u = np.zeros(N)

out, t_b, x_b = lsim(sys, U=u, T=t, X0=x0)
out_fb, t_fb, x_fb = lsim(sys_fb, U=u, T=t, X0=x0)
plt.plot(t_fb, out_fb[:,1], label="output")
plt.plot(t_b, x_b[:,0], label="$X_1$")
plt.plot(t_b, x_b[:,1], label="$X_2$")
plt.plot(t_fb, x_fb[:,0], label="$X_1 feed back$")
plt.plot(t_fb, x_fb[:,1], label="$X_2 feed back$")
plt.legend()
plt.show()
