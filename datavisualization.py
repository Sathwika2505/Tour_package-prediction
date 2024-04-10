from data_preprocessing import preprocessing
import pandas as pd
import plotly.express as px
from IPython.display import Image
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.io as pio
from sklearn.utils import column_or_1d
from scipy import stats
from sklearn.preprocessing import LabelEncoder
a =[]

def remove_outliers_zscore(data, threshold=3):
    z_scores = stats.zscore(data)
    abs_z_scores = np.abs(z_scores)
    filtered_entries = (abs_z_scores < threshold).all(axis=1)
    data_without_outliers = data[filtered_entries]
    return data_without_outliers

def data_visualization():
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
    data.drop(['TypeofContact', 'Age', 'Gender', 'Designation'], axis=1,inplace=True)
    data = remove_outliers_zscore(data)
    col=list(data.columns)
    col.remove("ProdTaken")
    print(col)
    for i in col:
        fig = px.box(data, y=i)
        fig.update_layout(template='plotly_dark')
        #fig.update_layout(plot_bgcolor = "plotly_dark")
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        # fig.show()
        fig.write_image(f"{i}.jpg")
        # a.append(fig)
    # for i in col:
    #     fig = ff.create_distplot([data[i].values],group_labels=[i])
    #     fig.update_layout(template='plotly_dark')
    #     #fig.update_layout(plot_bgcolor = "plotly_dark")
    #     fig.update_xaxes(showgrid=False,zeroline=False)
    #     fig.update_yaxes(showgrid=False,zeroline=False)
        # fig.show()
        # a.append(fig)
    df=data.drop("ProdTaken",axis=1)
    y=df.corr().columns.tolist()
    z=df.corr().values.tolist()
    z_text = np.around(z, decimals=4) # Only show rounded value (full value on hover)
    fig = ff.create_annotated_heatmap(z,x=y,y=y,annotation_text=z_text,colorscale=px.colors.sequential.Cividis_r,showscale=True)
    fig.update_layout(template='plotly_dark')
    # fig.show()
    fig.write_image("img.jpg")
    # a.append(fig)
    
    return data

data_visualization()