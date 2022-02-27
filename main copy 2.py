import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["temp"].tolist()
population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("population mean:- ", population_mean)
print("std_deviation:- ", std_deviation)


### Check output 
# We know the mean and standard
# deviation of the data. We also know
# that the data does not have a normal distribution


# Now, let's do a small experiment.
# Let's takes out 100 random data
# points from the raw temperature data.
# 100 random data points is called "sample data"
# and raw temperature data is called
# "population data"
# We will collect 100 random data
# points, calculate the mean & standard
# deviation and print it on the console.
