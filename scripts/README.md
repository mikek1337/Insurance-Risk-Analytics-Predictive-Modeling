# Insurance Risk Analytics - Python Modules

This project contains two main Python modules for data preprocessing and visualization:

- [`scripts/preprocess.py`](scripts/preprocess.py): Data cleaning, transformation, and utility functions.
- [`scripts/plots.py`](scripts/plots.py): Visualization utilities for exploratory data analysis.

---

## `preprocess.py`

This module provides functions for cleaning, transforming, and preparing insurance data for analysis and modeling.

### Key Functions

- **load_data(filename)**  
  Loads a CSV file from the `../data/` directory using a pipe (`|`) delimiter.

- **find_and_replace_outliers_with_median(df, cols, threshold=3)**  
  Detects outliers in specified numeric columns using the z-score method and replaces them with the column median.

- **find_outliers(df, threshold=3)**  
  Identifies columns containing outliers based on the z-score method.

- **IQR_outlier(df, cols=None)**  
  Identifies outliers in specified columns using the IQR method.

- **find_columns_with_missing_value(df, threshold=0.05)**  
  Returns columns with a proportion of missing values above the given threshold.

- **normalize_date(df, date_col)**  
  Normalizes a date column to remove time information.

- **clean_data(df)**  
  Cleans and preprocesses the DataFrame by normalizing dates, dropping columns with excessive missing data, and more.

- **load_countries(paths)**  
  Loads and concatenates country data from a list of file paths.

- **load_country_data(path)**  
  Loads data from a file and adds a 'Country' column based on the file path.

- **drop_column(df, cols)**  
  Drops specified columns from a DataFrame.

- **convert_money_tofloat(value)**  
  Converts a monetary value to a float-compatible string, handling commas and NaNs.

---

## `plots.py`

This module provides plotting utilities for exploratory data analysis.

### Key Functions

- **plot_boxplot(df, cols)**  
  Plots boxplots for the specified numeric columns. If `cols` is empty, plots all columns.

- **plot_histogram(df, cols)**  
  Plots histograms for numeric columns and count plots for categorical columns. If `cols` is empty, plots all columns.

- **correlation_matrix(df, cols, name)**  
  Displays a heatmap of the correlation matrix for the specified columns.

---

## Usage

Import the functions you need in your analysis scripts or notebooks:

```python
from preprocess import (
    load_data, drop_column, find_columns_with_missing_value, find_outliers,
    find_and_replace_outliers_with_median, IQR_outlier, normalize_date, convert_money_tofloat
)
from plots import plot_boxplot, plot_histogram, correlation_matrix