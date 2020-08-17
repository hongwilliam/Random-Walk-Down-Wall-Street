import cgitb
cgitb.enable()
import numpy as np
import pandas as pd
import scipy.stats
import pandas_datareader as pdr
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import sys
from numpy.polynomial import Polynomial as P
import numpy.linalg as la

def data_discrete(x_values,y_values,n):
    coeficients=[]
    b_matrix=np.ndarray(shape = (n+1, n+1), dtype = 'float')
    c_matrix=np.ndarray(shape = (n+1, 1), dtype = 'float')
    i = 0
    while i <=n:
        j = 0
        c_value=0
        while j <=n:
            b_value = 0
            for m in range(len(x_values)):
                b_value +=(x_values[m])**(i+j)
            b_matrix[i][j]= b_value
            j+=1
        for a in range(len(y_values)):
            c_value += (x_values[a])**i *y_values[a]
        c_matrix[i][0]=c_value
        i+=1
    #print(b_matrix)
    #print(c_matrix)
    a_values = la.solve(b_matrix,c_matrix)
    for p in range (len(a_values)):
        coeficients.append(a_values[p][0])
    p_f = P(coeficients)
    return p_f