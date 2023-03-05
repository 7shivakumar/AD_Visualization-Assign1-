# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 17:23:27 2023
@author: Shiva Kumar Sundara Murthy

This code plots 3 different visualisations that is line plot, pie plot, Histogram using 3 different data sets.
"""

import pandas as pd
import matplotlib.pyplot as plt

def linechart(df):
    
    """
    This linechart function plots various line graph for the fossil fuel consumptions over years
    for various countries.
    
    """
    
    df = df.dropna(axis = 'columns')

    #Ploting line graphs for values of fossil fuel consumption upon various years for varius contries
    plt.plot(df['Year'], df['Switzerland'], label='Switzerland')
    plt.plot(df['Year'], df['Spain'], label='Spain')
    plt.plot(df['Year'], df['India'], label='India')
    plt.plot(df['Year'], df['Germany'], label='Germany')
    plt.plot(df['Year'], df['United States'], label='United States')
    
    #setting up the labels for chart and printing it
    plt.xlabel('Years')
    plt.ylabel('% of Fossil fuel Consumption')
    plt.title('Various Countries Fossil Fuel Consumptions from 1996-2003')
    plt.legend()
    plt.show()
    

def Histogram(df):
    
    """
    This Histogram function plots Histo graph based on number of missions launched by 
    SpaceX over years i.e from 2006-2023.
    
    """
    df['Launch year'] = pd.to_datetime(df['Launch Date'])
    df['Launch year'] = df['Launch year'].dt.year
    #from the dataset, ploting Histograph for the number of rockets launched based every year from 2006 - 2023
    plt.hist(df['Launch year'],edgecolor='black',bins=range(2006, 2023))
    
    #setting labels and ploting the graph
    plt.xlabel('year')
    plt.ylabel('Number of Launches')
    plt.title('Number of spaceX launches per Year')
    plt.show()
    

def Piechart(df):
    
    """
    This Piechart function plots Pie graph by calculating the mean of fresh water withdrawls upon years from
    various countries calculates percentile and displays them.

    """
    
    # Dropping cloumns which are having Nan values for avoiding discrepency in chart, and also dropping two countries for 
    df = df.dropna(axis = 'columns')
    df = df.drop('India',axis=1)
    df = df.drop('United States',axis=1)
    
    # Calculating the mean of whole columns which gives average Fresh water Withdrawls from Year 1996-2003
    mean = list(df.mean())
    mean.pop(0)
    
    # Pulling out the column names and storing in list for labeling the pie chart
    countries = list(df.columns)
    countries.pop(0)
    
    # creating Pie chart using the obtained mean values and setting the attributes
    plt.pie(mean, labels = countries,shadow = True,autopct ='%1.1f%%',startangle = 90, explode=(0,0.2,0.1,0,0.1,0,0.3))
    plt.title("Fresh Water Withdrawls between various countries from 1996 -2003 \n \n")
    plt.show()

    
#importing Fossil Fuel Consumption dataset to data
data = pd.read_excel("Fossil Fuel Consumption.xlsx")
#calling linechart function to plot line char
linechart(data)

#importing Freshwater Withdrawals dataset to Freshwater_data
Freshwater_data = pd.read_excel('Freshwater Withdrawals.xlsx')
#calling Piechart function to plot Piechart
Piechart(Freshwater_data)

#importing Spacex missions dataset to spaceX_missions
SpaceX_missions =  pd.read_csv("database.csv")

#calling Histogram function to histogram chart
Histogram(SpaceX_missions)