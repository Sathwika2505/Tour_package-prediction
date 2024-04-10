from data_preprocessing import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import column_or_1d
def feature_engineering():
    data = preprocessing()
    categorical_vars = []
    numerical_vars = []
    labelencoder = LabelEncoder()
    for column in data.columns:
        if data[column].dtype == 'object' or data[column].dtype.name == 'category':
            categorical_vars.append(column)
        else:
            numerical_vars.append(column)
    for column in categorical_vars:
        data[column] = column_or_1d(data[column]).astype(str)
        labelencoder = LabelEncoder()
        data[column] = labelencoder.fit_transform(data[column])

    data.to_csv('Travel_package_purchase_prediction.csv', index=False)

    print(data.dtypes)

    return data
feature_engineering()