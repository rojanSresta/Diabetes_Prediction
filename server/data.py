import pandas as pd

def read_columns():
    df = pd.read_csv('s_diabetes.csv')
    columns_list = df.columns.tolist()
    columns_list.pop()
    return columns_list