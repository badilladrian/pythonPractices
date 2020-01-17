# Find out your current working directory
import os
import pandas as pd
from pandas import DataFrame

print(os.getcwd())
os.chdir(r"C:\\Users\\Usuario\\Documents\\Adrian\\Python\\Python Practices") 

print(os.getcwd())

#data = pd.read_csv("clockinout.csv") 
data = pd.read_csv("clockinout.csv", index_col ="INTERVIEWER_ID")

print(data)

first = data.loc["ja88"]

print(first)
