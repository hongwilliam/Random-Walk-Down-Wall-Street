import cgitb
cgitb.enable()
import math
import numpy
import scipy

#basic statistics exercise

def compute_mean(list):
    sum = 0
    i = 0
    while i < len(list):
        sum += list[i]
        i += 1
    #print(sum / len(list))
    return sum / len(list)

def compute_variance(list):
    mean = compute_mean(list)
    sum_squared_deviations = 0
    squared_deviation = 0
    n = len(list)
    i = 0
    while i < len(list):
        squared_deviation = (list[i] - mean) ** 2
        sum_squared_deviations += squared_deviation
        i += 1
    variance = sum_squared_deviations / (n-1)
    #print (variance)
    return variance

def compute_standard_deviation(list):
    #this is for sample standard deviation, not population
    variance = compute_variance(list)
    print (math.sqrt(variance))
    return math.sqrt(variance)

def compute_z_score(x, mu, sigma):
    #mu = mean, sigma = standard deviation
    #represents how many SDs that x is away from the mean
    #print ((x-mu)/sigma)
    return (x-mu)/sigma

#add expected value and covariance later
