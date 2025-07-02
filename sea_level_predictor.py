import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file

# Load data
 df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
 fig=plt.figure(figsize=(10,10))
 plt.scatter(df["Year"],df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
 lr=linregress(df["Year"],df["CSIRO Adjusted Sea Level"])
 x=pd.Series(range(1880,2051))
 y=lr.slope*x+lr.intercept

 plt.plot(x,y,'r')

    # Create second line of best fit

 df2=df[df["Year"]>=2000]

 lr2=linregress(df2["Year"],df2["CSIRO Adjusted Sea Level"])
 x2=pd.Series(range(2000,2051))
 y2=lr2.slope*x2+lr2.intercept

 plt.plot(x2,y2,'g')

    # Add labels and title
 plt.title("Rise in Sea Level")
 plt.xlabel("Year")
 plt.ylabel("Sea Level (inches)")

    
    # Save plot and return data for testing (DO NOT MODIFY)
 plt.savefig('sea_level_plot.png')
 return plt.gca()