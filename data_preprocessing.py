from data_analysis import data_analysis
import pandas as pd

def preprocessing():
    data = data_analysis()
    data = data.fillna(0)
    data.drop(['CustomerID'],axis=1,inplace=True)
    cat_cols = ['Designation','ProdTaken', 'OwnCar', 'Passport',
            'CityTier','MaritalStatus',
            'ProductPitched','Gender','Occupation','TypeofContact'
            ]
    for i in cat_cols:
        print('Unique values in',i, 'are :')
        print(data[i].value_counts())
        print('*'*50)
    data['Gender'] = data['Gender'].apply(lambda x: 'Female' if x == 'Fe Male' else x)
    data.Gender.value_counts()
    data[cat_cols] = data[cat_cols].astype('category')
    data['Agebin'] = pd.cut(data['Age'], bins = [18,25, 31, 40, 50, 65], labels = ['18-25','26-30', '31-40', '41-50', '51-65'])
    data['Incomebin'] = pd.cut(data['MonthlyIncome'], bins = [0,15000,20000, 25000, 30000,35000,40000,45000,50000,100000], labels = ['<15000', '<20000', '<25000', '<30000','<35000','<40000','<45000','<50000','<100000'])
    return data

preprocessing()