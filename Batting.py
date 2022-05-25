

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a script that determines what batters from 2000 to 2021 had a good performance in effort of m
"""


import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

batting_table=pd.read_csv(r"//Users//mariopadilla//Documents//Python Scripts//baseballdatabank-2022.2//core//Batting.csv")
def batters(batting,year,AB_Cutoff):
    #remove batters before defined year in argument
    batting=batting[batting.yearID>=year]
    #remove instances where batters had less than defined AB number in argument
    batting=batting[batting.AB>=AB_Cutoff]
    #make Singles hit column ("1B")
    batting["1B"]=batting['H']-(batting['2B']+batting['3B']+batting['HR'])
    #create OBP column (On Base Percentage)
    batting['OBP']=(batting['H']+batting['BB']+batting['HBP'])/(batting['AB']+batting['BB']+batting['HBP']+batting['SF'])
    #create slugging column
    batting['Slugging']=(batting['1B']+2*batting['2B']+3*batting['3B']+4*batting['HR'])/batting['AB']
    #create batting average column
    batting["Ave"]=batting['H']/batting['AB']
    return(batting)

batting_adj=batters(batting_table,2000,300)
    
x=batting_adj['OBP']
y=batting_adj['Slugging']
z=batting_adj['Ave']

dots=plt.axes(projection='3d')
dots.set_xlabel("OBP")
dots.set_ylabel("Slugging")
dots.set_zlabel("Ave")
dots.scatter(x,y,z)
dots.set_title("Batting Statistics")