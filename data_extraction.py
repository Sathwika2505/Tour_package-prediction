import pandas as pd

def data_extraction():
    df = pd.read_csv("tour_package.csv")
    print(df.head)
    return df

data_extraction()
