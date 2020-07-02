import cgitb
cgitb.enable()
import numpy as np
import pandas as pd

#note to developers: go on terminal in the directory this file is in
#type python stat_functions.py to excecute the file

#TESTING BASIC STATISTICAL FUNCTIONS


#PART 1: testing the mean function
list_1 = np.array([1, 2, 3, 4, 5])
print(np.mean(list_1)) #should return 3


#PART 2: testing mean on 2 dimensional arrays
list_2 = np.array([ [1, 2, 3], [4, 5, 6] ]) #list of lists
print(np.mean(list_2)) #should return 3.5
print(np.mean(list_2[0])) #should return mean of first list, which is 2

#should return mean of 1 and 4, 2 and 5, 3 and 6... which is [2.5 3.5 4.5]
print(np.mean(list_2, axis = 0))

#should return mean of 1,2,3 and 4,5,6... which is [2. 5.]
print(np.mean(list_2, axis = 1))


#PART 3: testing the standard deviation function
list_3 = np.array([1, 2, 3, 4])
print(np.std(list_3)) #should return 1.118 ish


#PART 4: testing the covariance function
#covariance > 0 is positively correlated, 0 is uncorrelated, < 0 is negatively

#perfect negative correlation
list_4 = [0, 1, 2]
list_5 = [2, 1, 0]
list_4 = pd.Series(list_4)
list_5 = pd.Series(list_5)
print(list_4.cov(list_5)) #should return -1

#perfect positive correlation
list_6 = [0, 1, 2]
list_7 = [1, 2, 3]
list_6 = pd.Series(list_6)
list_7 = pd.Series(list_7)
print(list_6.cov(list_7)) #should return 1
