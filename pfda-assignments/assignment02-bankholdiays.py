# bankholidays.py 
# This program will read bank holidays from a json file and print them out - specifically for Northern Ireland.
# The second part of the assignment is to write a function that will return the number of bank holidays unique to Northern Ireland.

# The json is available from https://www.gov.uk/bank-holidays.json

import json
import urllib.request
import datetime
import requests
import pandas as pd

# This is split into Part 1 and part 2 - Part 1 is to read the json file and print out the bank holidays for Northern Ireland. - outputs are at the end of the program in note form.

url =" https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
# print(data)                                       # to check it works

df = pd.DataFrame.from_dict(data)                   # convert to dataframe using pandas
print(df)

dfs = []                                            # To create an empty list to hold dataframes for making it easier to read later on I used this reference: 
for country, data in data.items():                  # https://stackoverflow.com/questions/53953814/convert-nested-json-to-pandas-dataframe
    df = pd.DataFrame(data['events'])
    df['Country'] = country
    dfs.append(df)

final = pd.concat(dfs, ignore_index=True)
final['date'] = pd.to_datetime(final['date'])        # convert date to datetime format
# print(final)

# This will filter the dataframe to show only Northern Ireland bank holidays for all years.
#ni_holidays_df = final[final['Country'] == 'northern-ireland']
#print(ni_holidays_df)                               # print out the bank holidays for Northern Ireland

# As (ni_holidays_df) doesn't limit it to one year (which will make things easier later on), I decided to focus on 2026.

# Need to be able to filter the dataframe to show only Northern Ireland bank holidays for 2026.
ni_holidays2026_df = final[(final['Country'] == 'northern-ireland') & (final['date'].dt.year == 2026)]
print(ni_holidays2026_df)                           # print out the bank holidays for Northern Ireland for 2026.

## PART 2.

# Output the number of bank holidays unique to Northern Ireland in 2026.
# Use a function to define this - Holidays unique to Northern Ireland are those that do not appear in the bank holidays for England and Wales, Scotland or UK in 2026.
# For the holiday and date, see https://www.gov.uk/bank-holidays
def unique_ni_holidays_2026():
    ni_holidays2026 = set(ni_holidays2026_df['title'])  # Get the set of Northern Ireland holidays in 2026.
    eng_wales_holidays2026 = set(final[(final['Country'] == 'england-and-wales') & (final['date'].dt.year == 2026)]['title']) # Get the holidays for England and Wales in 2026.
    scotland_holidays2026 = set(final[(final['Country'] == 'scotland') & (final['date'].dt.year == 2026)]['title']) # Get the holidays for Scotland in 2026.
    uk_holidays2026 = set(final[(final['Country'] == 'uk') & (final['date'].dt.year == 2026)]['title']) # Get the holidays for UK in 2026. - This could include places like Isle of Man, Jersey, Guernsey, and the Channel Islands.
    
    # Find unique holidays to Northern Ireland
    unique_holidays = ni_holidays2026 - eng_wales_holidays2026 - scotland_holidays2026 - uk_holidays2026 # unique holidays to Northern Ireland = ni-)eng+wal)-scot-uk
    
    return len(unique_holidays), unique_holidays

# Call the function and print the result, and name the holidays.
num_unique_holidays, unique_holiday_names = unique_ni_holidays_2026()
print("Number of bank holidays unique to Northern Ireland in 2026:", num_unique_holidays)   # Number of unique holidays.
print("Unique bank holidays by name in Northern Ireland in 2026:", unique_holiday_names)    # Names of unique holidays.

## OUTPUT - PART 1

##                                      title       date           notes  bunting           Country
## 88                         New Year’s Day 2026-01-01                     True  northern-ireland
## 89                       St Patrick’s Day 2026-03-17                     True  northern-ireland
## 90                            Good Friday 2026-04-03                    False  northern-ireland
## 91                          Easter Monday 2026-04-06                     True  northern-ireland
## 92                 Early May bank holiday 2026-05-04                     True  northern-ireland
## 93                    Spring bank holiday 2026-05-25                     True  northern-ireland
## 94  Battle of the Boyne (Orangemen’s Day) 2026-07-13  Substitute day    False  northern-ireland
## 95                    Summer bank holiday 2026-08-31                     True  northern-ireland
## 96                          Christmas Day 2026-12-25                     True  northern-ireland
## 97                             Boxing Day 2026-12-28  Substitute day     True  northern-ireland

## OUTPUT - PART 2

# Number of bank holidays unique to Northern Ireland in 2026: 2
# Unique bank holidays by name in Northern Ireland in 2026: {'Battle of the Boyne (Orangemen’s Day)', 'St Patrick’s Day'}

## END OF PROGRAM