#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np              # Numerical library
from scipy import *             # Load the scipy functions
from control.matlab import *    # Load the controls systems library
from matplotlib import pyplot as plt

# System matrices
A = matrix([[0, 1], [-5, -6]])
B = matrix([[0], [1]])
C = matrix([[1, 0]])
sys = ss(A, B, C, 0);

N = 1024
x0 = [1.0, 0.1]
t = np.linspace(0, 4, 1024)
u = np.zeros(N)

out_fb, t_fb, x_fb = lsim(sys, U=u, T=t, X0=x0)
#    plt.plot(t_fb, out_fb[:,1], label="output")
plt.plot(t_fb, x_fb[:,0], label="$X_1$")
plt.plot(t_fb, x_fb[:,1], label="$X_2$")
plt.legend()
plt.show()
