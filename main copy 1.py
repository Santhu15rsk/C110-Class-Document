## Let's start with the temperature data in the room.
## Here is the code draw a plot for the temperature data?


import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

#We are reading complete data in data.csv and giving it to df
df = pd.read_csv("data.csv")
#We are taking only the temperature values and giving it to data
data = df["temp"].tolist()

# code to show the plot of raw data
fig = ff.create_distplot([data], ["temp"], show_hist=False)
fig.show()


### Check output : You should get a graph

## Is the distribution normal? NO
## So clearly, there are datasets which
## do not follow normal distribution.

# Let us try to find the mean and
# standard deviation of the data we have.



