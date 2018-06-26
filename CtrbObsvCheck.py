import numpy as np              # Numerical library
from scipy import *             # Load the scipy functions
from control.matlab import *    # Load the controls systems library
from matplotlib import pyplot as plt

def check_ctrb(A, B):
    a = np.mat(A)
    Uc = ctrb(A, B)
    if np.linalg.matrix_rank(Uc) != a.shape[0]:
        return -1 #System not Controllability
    else :
        return 0 #System Controllability

def check_obsv(A, C):
    a = np.mat(A)
    Uo = obsv(A,C)
    if np.linalg.matrix_rank(Uo) != a.shape[0]:
        return -1#System not Observability
    else :
        return 0#System Observability
