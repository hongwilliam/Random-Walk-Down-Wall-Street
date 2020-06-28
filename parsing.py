import csv 
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/hongwilliam/Random-Walk-Down-Wall-Street/master/fredgraph.csv'
csv_file = pd.read_csv(url)
fig = px.line(csv_file, x = 'DATE', y = 'DEXJPUS', labels = {'DEXJPUS':'Japanese Yen for one USD'}, title = "Japan/U.S Foreign Exchange Rate 10 Year Period")
fig.show()
figone = px.line(csv_file, x = 'DATE', y = 'DJIA',labels = {'DJIA':'Dow Jones Industrial Average in USD'}, title = "Dow Jones Price 10 Year Period")
figone.show()
