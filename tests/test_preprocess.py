import pytest
import pandas as pd
from unittest.mock import patch
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))
from preprocess import drop_column, convert_money_tofloat, normalize_date, find_columns_with_missing_value, find_outliers

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'Timestamp': ['2024-01-01', '2024-01-02'],
        'Value': [1, 2]
    })
def test_drop_column(sample_df):
    df = sample_df.copy()
    result = drop_column(df, ['Value'])
    assert 'Value' not in result.columns
    assert 'Timestamp' in result.columns
def test_convert_money_tofloat():
    assert convert_money_tofloat('1,234.56') == '1234.56'
    assert convert_money_tofloat('nan') == '0.0'
    assert convert_money_tofloat(1234.56) == '1234.56'
    assert convert_money_tofloat(None) == '0.0'
def test_normalize_date():
    df = pd.DataFrame({'date': ['2024-01-01 12:34:56', '2024-01-02 23:59:59']})
    result = normalize_date(df.copy(), 'date')
    assert pd.api.types.is_datetime64_any_dtype(result['date'])
    assert all(result['date'].dt.hour == 0)
    assert all(result['date'].dt.minute == 0)
    assert all(result['date'].dt.second == 0)
def test_find_columns_with_missing_value():
    df = pd.DataFrame({
        'a': [1, None, 3, None],
        'b': [1, 2, 3, 4],
        'c': [None, None, None, None]
    })
    # threshold is 0.5 (50%), so only 'c' should be returned
    result = find_columns_with_missing_value(df, threshold=0.5)
    print(result)
    assert 'c' in result
    assert 'a' in result
    assert 'b' not in result
def test_find_outliers():
    df = pd.DataFrame({
        'x': [1, 2, 3, 100],  # 100 is an outlier
        'y': [10, 10, 10, 10],  # no outlier
        'z': ['a', 'b', 'c', 'd']  # non-numeric
    })
    cols = find_outliers(df, threshold=1)
    assert 'x' in cols
    assert 'y' not in cols
    assert 'z' not in cols

