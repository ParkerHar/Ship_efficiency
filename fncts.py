import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def box_plots(df, col, title):
    '''Function reads the dataframe and returns a boxplot of a column.
    
        ARGS:
        df: dataframe
        col: column to plot
        title: title of the plot
    '''
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=col, data=df) #showfliers=False can be added for no outliers. Easier to see for skewed data.
    plt.title(title)
    plt.show()

def hist_plots(df, col, title):
    '''Function reads the dataframe and returns a histogram of a column.
    
        ARGS:
        df: dataframe
        col: column to plot
        title: title of the plot
    '''
    plt.figure(figsize=(10, 6))
    sns.histplot(df[col], bins=20, kde=True)
    plt.title(title)
    plt.show()

def scatter_plots(df, x, y, title):
    '''Function reads the dataframe and returns a scatter plot of two columns.
    
        ARGS:
        df: dataframe
        x: x-axis column
        y: y-axis column
        title: title of the plot
    '''
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x, y=y, data=df)
    plt.title(title)
    plt.show()

def  geo_plots(df, lat, lon):
    '''Function reads the dataframe and returns a scatter plot of latitude and longitude.
    
        ARGS:
        df: dataframe
        lat: latitude column
        lon: longitude column
    '''

    p = px.scatter_geo(df, lat = 'latitude', lon = 'longitude')
    p.show()

def top_n(df, col, n):
    '''Function reads the dataframe and returns the top n values of a column.
    
        ARGS:
        df: dataframe
        col: column to get top n values
        n: number of top values to return
        
        Helper function to get a sense of the data
    '''
    return df.nlargest(n, col)

def data_info(df):
    '''Function reads the dataframe and returns the shape, columns, describe, nulls, and head of the dataframe.
    
        ARGS:
        df: dataframe
        
        Helper function to get a sense of the data
    '''
    print('DF SHAPE:','\n', df.shape)
    print('DF COLUMNS:','\n', df.columns)
    print('DF DESCRIBE:','\n', df.describe())
    print('DF NULLS:','\n',df.isnull().sum())
    print('DF HEAD:','\n',df.head())

def mean_median(df):
    '''Function reads the numeric columns of a dataframe and returns the mean and median of each column.
    
        ARGS:
        df: dataframe
        
        Helper function to get a sense of the data
    '''
    for col in df.select_dtypes(include='number').columns:
        print(f'{col} mean: {df[col].mean()}')
        print(f'{col} median: {df[col].median()}\n')

def drop_outliers(df, col):
    '''Function reads the dataframe and drops the outliers of a column.
    
        ARGS:
        df: dataframe
        col: column to drop outliers
        
        RETURNS:
        df: dataframe with outliers removed
    '''
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5*iqr
    upper_bound = q3 + 1.5*iqr
    df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]
    return df


def cat_buckets(df, col):
    '''Function reads in a column and stores the values as numbers based on which
    bucket they fall into.
    
        ARGS:
        df: dataframe
        col: column to bucket
        
        RETURNS:
        df: dataframe with new column
    '''
    df[col+'_bucket'] = pd.qcut(df[col], q=4, labels=False)
