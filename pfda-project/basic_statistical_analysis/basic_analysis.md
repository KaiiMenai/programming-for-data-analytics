# Basic Statistical Analysis on Ireland Afforestation Data

***Author: Kyra Menai Hamilton***

## Summary

## Interesting Statistics Findings for Counties 


1. Average VALUE per county (excluding Ireland for county-specific analysis)
| County        |    VALUE |
|:--------------|---------:|
| Co. Cork      | 287.549  |
| Co. Clare     | 185.673  |
| Co. Kerry     | 180.842  |
| Co. Mayo      | 143.766  |
| Co. Galway    | 136.884  |
| Co. Roscommon | 135.283  |
| Co. Tipperary | 133.265  |
| Co. Leitrim   | 120.72   |
| Co. Cavan     | 101.176  |
| Co. Limerick  |  96.1438 |

### 2. Total VALUE per County
Total afforestation value summed across all years.
| County        |   VALUE |
|:--------------|--------:|
| Co. Cork      |   43995 |
| Co. Clare     |   28408 |
| Co. Kerry     |   27488 |
| Co. Mayo      |   22715 |
| Co. Roscommon |   22457 |
| Co. Galway    |   21217 |
| Co. Tipperary |   20123 |
| Co. Leitrim   |   18108 |
| Co. Cavan     |   15480 |
| Co. Limerick  |   14710 |

### 3. Coefficient of Variation per County
Measures relative variability (std/mean); higher values indicate more year-to-year inconsistency.
| County        |   VALUE |
|:--------------|--------:|
| Co. Donegal   | 1.46297 |
| Co. Wexford   | 1.24197 |
| Co. Waterford | 1.20094 |
| Co. Kilkenny  | 1.16203 |
| Co. Tipperary | 1.13245 |
| Co. Kildare   | 1.13011 |
| Co. Limerick  | 1.12238 |
| Co. Sligo     | 1.10442 |
| Co. Dublin    | 1.0859  |
| Co. Offaly    | 1.07014 |

### 4. Maximum VALUE per County
Peak afforestation value in any single year.
| County        |   VALUE |
|:--------------|--------:|
| Co. Cork      |    1157 |
| Co. Kerry     |     736 |
| Co. Clare     |     695 |
| Co. Galway    |     561 |
| Co. Mayo      |     548 |
| Co. Tipperary |     546 |
| Co. Leitrim   |     536 |
| Co. Kilkenny  |     523 |
| Co. Roscommon |     449 |
| Co. Limerick  |     441 |

### 5. Number of Years with Data per County
Indicates data completeness for each county.
| County       |   Year |
|:-------------|-------:|
| Co. Carlow   |     17 |
| Co. Cavan    |     17 |
| Co. Clare    |     17 |
| Co. Cork     |     17 |
| Co. Donegal  |     17 |
| Co. Galway   |     17 |
| Co. Kildare  |     17 |
| Co. Kerry    |     17 |
| Co. Kilkenny |     17 |
| Co. Laois    |     17 |

### 6. Growth Rate per County
Simplified growth rate: (last year's VALUE - first year's VALUE) / first year's VALUE.
| County        |         0 |
|:--------------|----------:|
| Co. Meath     | -0.52381  |
| Co. Louth     | -0.763636 |
| Co. Carlow    | -0.767442 |
| Co. Leitrim   | -0.790576 |
| Co. Dublin    | -0.833333 |
| Co. Cavan     | -0.9      |
| Co. Galway    | -0.908189 |
| Co. Laois     | -0.909722 |
| Co. Tipperary | -0.917582 |
| Co. Offaly    | -0.933333 |

## Data Sources and Outputs
- Raw data: pfda_data.csv
- Summary statistics: summary_statistics.csv
- All statistical CSVs are in the basic_statistical_analysis/ folder.
- Plots are saved in outputs/ as PNG files.
