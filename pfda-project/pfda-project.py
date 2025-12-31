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
import os

# Load the data from the CSO API and save the dataset as a CSV file
url = "https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%5D,%22dimension%22:%7B%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22CSV%22,%22version%22:%221.0%22%7D,%22matrix%22:%22AFA01%22%7D,%22version%22:%222.0%22%7D%7D"
response = requests.get(url)
json_data = response.json()
csv_string = json_data['result']
data = pd.read_csv(io.StringIO(csv_string))
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'pfda_data.csv')
data.to_csv(csv_path, index=False)
# note if saved successfully, a file named 'pfda_data.csv' will appear in the working directory

# Create a subfolder for outputs
outputs_dir = os.path.join(script_dir, 'outputs')
os.makedirs(outputs_dir, exist_ok=True)

# Read the dataset
data = pd.read_csv(csv_path)
# Display the first few rows of the dataset
print(data.head())

# Now to clean the dataset
# Check for missing values
print(data.isnull().sum())

# Drop rows with missing values
data = data.dropna()
# Verify that there are no more missing values
print(data.isnull().sum())
# Display data types of each column
print(data.dtypes)

# For now I think the data types are fine, but if needed we can convert them later.
# Basic Data Exploration
# Summary Statistics for value vs county vs year
summary_stats = data.groupby(['County', 'Year'])['VALUE'].describe()
print(summary_stats)
# Save summary statistics to a CSV file
summary_stats_path = os.path.join(outputs_dir, 'summary_statistics.csv')
summary_stats.to_csv(summary_stats_path)


# Visualize distributions of key variables
plt.figure(figsize=(10, 6))
sns.histplot(data['VALUE'], bins=30, kde=True)
plt.title('Distribution of Values')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
# Save the plot
hist_path = os.path.join(outputs_dir, 'value_distribution.png')
plt.savefig(hist_path)

# Visualise the Value over the years for Ireland as a whole
ireland_data = data[data['County'] == 'Ireland']
plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='VALUE', data=ireland_data, marker='o')
plt.title('Value over Years for Ireland')
plt.xlabel('Year')
plt.ylabel('Value')
plt.grid()
plt.show()
# Save the plot
lineplot_path = os.path.join(outputs_dir, 'value_over_years_ireland.png')
plt.savefig(lineplot_path)

# Analyse data over the years for Ireland as a whole. Look at species trends
species_trends = ireland_data.groupby(['Year', 'Species'])['VALUE'].sum().reset_index()
plt.figure(figsize=(35, 15))
sns.lineplot(x='Year', y='VALUE', hue='Species', data=species_trends, marker='o')
plt.title('Species Trends over Years for Ireland')
plt.xlabel('Year')
plt.ylabel('Value')
plt.legend(title='Species', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid()
plt.show()
# Save the plot
species_trends_path = os.path.join(outputs_dir, 'species_trends_ireland.png')
plt.savefig(species_trends_path)    

# I wanted to further analyse the data using regression models, but I think the data is not sufficient for that purpose.
# So I decided to look at correlations between numerical variables instead.
# I wanted to look to see if there were any correlations between the species planted and the Forest owner.
correlation_data = data[['Species', 'Forest Owner', 'VALUE']]#
correlation_data = correlation_data.dropna()
correlation_data['Species_Code'] = correlation_data['Species'].astype('category').cat.codes
correlation_data['Forest_Owner_Code'] = correlation_data['Forest Owner'].astype('category').cat.codes
correlation_matrix = correlation_data[['Species_Code', 'Forest_Owner_Code', 'VALUE']].corr()
print(correlation_matrix)
# Visualize the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()
# Save the plot
correlation_matrix_path = os.path.join(outputs_dir, 'correlation_matrix.png')
plt.savefig(correlation_matrix_path)    
# Save the correlation matrix to a CSV file
correlation_matrix_csv_path = os.path.join(outputs_dir, 'correlation_matrix.csv')
correlation_matrix.to_csv(correlation_matrix_csv_path)  

# Now for analysis for the forest owner types over the years for Ireland as a whole
forest_owner_trends = ireland_data.groupby(['Year', 'Forest Owner'])['VALUE'].sum().reset_index()
plt.figure(figsize=(35, 15))
sns.lineplot(x='Year', y='VALUE', hue='Forest Owner', data=forest_owner_trends, marker='o')
plt.title('Forest Owner Trends over Years for Ireland')
plt.xlabel('Year')
plt.ylabel('Value')
plt.legend(title='Forest Owner', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid()
plt.show()
# Save the plot
forest_owner_trends_path = os.path.join(outputs_dir, 'forest_owner_trends_ireland.png')
plt.savefig(forest_owner_trends_path)   

# Now I want to analyse the data for specific counties. I want to look at the top 5 counties with the highest total value over the years.
county_totals = data.groupby('County')['VALUE'].sum().reset_index()
top_5_counties = county_totals.nlargest(5, 'VALUE')['County'].tolist()
print("Top 5 Counties with highest total value over the years:", top_5_counties)

for county in top_5_counties:
    county_data = data[data['County'] == county]
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Year', y='VALUE', data=county_data, marker='o')
    plt.title(f'Value over Years for {county}')
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.grid()
    plt.show()
    # Save the plot
    county_plot_path = os.path.join(outputs_dir, f'value_over_years_{county.replace(" ", "_").lower()}.png')
    plt.savefig(county_plot_path)
    # Further analysis for species trends in the county
    species_trends_county = county_data.groupby(['Year', 'Species'])['VALUE'].sum().reset_index()
    plt.figure(figsize=(20, 12))
    sns.lineplot(x='Year', y='VALUE', hue='Species', data=species_trends_county, marker='o')
    plt.title(f'Species Trends over Years for {county}')
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.legend(title='Species', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid()
    plt.show()
    # Save the plot
    species_trends_county_path = os.path.join(outputs_dir, f'species_trends_{county.replace(" ", "_").lower()}.png')
    plt.savefig(species_trends_county_path)
    # Further analysis for forest owner trends in the county
    forest_owner_trends_county = county_data.groupby(['Year', 'Forest Owner'])['VALUE'].sum().reset_index()
    plt.figure(figsize=(20, 12))
    sns.lineplot(x='Year', y='VALUE', hue='Forest Owner', data=forest_owner_trends_county, marker='o')
    plt.title(f'Forest Owner Trends over Years for {county}')
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.legend(title='Forest Owner', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid()
    plt.show()
    # Save the plot
    forest_owner_trends_county_path = os.path.join(outputs_dir, f'forest_owner_trends_{county.replace(" ", "_").lower()}.png')
    plt.savefig(forest_owner_trends_county_path)
plt.figure(figsize=(10, 6))
sns.histplot(data['VALUE'], bins=30, kde=True)
plt.title('Distribution of Values')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
# Save the plot
hist_path = os.path.join(outputs_dir, 'value_distribution.png')
plt.savefig(hist_path)  
# Visualise the Value over the years for Ireland as a whole
ireland_data = data[data['County'] == 'Ireland']
plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='VALUE', data=ireland_data, marker='o')
plt.title('Value over Years for Ireland')
plt.xlabel('Year')
plt.ylabel('Value')
plt.grid()
plt.show()
# Save the plot
lineplot_path = os.path.join(outputs_dir, 'value_over_years_ireland.png')
plt.savefig(lineplot_path)

# I want to look to see if there has been a significant difference in afforestation between the first year and most recent year.
first_year = data['Year'].min()
most_recent_year = data['Year'].max()   
first_year_data = data[data['Year'] == first_year]['VALUE']
most_recent_year_data = data[data['Year'] == most_recent_year]['VALUE']
t_stat, p_value = stats.ttest_ind(first_year_data, most_recent_year_data)
print(f"T-statistic: {t_stat}, P-value: {p_value}")
if p_value < 0.05:
    print("There is a significant difference in afforestation between the first year and the most recent year.")
else:
    print("There is no significant difference in afforestation between the first year and the most recent year.")

# Since there is a difference in the afforestation between the first and most recent year, I want to visualise this using boxplots.
plt.figure(figsize=(10, 6))
sns.boxplot(x='Year', y='VALUE', data=data[data['Year'].isin([first_year, most_recent_year])])
plt.title('Afforestation Values: First Year vs Most Recent Year')
plt.xlabel('Year')
plt.ylabel('Value')
plt.show()
# Save the plot
boxplot_path = os.path.join(outputs_dir, 'afforestation_boxplot.png')
plt.savefig(boxplot_path)
plt.figure(figsize=(10, 6))
sns.histplot(data['VALUE'], bins=30, kde=True)
plt.title('Distribution of Values')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
# Save the plot
hist_path = os.path.join(outputs_dir, 'value_distribution.png')
plt.savefig(hist_path)

