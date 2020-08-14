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

#DEVELOPER INSTRUCTIONS

#(1) MAKE SURE TO INSTALL THIS PACKAGE IN THE TERMINAL USING THE COMMANDS:
#pip install pandas-datareader

#(2) go on terminal in the directory this file is in

#(3) type in the command line
#python random_walk.py

#(4) enter in instrctions when prompted in the terminal


#PART 1: testing basic stat functions

#mean
list_1 = np.array([1, 2, 3, 4, 5])
#print(np.mean(list_1)) #should return 3

#2D arrays
list_2 = np.array([ [1, 2, 3], [4, 5, 6] ]) #list of lists
#print(np.mean(list_2)) #should return 3.5
#print(np.mean(list_2[0])) #should return mean of first list, which is 2

#should return mean of 1 and 4, 2 and 5, 3 and 6... which is [2.5 3.5 4.5]
#print(np.mean(list_2, axis = 0))

#should return mean of 1,2,3 and 4,5,6... which is [2. 5.]
#print(np.mean(list_2, axis = 1))

#standard deviation
list_3 = np.array([1, 2, 3, 4])
#print(np.std(list_3)) #should return 1.118 ish


#PART 2: testing the correlation coefficient function
# > 0 is positively correlated, 0 is uncorrelated, < 0 is negatively
# range of correlation is [-1, 1]
# ORDER OF INPUTS DOES NOT MATTER FOR CORRELATION COEFFICIENT

#perfect linear negative correlation
list_4 = [0, 1, 2]
list_5 = [2, 1, 0]
list_4 = pd.Series(list_4)
list_5 = pd.Series(list_5)
#print(list_4.corr(list_5)) #should return -1

#perfect linear positive correlation
list_6 = [0, 1, 2]
list_7 = [1, 2, 3]
list_6 = pd.Series(list_6)
list_7 = pd.Series(list_7)
#print(list_6.corr(list_7)) #should return 1


#PART 3: retrieving csv files from online and storing into list
COST = pdr.get_data_yahoo(symbols = 'COST', start =  datetime(2010, 7, 14), end = datetime(2020, 7, 14))
#print(round(COST['Close'][0], 2)) #Costco's close at 7/14/2010 was $56.35

COST_list = []
x = 0
while (x < len(COST)):
    entry = COST['Close'][x]
    entry = round(entry, 2)
    COST_list.append(entry)
    x += 1
#print(COST_list)

# Correlation Analysis
def compute_correlation_companies(company_1, company_2, start_year, start_month, start_day, end_year, end_month, end_day):
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

    if ( (a > d) or (a == d and ( (b > e) or ( (b == e and c > f) ) ) ) ):
        print ("Start date must be earlier than end date")
        sys.exit()


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
    return round(comp1_list.corr(comp2_list), 2)

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

def compute_volatility(company, start_year, start_month, start_day, end_year, end_month, end_day):
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

    temp = pdr.get_data_yahoo(symbols = company, start =  datetime(a, b, c), end = datetime(d, e, f))
    comp_list = []
    x = 0
    while (x < len(temp)):
        entry = temp['Close'][x]
        entry = round(entry, 2)
        comp_list.append(entry)
        x += 1

    average = "The average for this data point is: "
    average += str(round(np.mean(comp_list), 2))
    print(average)

    standard_deviation = "The standard deviation for this data point is: "
    standard_deviation += str(round(np.std(comp_list), 2)) + "\n"
    print (standard_deviation)

    return round(np.std(comp_list), 2)

def compute_average_daily_price_change(company, start_year, start_month, start_day, end_year, end_month, end_day):
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

    if ( (a > d) or (a == d and ( (b > e) or ( (b == e and c > f) ) ) ) ):
        print ("Start date must be earlier than end date")
        sys.exit()

    temp = pdr.get_data_yahoo(symbols = company, start =  datetime(a, b, c), end = datetime(d, e, f))
    change_sum = 0
    x = 0
    while (x < (len(temp)-1)):
        entry_1 = temp['Close'][x]
        entry_1 = round(entry_1, 2)
        entry_2 = temp['Close'][x+1]
        entry_2 = round(entry_2, 2)
        answer = ((entry_2 - entry_1)/(entry_1)) * 100
        change_sum += answer
        x += 1

    y = round((change_sum/(len(temp)-1)), 2)
    y = str(y) + "%"
    print(y)
    #answer is given as %
    return y

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

def compute_exponential_moving_average(company, start_year, start_month, start_day, end_year, end_month, end_day):
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

        temp = pdr.get_data_yahoo(symbols = company, start =  datetime(a, b, c), end = datetime(d, e, f))
        comp_list = []
        x = 0
        while (x < len(temp)):
            entry = temp['Close'][x]
            entry = round(entry, 2)
            comp_list.append(entry)
            x += 1

        comp_list = pd.Series(comp_list)
        comp_list = comp_list.ewm(span = x, adjust=False).mean()
        x -= 1
        answer = round(comp_list[x], 2)

        return answer
# print(compute_exponential_moving_average('TSLA', 2015, 6, 7, 2020, 8, 12))

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
    plt.plot(temp['Close'])
    plt.title('Price History Over Time')
    plt.ylabel('Share Price in USD')
    plt.xlabel('Date')
    plt.show(block = False)

    # Plotting the Volume
    plt.figure(figsize = (20, 6))
    plt.plot(temp['Volume']/1000000)
    plt.title('Trade Volumes Over Time')
    plt.ylabel('Trade Volumes in Millions')
    plt.xlabel('Date')
    plt.show(block = False)
    # return temp.tail(20)

#print(stock_obv_visual('TSLA', 2019, 6, 7, 2020, 8, 12))

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



#PART 4: entering command line input to get analysis
#THIS IS THE COOL SHIT
print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers you can enter \nEnter in 3 to get graphing capabilities\nEnter in 4 to exit the program")
while True:
    selection = input("Enter option here: ")
    if selection == '1':
        print("________________________________________________________________________________")
        print("Instructions: \nEnter in 1 to compute correlation coefficient between two data points \nEnter in 2 to compute volatility \nEnter in 3 to compute stochastic oscillator\nEnter in 4 to compute average daily percent change\nEnter in 5 to compute exponential moving average\nEnter in 6 to do polynomial approximations")
        next_selection = input("Enter option here: ")
        if next_selection == '1':
            enter_company_1 = input("Enter a ticker here: ")
            enter_company_2 = input("Enter another ticker here: ")
            enter_start = input("Enter start date of analysis as Year, Month, Day (ex: 2010, 8, 12): ")
            enter_end = input("Enter end date of analysis as Year, Month, Day (ex: 2020, 8, 12): ")
            start_list = enter_start.split(", ")
            end_list = enter_end.split(", ")

            print("Here is the correlaton coefficient between %s and %s: " %(enter_company_1, enter_company_2))
            print(compute_correlation_companies(enter_company_1, enter_company_2,
            start_list[0], start_list[1], start_list[2], end_list[0], end_list[1], end_list[2] ))

            print("________________________________________________________________________________")
            print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers you can enter \nEnter in 3 to get graphing capabilities\nEnter in 4 to exit the program")

        if next_selection == '2':
            enter_company = input("Enter a ticker here: ")
            enter_start = input("Enter start date of analysis as Year, Month, Day (ex: 2010, 8, 12): ")
            enter_end = input("Enter end date of analysis as Year, Month, Day (ex: 2020, 8, 12): ")
            start_list = enter_start.split(", ")
            end_list = enter_end.split(", ")
            print("Here is the volatility analysis for %s: " %enter_company)
            compute_volatility(enter_company, start_list[0], start_list[1], start_list[2], end_list[0], end_list[1], end_list[2])
            print("________________________________________________________________________________")
            print("\n")
            print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers you can enter \nEnter in 3 to get graphing capabilities\nEnter in 4 to exit the program")

        if next_selection == '3':
            enter_company = input("Enter a ticker here: ")
            enter_date = input("Enter in today's date (ex: 2020, 8, 12): ")
            date_list = enter_date.split(", ")
            print("Here is the stochastic oscillator for %s: " %enter_company)
            compute_stochastic_oscillator(enter_company, date_list[0], date_list[1], date_list[2])
            print("________________________________________________________________________________")
            print("\n")
            print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers you can enter \nEnter in 3 to get graphing capabilities\nEnter in 4 to exit the program")

        if next_selection == '4':
            enter_company = input("Enter a ticker here: ")
            enter_start = input("Enter start date of analysis as Year, Month, Day (ex: 2010, 8, 12): ")
            enter_end = input("Enter end date of analysis as Year, Month, Day (ex: 2020, 8, 12): ")
            start_list = enter_start.split(", ")
            end_list = enter_end.split(", ")

            print("Here is the average daily percent change for %s " %enter_company)
            compute_average_daily_price_change(enter_company,start_list[0], start_list[1], start_list[2], end_list[0], end_list[1], end_list[2])
            print("________________________________________________________________________________")
            print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers you can enter \nEnter in 3 to get graphing capabilities\nEnter in 4 to exit the program")

        if next_selection == '5':
            enter_company = input("Enter a ticker here: ")
            enter_start = input("Enter start date of analysis as Year, Month, Day (ex: 2010, 8, 12): ")
            enter_end = input("Enter end date of analysis as Year, Month, Day (ex: 2020, 8, 12): ")
            start_list = enter_start.split(", ")
            end_list = enter_end.split(", ")

            print("Here is the exponential moving average for %s " %enter_company)
            print(compute_exponential_moving_average(enter_company,start_list[0], start_list[1], start_list[2], end_list[0], end_list[1], end_list[2]))

        if next_selection == '6':
            enter_company_1 = input("Enter a ticker here: ")
            enter_company_2 = input("Enter another ticker here: ")
            enter_start = input("Enter start date of analysis as Year, Month, Day (ex: 2010, 8, 12): ")
            enter_end = input("Enter end date of analysis as Year, Month, Day (ex: 2020, 8, 12): ")
            #FOR FARHAN
            #enter_n_degree = input("Enter the degree you want your polynomial as: ")
            # ^ you can use enter_n_degree as an int now
            start_list = enter_start.split(", ")
            end_list = enter_end.split(", ")
            comlist1, comlist2 = companies_lists(enter_company_1, enter_company_2, start_list[0], start_list[1], start_list[2], end_list[0], end_list[1], end_list[2] )
            i = 1
            print("Here is the n degree ")
            while i <=10:##graphing the first 10 degree polynomials
                print(f"Degree {i} polynomial:")
                x = np.arange(0, 1000, 0.001)
                y = data_discrete(comlist1,comlist2,i)(x) # Python distinguish lower and upper cases.
                line = plt.plot(x, y, lw = 1)
                #plt.annotate('f(x)', xy = (0, 1), xytext = (2, 1),
                #arrowprops = dict(facecolor = 'black', shrink = 0.01))
                plt.ylim(0, 10000)
                plt.show()
                i+=1



        if next_selection != '1' and next_selection != '2' and next_selection != '3' and next_selection != '4' and next_selection != '5' and next_selection != '6':
            print("Incorrect input entered\n")
            print("________________________________________________________________________________")
            print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers you can enter \nEnter in 3 to get graphing capabilities\nEnter in 4 to exit the program")

    if selection == '2':
        print("________________________________________________________________________________")
        print("Instructions: \nEnter in 1 to get a list of relevant market indexes \nEnter in 2 to get a list of US market sectors \nEnter in 3 to get a list of commodities and currencies")
        next_selection = input("Enter option here: ")
        if next_selection == '1':
            print("________________________________________________________________________________")
            a = "\nBelow are some tickers you can enter that track market indexes\n"
            b = "S&P 500: ^GSPC\n"
            c = "Dow Jones Industrial Average: ^DJI\n"
            d = "NASDAQ Composite: ^IXIC\n"
            e = "Russell 2000: ^RUT \n"
            f = "FTSE 100: %5EFTSE%3FP%3DFTSE\n"
            g = "Nikkei 225: ^N225\n"
            h = "VIX Volatility Index: ^VIX\n"
            print(a+b+c+d+e+f+g+h)
            print("________________________________________________________________________________")
            print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers you can enter \nEnter in 3 to get graphing capabilities\nEnter in 4 to exit the program")
        if next_selection == '2':
            print("________________________________________________________________________________")
            a = "\nBelow are some tickers you can enter that represent market sectors\n"
            b = "Communication Services: XLC\n"
            c = "Consumer Discretionary: XLY\n"
            d = "Consumer Staples: XLP\n"
            e = "Energy: XLE\n"
            f = "Financials: XLF\n"
            g = "Health: XLV\n"
            h = "Industrials: XLI\n"
            i = "Materials: XLB\n"
            j = "Real Estate: XLRE\n"
            k = "Technology: XLK\n"
            l = "Utilities: XLU\n"
            print(a+b+c+d+e+f+g+h+i+j+k+l)
            print("________________________________________________________________________________")
            print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers you can enter \nEnter in 3 to get graphing capabilities\nEnter in 4 to exit the program")
        if next_selection == '3':
            print("________________________________________________________________________________")
            a = "\nBelow are some tickers you can enter that track commodities and currencies\n"
            b = "US Treasury 10 Year Bond: ^TNX\n"
            c = "Crude Oil: CL=F\n"
            d = "Gold: GC=F\n"
            e = "Silver: SI=F\n"
            f = "Bitcoin: BTC-USD\n"
            g = "US Dollar/Euro Exchange Rate: USDEUR=X\n"
            h = "US Dollar/Yen Exchage Rate: JPY=X\n"
            print(a+b+c+d+e+f+g+h)
            print("________________________________________________________________________________")
            print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers you can enter \nEnter in 3 to get graphing capabilities\nEnter in 4 to exit the program")
        if next_selection != '1' and next_selection != '2' and next_selection != '3':
            print("Incorrect input entered\n")
            print("________________________________________________________________________________")
            print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers you can enter \nEnter in 3 to get graphing capabilities\nEnter in 4 to exit the program")


    if selection == '3':
        print("________________________________________________________________________________")
        enter_company = input("Enter a ticker here: ")
        enter_start = input("Enter start date of analysis as Year, Month, Day (ex: 2010, 8, 12): ")
        enter_end = input("Enter end date of analysis as Year, Month, Day (ex: 2020, 8, 12): ")
        start_list = enter_start.split(", ")
        end_list = enter_end.split(", ")
        print("Here is the price over time and volume over time for %s: " %enter_company)
        print(stock_obv_visual(enter_company,start_list[0], start_list[1], start_list[2], end_list[0], end_list[1], end_list[2] ))
        print("________________________________________________________________________________")
        print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers you can enter \nEnter in 3 to get graphing capabilities\nEnter in 4 to exit the program")


    if selection == '4':
        sys.exit()

    if selection != '1' and selection != '2' and selection != '3' and selection != '4':
        print("Incorrect input entered\n")
        print("________________________________________________________________________________")
        print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers you can enter \nEnter in 3 to get graphing capabilities\nEnter in 4 to exit the program")
