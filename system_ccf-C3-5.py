#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 対角正準形  #出力がおかしい
import numpy as np              # Numerical library
from scipy import *             # Load the scipy functions
from control.matlab import *    # Load the controls systems library
from matplotlib import pyplot as plt
from scipy import arange
import CtrbObsvCheck as ck
from scipy.linalg import expm
#from control import canonical_form
import canonical as cc
# 参照 http://python-control.readthedocs.io/en/latest/generated/control.canonical_form.html
sys = ss([[0, 1, 1],
          [-2, -3, 1],
          [0, 0, -3]],
         [[1],
          [1],
          [1]],
         [[1, 0, 1]], 0)

Mc = ctrb(sys.A, sys.B)

sys_c, Tc = cc.observable_form(sys)
print(sys_c, Tc)
