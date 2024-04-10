from data_extraction import data_extraction

def data_analysis():
    data = data_extraction()
    print(data.info())
    print(data.describe())
    print(data.columns)
    print(data.shape)
    print(data.head())
    print(data.tail())
    print(data.isnull().sum())
    for col in data.columns:
        print(col, data[col].nunique())
    return data

data_analysis()