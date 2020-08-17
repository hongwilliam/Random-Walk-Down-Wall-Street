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


#uses period of last 14 trading days
#returns value between 0-100
#value > 80: overbought, value < 20: oversold
#generally the higher the value, the more overbought it is
def compute_stochastic_oscillator(company, year, month, day):
    a = int(year)
    b = int(month)
    c = int(day)


    # Error: the months exist out of range
    if (b < 1 or b > 12):
        print("Month out of range")
        sys.exit()

    # Error: days are out of range for non-leap years and regular months
    if ((c < 1) or (c > 31) or ( b == 2 and c > 28  and a % 4 != 0 ) ):
        print("Day out of range")
        sys.exit()

    # Error: day out of range for leap year
    if ((b == 2) and (c > 29) and (a % 4 == 0)):
        print("Day out of range")
        sys.exit()

    # Error: handle months with 31 days
    if ((b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12) and (c > 31)):
        print("Day out of range")
        sys.exit()

    # Error: handle months with 30 days
    if ((b == 4 or b == 6 or b == 9 or b == 11 ) and (c > 30)):
        print("Day out of range")
        sys.exit()

    d = a
    e = b-1
    f = c
    if (b == 1):
        d -= 1
        e = 12

    temp = pdr.get_data_yahoo(symbols = company, start =  datetime(d, e, f), end = datetime(a, b, c))
    comp_list = []
    x = 0
    while (x < len(temp)):
        entry = temp['Close'][x]
        entry = round(entry, 2)
        comp_list.append(entry)
        x += 1

    while (len(comp_list) > 14):
        comp_list.pop(0)

    low = np.min(comp_list)
    high = np.max(comp_list)
    closing = comp_list[13]
    answer = ( (closing - low)/(high - low) ) * 100
    answer = round(answer, 2)
    x = str(answer) + "%"
    print(x)
    return answer