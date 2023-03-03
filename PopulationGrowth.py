# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 11:15:54 2023

@author: pv22aar
"""

#import modules pandas and matplot
import pandas as pd
import matplotlib.pyplot as plt

#read csv file
df = pd.read_csv(r'./data_multiple_line.csv')

#Function for plotting Line plot
def linefunction():
   
    ax = df.plot(x='Country', y=['1970', '1980', '1990', '2000']) 

#setting labels    
    ax.set_ylabel("Population Growth")
    plt.savefig("lineplot.png")
#calling the title function for setting a title   
    plt.title('Population Growth 1970-2000')    
    plt.show()
linefunction() #calling the defined function for line plot 

#Function for plotting Bar Graph
def barfunction():
    
#plotting population growth during the following years    
    ax = df.plot(x='Country', y=['1970', '1980', '1990', '2000'],kind='bar')

#setting labels    
    ax.set_ylabel("Population Growth")
    plt.savefig("BarChart.png")
#calling the title function for setting a title   
    plt.title('Population Growth 1970-2000')
    plt.show()
barfunction() #calling the defined function for bar plot

#Function for plotting Pie Chart
def piechart():
    
#plotting pie chart for the year 1980
    country = df["Country"]
    year = df["1980"]
#choosing colours for the pie chart
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
    plt.pie(year, labels=country, colors=colors, autopct='%1.1f%%', startangle=140)
#calling the title function for setting a title    
    plt.title('Population Growth in 1980')
    plt.legend(bbox_to_anchor=(2,1))
    plt.savefig("PieChart.png")
    plt.show()
piechart() #calling the defined function for pie chart
    

