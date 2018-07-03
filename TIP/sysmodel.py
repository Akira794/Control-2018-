#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 台車型倒立振子の最適レギュレータ設計

import numpy as np              # Numerical library
from scipy import *             # Load the scipy functions
from control.matlab import *    # Load the controls systems library

def system():
# system parameters
    M = 0.3  # 台車の質量 kg
    m = 0.2  # 振子の質量 kg
    l = 0.3  # 振子長の2分の1 m
    J = 1/12 * m * l**2  # 振子の慣性モーメント kg・m^2
    g = 9.81  # 重力加速度 m/s^2

    alp = (M + m) * (J + m * l**2) - (m * l)**2

    A = np.matrix([[0, 0, 1, 0],
                [0, 0, 0, 1],
                [0, -(((m * l)**2 * g) / alp), 0, 0],
                [0, ((M + m) * m * g * l) / alp, 0, 0]])

    B = np.matrix([[0],
                 [0],
                 [(J + m * (l**2)) / alp],
                 [-(m * l) / alp]])

    C = np.matrix([[1, 0, 0, 1]])

    D = 0

    x0 = np.array([[0.1], [0.1], [0.1], [0.1]])
    xh = np.array([[0], [0], [0], [0]])

    sys = ss(A,B,C,D)

    return sys

def main():
    sys = system()
    print(sys)

if __name__ == '__main__':
    main()
