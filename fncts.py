import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def box_plots(df, col, title):
    '''Function reads the dataframe and returns a boxplot of a column.
    
        ARGS:
        df: dataframe
        col: column to plot
        title: title of the plot
    '''
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=col, data=df)
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