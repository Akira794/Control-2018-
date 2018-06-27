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



  sys = ss(A, B, C, 0);

  amp = 1.0
  freq = 0.8
  x = np.array([[1],
                [0]])
  u = 1
  dt = 0.1
  x1 = []
  x2 = []
  time  = []

#  print(sys.A * x)
#  print(sys.B * u)

  for n in drange(0.0, 10.0, dt):
      u = np.sign(amp*np.sin(2*np.pi*freq*n))
      dx = sys.A * x + sys.B * u
      x  = x + dx * dt

      x1.append(float(x[0]))
      x2.append(float(x[1]))
      time.append(n)

  plt.plot(time, x1, time, x2)
  plt.grid(which='major',color='gray',linestyle='-')
  plt.show()
if __name__ == "__main__":
  main()
