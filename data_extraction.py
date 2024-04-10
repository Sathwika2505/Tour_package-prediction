import pandas as pd

def data_extraction():
    df = pd.read_csv(r"C:\Users\SathwikaGopishetty\Downloads\archive (18)\tour_package.csv")
    print(df.head)
    return df

data_extraction()