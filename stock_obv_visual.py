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

def stock_obv_visual(company, start_year, start_month, start_day, end_year, end_month, end_day):
    a = int(start_year)
    b = int(start_month)
    c = int(start_day)
    d = int(end_year)
    e = int(end_month)
    f = int(end_day)

    # Error: same start and end date
    if ((a == d) and (b == e) and (c == f)):
        print("The start and end dates must be different")
        sys.exit()

    # Error: the months exist out of range
    if ((b < 1 or b > 12) or (e < 1 or e > 12)):
        print("Month out of range")
        sys.exit()

    # Error: days are out of range for non-leap years and regular months
    if ((c < 1) or (f < 1) or (c > 31) or (f > 31) or ( (b == 2 or e == 2) and (c > 28 or f > 28) and (a % 4 != 0 or d % 4 != 0 ) ) ):
        print("Day out of range")
        sys.exit()

    # Error: day out of range for leap year
    if ((b == 2 or e == 2) and (c > 29 or f > 29) and (a % 4 == 0 or d % 4 == 0)):
        print("Day out of range")
        sys.exit()

    # Error: handle months with 31 days
    if ((b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12 or
         e == 1 or e == 3 or e == 5 or e == 7 or e == 8 or e == 10 or e == 12 ) and (c > 31)):
        print("Day out of range")
        sys.exit()

    # Error: handle months with 30 days
    if ((b == 4 or b == 6 or b == 9 or b == 11 or e == 4 or e == 6 or e == 9 or e == 11 ) and (c > 30)):
        print("Day out of range")
        sys.exit()

    # Error: start date later than end date
    if ( (a > d) or (a == d and ( (b > e) or ( (b == e and c > f) ) ) ) ):
        print ("Start date must be earlier than end date")
        sys.exit()

    # Obtaining data from the Yahoo Finance Website
    # style.use('ggplot')
    temp = pdr.get_data_yahoo(company, start =  datetime(a, b, c), end = datetime(d, e, f))
    # print(temp)
    temp.reset_index(inplace = True)
    temp.set_index("Date", inplace = True)

    # Plotting the Close Price
    plt.figure(figsize = (20, 6))
    plt.subplot(131)
    plt.plot(temp['Close'])
    plt.title('Price History Over Time')
    plt.ylabel('Share Price in USD')
    plt.xlabel('Date')

    # Plotting the Volume
    plt.subplot(132)
    plt.plot(temp['Volume']/1000000)
    plt.title('Trade Volumes Over Time')
    plt.ylabel('Trade Volumes in Millions')
    plt.xlabel('Date')
    plt.show(block = False)
    # return temp.tail(20)

#print(stock_obv_visual('TSLA', 2019, 6, 7, 2020, 8, 12))