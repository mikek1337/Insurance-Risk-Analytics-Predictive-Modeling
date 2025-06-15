Collecting workspace information# Insurance Risk Analytics - Initial Data Analysis

This Jupyter notebook provides an initial exploratory data analysis and preprocessing workflow for the insurance risk analytics dataset. The goal is to clean, transform, and visualize the data to support predictive modeling and business insights.

## Contents

- **Data Loading:**  
  Reads the raw insurance data from a pipe-delimited text file into a pandas DataFrame.

- **Data Cleaning:**  
  - Drops columns with more than 70% missing data.
  - Normalizes date columns (`TransactionMonth`, `VehicleIntroDate`).
  - Converts monetary columns (e.g., `CapitalOutstanding`) to numeric types.
  - Fills missing values in categorical columns with `'Not specified'`.
  - Calculates derived features such as `VehicleAge`.

- **Missing Value Analysis:**  
  Identifies columns with missing values to guide further cleaning.

- **Outlier Detection and Handling:**  
  - Detects outliers in numerical columns using z-score.
  - Replaces outliers with the median value for robust analysis.

- **Visualization:**  
  - Box plots for numerical variables.
  - Histograms for categorical variables.
  - Scatter plots and correlation matrices for key metrics.
  - Bar plots, heatmaps, lollipop charts, and bubble plots to explore relationships between provinces, cover types, premiums, and vehicle makes.

## Usage

1. **Install dependencies:**  
   Make sure you have the required Python packages (see requirements.txt).

2. **Run the notebook:**  
   Open inital_analysis.ipynb in Jupyter or VS Code and execute the cells sequentially.

3. **Customize analysis:**  
   Modify the columns or visualizations as needed for your specific business questions.

## Key Functions Used

- `load_data`, `drop_column`, `find_columns_with_missing_value`, `find_outliers`, `find_and_replace_outliers_with_median`, `IQR_outlier`, `normalize_date`, `convert_money_tofloat` from `scripts/preprocess.py`
- `plot_boxplot`, `plot_histogram`, `correlation_matrix` from `scripts/plots.py`

## Output

The notebook produces:
- Cleaned and preprocessed DataFrame ready for modeling.
- Visual summaries of key variables and relationships.
- Insights into data quality, missing values, and outlier distributions.

---

**Note:**  
Update the data file path and column names as needed to match your dataset. For further analysis or modeling, use the cleaned DataFrame produced in this notebook.