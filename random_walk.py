#Members: William Hong, Daniel Han, Aaron Chen, Farhan Azad

# Libraries that are required for function performance
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

# Functions Created in Other Files that will be used in our analysis
from companies_lists import companies_lists
from compute_average_daily_price_change import compute_average_daily_price_change
from compute_correlation_companies import compute_correlation_companies
from compute_exponential_moving_average import compute_exponential_moving_average
from compute_stochastic_oscillator import compute_stochastic_oscillator
from compute_volatility import compute_volatility
from data_discrete import data_discrete
from stock_obv_visual import stock_obv_visual

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

#PART 4: entering command line input to get analysis
#THIS IS THE COOL SHIT
print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers you can enter \nEnter in 3 to get graphing capabilities\nEnter in 4 to exit the program")
while True:
    selection = input("Enter option here: ")
    if selection == '1':
        print("________________________________________________________________________________")
        print("Instructions: \nEnter in 1 to compute correlation coefficient between two data points \nEnter in 2 to compute volatility \nEnter in 3 to compute stochastic oscillator\nEnter in 4 to compute average daily percent change\nEnter in 5 to compute exponential moving average")
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
            print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers you can enter \nEnter in 3 to get graphing capabilities\nEnter in 4 to exit the program")

        if next_selection == '3':
            enter_company = input("Enter a ticker here: ")
            enter_date = input("Enter in today's date (ex: 2020, 8, 12): ")
            date_list = enter_date.split(", ")
            print("Here is the stochastic oscillator for %s: " %enter_company)
            compute_stochastic_oscillator(enter_company, date_list[0], date_list[1], date_list[2])
            print("________________________________________________________________________________")
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
            print("________________________________________________________________________________")
            print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers you can enter \nEnter in 3 to get graphing capabilities\nEnter in 4 to exit the program")

        if next_selection != '1' and next_selection != '2' and next_selection != '3' and next_selection != '4' and next_selection != '5':
            print("Incorrect input entered")
            print("________________________________________________________________________________")
            print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers you can enter \nEnter in 3 to get graphing capabilities\nEnter in 4 to exit the program")

    if selection == '2':
        print("________________________________________________________________________________")
        print("Instructions: \nEnter in 1 to get a list of relevant market indexes \nEnter in 2 to get a list of US market sectors \nEnter in 3 to get a list of commodities\nEnter in 4 to get a list of US Treasury bonds and currencies")
        next_selection = input("Enter option here: ")
        if next_selection == '1':
            print("________________________________________________________________________________")
            a = "Below are some tickers you can enter that track market indexes\n"
            b = "S&P 500: ^GSPC\n"
            c = "Dow Jones Industrial Average: ^DJI\n"
            d = "NASDAQ Composite: ^IXIC\n"
            e = "Russell 2000: ^RUT \n"
            f = "S&P 400: ^SP400\n"
            g = "FTSE 100: %5EFTSE%3FP%3DFTSE\n"
            h = "EURO Stoxx 50: ^STOXX50E\n"
            i = "DAX 30: ^GDAXI\n"
            j = "CAC 40: ^FCHI\n"
            k = "Nikkei 225: ^N225\n"
            l = "Shanghai Composite: 000001.SS\n"
            m = "Hang Seng Index: ^HSI\n"
            n = "KOSPI: ^KS11\n"
            o = "Bovespa Index: BVSP\n"
            p = "VIX Volatility Index: ^VIX"
            print(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p)
            print("________________________________________________________________________________")
            print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers you can enter \nEnter in 3 to get graphing capabilities\nEnter in 4 to exit the program")
        if next_selection == '2':
            print("________________________________________________________________________________")
            a = "Below are some tickers you can enter that represent market sectors\n"
            b = "Communication Services: VOX\n"
            c = "Consumer Discretionary: VCR\n"
            d = "Consumer Staples: VDC\n"
            e = "Energy: VDE\n"
            f = "Financials: VFH\n"
            g = "Health: VHT\n"
            h = "Industrials: VAW\n"
            i = "Materials: VMC\n"
            j = "Real Estate: VNQ\n"
            k = "Technology: VGT\n"
            l = "Utilities: VPU"
            print(a+b+c+d+e+f+g+h+i+j+k+l)
            print("________________________________________________________________________________")
            print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers you can enter \nEnter in 3 to get graphing capabilities\nEnter in 4 to exit the program")
        if next_selection == '3':
            print("________________________________________________________________________________")
            a = "Below are some tickers you can enter that track commodities futures\n"
            b = "Gold: GC=F\n"
            c = "Silver: SI=F\n"
            d = "Copper: HG=F\n"
            e = "Platinum: PL=F\n"
            f = "Corn: ZC=F\n"
            g = "Soybeans: ZS=F\n"
            h = "Sugar: SB=F\n"
            i = "Coffee: KC=F\n"
            j = "Cocoa: CC=F\n"
            k = "Cotton: CT=F\n"
            l = "Rough Rice: ZR=F\n"
            m = "Wheat: KE=F\n"
            n = "Crude Oil: CL=F\n"
            o = "Heating Oil: HO=F\n"
            p = "RBOB Gasoline: RB=F\n"
            q = "Natural Gas: NG=F"
            print(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q)
            print("________________________________________________________________________________")
            print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers you can enter \nEnter in 3 to get graphing capabilities\nEnter in 4 to exit the program")

        if next_selection == '4':
            print("________________________________________________________________________________")
            a = "Below are some tickers you can enter that track US Treasury bond yields and currency exchange rates\n"
            b = "US Treasury 10 Year Bond: ^TNX\n"
            c = "US Treasury 5 Year Bond: ^FVX\n"
            d = "US Treasury 30 Year Bond: ^TYX\n"
            e = "US Dollar/Euro Exchange Rate: USDEUR=X\n"
            f = "US Dollar/Yen Exchage Rate: JPY=X\n"
            g = "US Dollar/Pound Sterling Exchange Rate: GBP=X\n"
            h = "US Dollar/Yuan Exchange Rate: CNH=X\n"
            i = "Euro/Yen Exchange Rate: EURJPY=X\n"
            j = "Bitcoin/US Dollar: BTCUSD=X"
            print(a+b+c+d+e+f+g+h+i+j)
            print("________________________________________________________________________________")
            print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers you can enter \nEnter in 3 to get graphing capabilities\nEnter in 4 to exit the program")

        if next_selection != '1' and next_selection != '2' and next_selection != '3' and next_selection != '4':
            print("Incorrect input entered")
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
        plt.close()
        plt.close()


    if selection == '4':
        sys.exit()

    if selection != '1' and selection != '2' and selection != '3' and selection != '4':
        print("Incorrect input entered")
        print("________________________________________________________________________________")
        print("Instructions: \nEnter in 1 to start analysis \nEnter in 2 to get a list of useful tickers you can enter \nEnter in 3 to get graphing capabilities\nEnter in 4 to exit the program")
