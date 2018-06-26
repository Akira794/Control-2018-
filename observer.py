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

L = place(A.T, C.T,[-3, -4]).T

print("Observer_Gain:\n",L)
