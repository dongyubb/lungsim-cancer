import sympy as sp
from sympy import exp, sqrt
import numpy as np
import os
import math

def solve_volume_from_cc(cc_dir):
# def read_cc_solve_v(cc_dir):
#     cc_dir = '/home/ydon868/Desktop/VentilationStudy/lung030/baseline_cropped/Healthy/Output/unit_cc.txt'
    v_dir = os.path.join(os.path.dirname(cc_dir),'unit_v.txt')
    cc_array = np.loadtxt(cc_dir)
    y , x= sp.symbols('y x', positive=True, real=True)
    #print(len(cc_array))
    v_array = np.zeros(len(cc_array))
    for i in range(len(cc_array)):
        equation = cc_array[i] * exp(0.75*0.688*((x**2-1)**2))*0.688*(x**2-1)/2.0/x - 500
        v = sp.nsolve(equation, x, (1,10),solver='bisect',verify=False)
        v = v**3
        #print('solving unit volume ', i)
        v_array[i] = v
    np.savetxt(v_dir,v_array,newline='\n')
    return v_dir
