#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np              # Numerical library
from scipy import *             # Load the scipy functions
from control.matlab import *    # Load the controls systems library
from matplotlib import pyplot as plt
from scipy import arange
import CtrbObsvCheck as ck

def main():

    A = matrix([[0, 0], [-5, -6]])
    B = matrix([[0], [1]])
    C = matrix([[1, 0]])
    sys = ss(A, B, C, 0)

    if ck.check_ctrb(A, B) == -1:
        print("System not Controllability\n")
        return 0
    if ck.check_obsv(A, C) == -1:
        print("System not Observability\n")
        return 0

    Uc = ctrb(A, B)
    Uo = obsv(A, C)

    print("Uc = \n", Uc)
    print("Uo = \n", Uo)

if __name__ == '__main__':
    main()
