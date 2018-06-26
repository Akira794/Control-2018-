#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np              # Numerical library
from scipy import *             # Load the scipy functions
from control.matlab import *    # Load the controls systems library
from matplotlib import pyplot as plt
from scipy import arange
from scipy.linalg import expm

def drange(begin, end, step):
    n = begin
    while n + step < end:
     yield n
     n += step

def main():
  # system
  A = np.array([[0, 1],
                [-5, -6]])
  B = np.array([[0],
                [1]])

  C = np.array([[1, 0]])

  x0 = np.array([[1, 0]])

  sys = ss(A, B, C, 0);


  i = 0
  x1 = []
  x2 = []
  time  = []

  for n in drange(0.0, 6.0, 0.1):
      i = i + 1
      x = expm(sys.A * n) * x0
      x1.append(x[0][0])
      x2.append(x[1][0])
      time.append(n)
  plt.plot(time, x1, time, x2)

  plt.grid(which='major',color='gray',linestyle='-')
  plt.show()

if __name__ == "__main__":
  main()
