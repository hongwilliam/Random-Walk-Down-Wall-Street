import csv 
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/hongwilliam/Random-Walk-Down-Wall-Street/master/fredgraph.csv'
csv_file = pd.read_csv(url)
fig = px.line(csv_file, x = 'DATE', y = 'DEXJPUS')
fig.show()
figone = px.line(csv_file, x = 'DATE', y = 'DJIA')
figone.show()



