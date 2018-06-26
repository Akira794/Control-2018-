#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np              # Numerical library
from scipy import *             # Load the scipy functions
from control.matlab import *    # Load the controls systems library
from matplotlib import pyplot as plt
from scipy import arange


def main():
    A = matrix([[0, 1], [-5, -6]])
    B = matrix([[0], [1]])
    C = matrix([[1, 0]])
    sys = ss(A, B, C, 0);
    x0 = [[1],[0]]

    (y1a, T1a) = step(sys, T=arange(0, 10, 0.01), X0 = x0)
    plt.axhline(1, color="g", linestyle="--")
    plt.plot(T1a, y1a)
    plt.show()

if __name__ == "__main__":
    main()
