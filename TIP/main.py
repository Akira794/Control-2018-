#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 台車型倒立振子の最適レギュレータ設計

import numpy as np              # Numerical library
from scipy import *             # Load the scipy functions
from control.matlab import *    # Load the controls systems library
from matplotlib import pyplot as plt
import sysmodel as tip
import CtrbObsvCheck as ck
from scipy.linalg import expm


def drange(begin, end, step):
    n = begin
    while n + step < end:
        yield n
        n += step


def main():
    sys = tip.system()

    if ck.check_obsv(sys.A, sys.C) == -1:
        print("Not Observability\n")
        exit

    Q = np.matrix([[1000, 0, 0, 0], [0, 1, 0, 0], [0, 0, 100, 0], [0, 0, 0, 100]])
    R = 1

    F, P, e = lqr(sys.A, sys.B, Q, R)
    L = place(sys.A.T, sys.C.T, e).T

    print("\nObserver_Gain L:\n", L)
    print("\nFeedback_Gain F:\n", F)
    print("\n")

    x = np.matrix([[0.1], [0.1], [0.1], [0.1]])
    xh = np.matrix([[0], [0], [0], [0]])
    xb0 = np.r_[x, xh]

    #併合系
    bf = sys.B * F
    lc = L * sys.C
    A1 = np.c_[sys.A, -bf]
    A2 = np.c_[lc, sys.A - bf - lc]
    Ab = np.r_[A1, A2]


    dt = 0.01
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    xh1 = []
    xh2 = []
    xh3 = []
    xh4 = []
    time = []

    for n in drange(0.0, 10.0, dt):

        xb = expm(Ab * n) * xb0
        x1.append(float(xb[0]))
        x2.append(float(xb[1]))
        x3.append(float(xb[2]))
        x4.append(float(xb[3]))
        xh1.append(float(xb[4]))
        xh2.append(float(xb[5]))
        xh3.append(float(xb[6]))
        xh4.append(float(xb[7]))
        time.append(n)

    plt.plot(time, x1,label="$X_1 pos$")
    plt.plot(time, x2,label="$X_2 vel$")
    plt.plot(time, x3,label="$X_3 rad$")
    plt.plot(time, x4,label="$X_4 omega$")
    plt.plot(time, xh1,label="$Xh_1 pos$")
    plt.plot(time, xh2,label="$Xh_2 vel$")
    plt.plot(time, xh3,label="$Xh_3 rad$")
    plt.plot(time, xh4,label="$Xh_4 omega$")
    plt.grid(which='major',color='gray',linestyle='-')
    plt.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=0, fontsize=10)
    plt.show()

if __name__ == '__main__':
    main()
