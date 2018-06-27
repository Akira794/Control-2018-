#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np              # Numerical library
from scipy import *             # Load the scipy functions
from control.matlab import *    # Load the controls systems library
from matplotlib import pyplot as plt
from scipy import arange
import CtrbObsvCheck as ck
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

  D = None

  sys = ss(A, B, C, 0);

#可観測性の判定
  if ck.check_obsv(sys.A, sys.C) == -1:
      print("Not Observability\n")
      exit
  P = [-3,-4]
  L = place(sys.A.T,sys.C.T,P).T

  amp = 1.0
  freq = 1.0

  x = np.array([[1],[1]])
  xh = np.array([[0],[0]])

  yh = 0
  dt = 0.1
  x1 = []
  x2 = []
  xh1 = []
  xh2 = []
  time  = []

  for n in drange(0.0, 10.0, dt):
      u = np.sign(amp*np.sin(2*np.pi*freq*n))
      dx = sys.A * x + sys.B * u
      x  = x + dx * dt
      y  = sys.C * x

      x1.append(float(x[0]))
      x2.append(float(x[1]))

      dxh = sys.A * xh + sys.B * u - L*(yh - y)
      xh  = xh + dxh * dt
      yh  = sys.C * xh

      xh1.append(float(xh[0]))
      xh2.append(float(xh[1]))

      time.append(n)

  plt.plot(time, x1,label="$X_1 pos$")
  plt.plot(time, x2,label="$X_2 vel$")
  plt.plot(time, xh1,label="$Xh_1 pos$")
  plt.plot(time, xh2,label="$Xh_2 vel$")
  plt.grid(which='major',color='gray',linestyle='-')
  plt.legend()
  plt.show()

if __name__ == "__main__":
  main()
