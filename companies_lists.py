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

# Numerical Analysis Graphs with Polynomial Functions
def companies_lists(company_1, company_2, start_year, start_month, start_day, end_year, end_month, end_day):
    a = int(start_year)
    b = int(start_month)
    c = int(start_day)
    d = int(end_year)
    e = int(end_month)
    f = int(end_day)
    temp_1 = pdr.get_data_yahoo(symbols = company_1, start =  datetime(a, b, c), end = datetime(d, e, f))
    temp_2 = pdr.get_data_yahoo(symbols = company_2, start =  datetime(a, b, c), end = datetime(d, e, f))
    comp1_list = []
    comp2_list = []
    x = 0
    while (x < len(temp_1)):
        entry = temp_1['Close'][x]
        entry = round(entry, 2)
        comp1_list.append(entry)
        x += 1

    y = 0
    while (y < len(temp_2)):
        entry = temp_2['Close'][y]
        entry = round(entry, 2)
        comp2_list.append(entry)
        y += 1

    comp1_list = pd.Series(comp1_list)
    comp2_list = pd.Series(comp2_list)
    return comp1_list,comp2_list