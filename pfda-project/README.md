# PFDA Project Content here

## Author: Kyra Mensi Hamilton

The files within this folder are for the PFDA module project.

### [PFDA project description](https://vlegalwaymayo.atu.ie/pluginfile.php/1804303/mod_resource/content/2/Project%20Description.pdf)

### Data Source

The data was sourced from the [CSO webpage](https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%5D,%22dimension%22:%7B%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22CSV%22,%22version%22:%221.0%22%7D,%22matrix%22:%22AFA01%22%7D,%22version%22:%222.0%22%7D%7D)sd2

### Packages

To conduct analysis, install the following modules.

```
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
```

### Standardised Font

To ensure all plots have standardised font sizes I used:

```
plt.rcParams.update({
    'font.size': 14,
    'axes.labelsize': 16,
    'axes.titlesize': 18,
    'legend.fontsize': 12,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12
})
```

### URL to CSV

Save the data from the CSO URL as a csv.

```
# Load the data from the CSO API and save the dataset as a CSV file.
url = "https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%5D,%22dimension%22:%7B%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22CSV%22,%22version%22:%221.0%22%7D,%22matrix%22:%22AFA01%22%7D,%22version%22:%222.0%22%7D%7D"
response = requests.get(url)
json_data = response.json()
csv_string = json_data['result']
data = pd.read_csv(io.StringIO(csv_string))
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    script_dir = os.getcwd()  # For Jupyter notebooks
csv_path = os.path.join(script_dir, 'pfda_data.csv')
data.to_csv(csv_path, index=False)
# note if saved successfully, a file named 'pfda_data.csv' will appear in the working directory
```

### Subfolders

Subfolders were made in the pfda-project folder in the repository.

```
# Create a subfolder for outputs
outputs_dir = os.path.join(script_dir, 'outputs')
os.makedirs(outputs_dir, exist_ok=True)

# Create a subfolder for basic statistical analysis
basic_analysis_dir = os.path.join(script_dir, 'basic_statistical_analysis')
os.makedirs(basic_analysis_dir, exist_ok=True)
```

### Analysis

The type of analysis conducted in this project included:

- frequency plots
- basic statistical analysis
- summary statistics
- correlation matrix
- boxplots
- general plots for value (hectares) vs Forest Owner/Species/County
- t-test
- linear regression

### Main findings

- There were significant differences between the values recorded for afforestation in 2007 and in 2023.
    - p = 0.00034
- Following the linear regression model analysis, if afforestation continues along the same trend, then Ireland will not reach it's goal value of 8000 hectares of afforestation per annum in order to meet the 2050 goal of 18 % forest coverage.

# END