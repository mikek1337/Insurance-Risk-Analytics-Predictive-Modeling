import pandas as pd

DATA_FOLDER = '../data'

def load_data(filename):
    return pd.read_csv(f'{DATA_FOLDER}/{filename}', delimiter='|')

