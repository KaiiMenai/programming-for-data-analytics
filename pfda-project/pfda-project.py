# Code for analysing data for the PFDA project.
# Author: Kyra Menai Hamilton

# Data source: https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%5D,%22dimension%22:%7B%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22CSV%22,%22version%22:%221.0%22%7D,%22matrix%22:%22AFA01%22%7D,%22version%22:%222.0%22%7D%7D

# import the modules needed for analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import io
import statsmodels.api as sm
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from scipy import stats

# Load the data from the CSO API and save the dataset as a CSV file
url = "https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%5D,%22dimension%22:%7B%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22CSV%22,%22version%22:%221.0%22%7D,%22matrix%22:%22AFA01%22%7D,%22version%22:%222.0%22%7D%7D"
response = requests.get(url)
json_data = response.json()
csv_string = json_data['result']
data = pd.read_csv(io.StringIO(csv_string))
data.to_csv('pfda-project/pfda_data.csv', index=False)
# note if saved successfully, a file named 'pfda_data.csv' will appear in the working directory

# Read the dataset
data = pd.read_csv('pfda-project/pfda_data.csv')
# Display the first few rows of the dataset
print(data.head())
