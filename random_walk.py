import cgitb
cgitb.enable()
import numpy as np
import pandas as pd
import scipy.stats
import pandas_datareader as pdr
import yfinance as yf
from datetime import datetime, timedelta
import sys

#DEVELOPER INSTRUCTIONS

#(1) MAKE SURE TO INSTALL THIS PACKAGE IN THE TERMINAL USING THE COMMANDS:
#pip install pandas-datareader
#pip install yfinance

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

    # Test Conditions to handle same start and end date
    if ((a == d) and (b == e) and (c == f)):
        print("The start and end dates are the same. No possible analysis can be done.")
        sys.exit()

    # Test Conditions to handle exceptions where the months exist out of range
    if ((b < 1 or b > 12) or (e < 1 or e > 12)):
        print("There's an issue with the month for start_month or end_month. Please ensure it's between 1 and 12!")
        sys.exit()

    # Test conditions to handle exceptions where days are out of range for non-leap years and regular months
    if ((c < 1) or (f < 1) or ((b == 2 or e == 2) and (c > 28 or f > 28) and (a % 4 != 0 or d % 4 != 0 ))):
        print("There's an issue with the day for either the start date of analysis or end date of analysis!")
        sys.exit()

    # Test Conditions to handle leap year days in the month of February
    if ((b == 2 or e == 2) and (c > 29 or f > 29) and (a % 4 == 0 or d % 4 == 0)):
        print("This is an leap year, the start day and end day are potentially wrong!")
        sys.exit()

    # Test Conditions to handle months with 31 days for start date
    if ((b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12) and (c > 31)):
        print("There is an issue with the day for the start-date.")
        sys.exit()

    # Test Conditions to handle months with 30 days for start date
    if ((b == 4 or b == 6 or b == 9 or b == 11) and (c > 30)):
        print("There is an issue with the day for the start-date.")
        sys.exit()

    # Test Conditions to handle months with 31 days for end date
    if ((e == 1 or e == 3 or e == 5 or e == 7 or e == 8 or e == 10 or e == 12) and (f > 31)):
        print("There is an issue with the day for the end-date.")
        sys.exit()

    # Test Conditions to handle months with 30 days for end date
    if ((e == 4 or e == 6 or e == 9 or e == 11) and (f > 30)):
        print("There is an issue with the day for the end-date.")
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
    return comp1_list.corr(comp2_list)

#placeholder
def compute_volatility(company, start_year, start_month, start_day, end_year, end_month, end_day):
    a = int(start_year)
    b = int(start_month)
    c = int(start_day)
    d = int(end_year)
    e = int(end_month)
    f = int(end_day)

    temp = pdr.get_data_yahoo(symbols = company, start =  datetime(a, b, c), end = datetime(d, e, f))
    comp_list = []
    x = 0
    while (x < len(temp_1)):
        entry = temp['Close'][x]
        entry = round(entry, 2)
        comp_list.append(entry)
        x += 1

    return

#placeholder
def compute_momentum(company, start_year, start_month, start_day, end_year, end_month, end_day):
    a = int(start_year)
    b = int(start_month)
    c = int(start_day)
    d = int(end_year)
    e = int(end_month)
    f = int(end_day)

    temp = pdr.get_data_yahoo(symbols = company, start =  datetime(a, b, c), end = datetime(d, e, f))
    comp_list = []
    x = 0
    while (x < len(temp_1)):
        entry = temp['Close'][x]
        entry = round(entry, 2)
        comp_list.append(entry)
        x += 1

    return




#PART 4: entering command line input to get analysis
#THIS IS THE COOL SHIT
#put in underlining and terminal formatting later
print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers \nEnter in 3 to exit the program")
while True:
    selection = input("Enter option here: ")
    if selection == '1':
        print("________________________________________________________________________________")
        enter_company_1 = input("Enter a ticker here: ")
        enter_company_2 = input("Enter another ticker here: ")
        enter_start = input("Enter start date of analysis as Year, Month, Day (ex: 2010, 7, 16): ")
        enter_end = input("Enter end date of analysis as Year, Month, Day (ex: 2020, 7, 16): ")
        start_list = enter_start.split(", ")
        end_list = enter_end.split(", ")

        print("Here is the correlaton coefficient between the 2 companies: ")
        print(compute_correlation_companies(enter_company_1, enter_company_2,
        start_list[0], start_list[1], start_list[2], end_list[0], end_list[1], end_list[2] ))

        print("Here is the P/E (Price to Earning) Ratios of the two companies: ")
        enter_previous_date = datetime.today() - timedelta(days = 1)
        print("%s %d" %enter_company_1 %compute_pe_ratio(enter_company_1, enter_previous_date))
        print("%s %d" %enter_company_2 %compute_pe_ratio(enter_company_2, enter_previous_date))

        print("________________________________________________________________________________")
        print("\n")
        print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers \nEnter in 3 to exit the program")

    if selection == '2':
        print("________________________________________________________________________________")
        print("\nInstructions: \nEnter in 1 to get a list of market sectors \nEnter in 2 to get a list of relevant market indexes \nEnter in 3 to get a list of ETFs that track different market caps")
        next_selection = input("Enter option here: ")
        if next_selection == '1':
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
            print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers \nEnter in 3 to exit the program")
        if next_selection == '2':
            print("________________________________________________________________________________")
            a = "\nBelow are some tickers you can enter that track market indexes\n"
            b = "S&P 500: VOO\n"
            c = "Dow Jones Industrial Average: DIA\n"
            d = "NASDAQ 100: QQQ\n"
            e = "Russell 2000: VTWO \n"
            f = "Total US Stock Market: VTSMX\n"
            g = "Total World Stock Market: VT\n"
            h = "Short S&P 500: SH\n"
            print(a+b+c+d+e+f+g+h)
            print("________________________________________________________________________________")
            print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers \nEnter in 3 to exit the program")
        if next_selection == '3':
            print("________________________________________________________________________________")
            a = "\nBelow are some tickers you can enter that track different market caps\n"
            b = "US Large Cap: VV\n"
            c = "US Mid Cap: VO\n"
            d = "US Small Cap: VB\n"
            print(a+b+c+d)
            print("________________________________________________________________________________")
            print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers \nEnter in 3 to exit the program")
        if next_selection != '1' and next_selection != '2' and next_selection != '3':
            print("Incorrect input entered\n")
            print("________________________________________________________________________________")
            print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers \nEnter in 3 to exit the program")

    if selection == '3':
        sys.exit()

    if selection != '1' and selection != '2' and selection != '3':
        print("Incorrect input entered\n")
        print("________________________________________________________________________________")
        print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers \nEnter in 3 to exit the program")
