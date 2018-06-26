#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np              # Numerical library
from scipy import *             # Load the scipy functions
from control.matlab import *    # Load the controls systems library
from matplotlib import pyplot as plt
from scipy import arange
import CtrbObsvCheck as ck
from scipy.linalg import expm

def main():
  # system
  A = np.array([[0, 1],
                [-5, -6]])
  B = np.array([[0],
                [1]])

  C = np.array([[1, 0]])

  Q1 = np.array([[1, 0],
                [0, 1]])

  Q2 = np.array([[1000, 0],
                 [0, 1000]])

  R = np.array([[1]])
  D = None

  x0 = np.array([[1, 0]])

  sys = ss(A, B, C, 0);

#可制御性　可観測性の判定
  if ck.check_ctrb(A, B) and ck.check_obsv(A, C) == -1:
      print("Not Controllability and Observability\n")
      exit

  # calc lqr
  K1, P1, e1 = lqr(sys.A, sys.B, Q1, R)
  K2, P2, e2 = lqr(sys.A, sys.B, Q2, R)
  # result
  print("リカッチ方程式の解:\n", P1)
  print("状態フィードバックゲイン:\n", K1)
  print("閉ループ系の固有値:\n", e1)

  sys_fb1 = ss(sys.A - sys.B * K1, sys.B, sys.C, sys.D)
  sys_fb2 = ss(sys.A - sys.B * K2, sys.B, sys.C, sys.D)
  N = 1024
  x0 = [1.0, 0.0]
  t = np.linspace(0, 7, 1024)
  u = np.zeros(N)

  out, t_b, x_b = lsim(sys_fb1, U=u, T=t, X0=x0)
  out_fb, t_fb, x_fb = lsim(sys_fb2, U=u, T=t, X0=x0)
  #plt.plot(t_fb, out_fb[:,0], label="output")# 出力
  plt.plot(t_b, x_b[:,0], label="$X_1 normal$")
  plt.plot(t_b, x_b[:,1], label="$X_2 normal$")
  plt.plot(t_fb, x_fb[:,0], label="$X_1 pos vel up$")
  plt.plot(t_fb, x_fb[:,1], label="$X_2 pos vel up$")
  plt.legend()
  plt.show()

if __name__ == "__main__":
  main()
