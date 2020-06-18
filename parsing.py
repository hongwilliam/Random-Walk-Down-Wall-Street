import csv 
import matplotlib.pyplot as plt
import numpy as np

url = 'https://raw.githubusercontent.com/hongwilliam/Random-Walk-Down-Wall-Street/master/fredgraph.csv'
dates = pd.read_csv(url, usecols = ['DATE'])
usd_yen = pd.read_csv(url, usecols = ['DEXJPUS'])
dow = pd.read_csv(url, usecols = ['DJIA'])

# dates
plt.plot(dates, usd_yen)
plt.plot(dates, dow)

plt.show()



