import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
def plot_boxplot(df:pd.DataFrame, cols:list[str]):
    if len(cols) == 0:
        cols = df.columns
    for col in cols:
        if pd.api.types.is_numeric_dtype(df[col]):
            plt.boxplot(df['SumInsured'])
            plt.figure(figsize=(10,7))
            plt.show()

def plot_histogram(df:pd.DataFrame,cols:list[str]):
    i = 0
    if len(cols) == 0:
        cols = df.columns
    plt.figure(figsize=(18, 15))
    for col in cols:
        if pd.api.types.is_numeric_dtype(df[col]):
            
            sns.histplot(df[col], kde=True, bins=30) # dropna() to handle missing values
            plt.title(f'Distribution of {col}', fontsize=10)
            plt.xlabel(col, fontsize=8)
            plt.ylabel('Frequency', fontsize=8)
            plt.tick_params(axis='both', which='major', labelsize=7)
        else:
            # Use value_counts() to get counts for each category
            sns.countplot(data=df, x=col, order=df[col].value_counts().index, palette='viridis', hue=col)
            plt.title(f'Counts of {col}', fontsize=10)
            plt.xlabel(col, fontsize=8)
            plt.ylabel('Count', fontsize=8)
            plt.xticks(rotation=45, ha='right', fontsize=7)
            plt.tick_params(axis='y', which='major', labelsize=7)
        plt.show()
        i=+1
   


