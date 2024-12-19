import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#create box plots
def box_plots(df, col, title):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=col, data=df)
    plt.title(title)
    plt.show()

# create histograms
def hist_plots(df, col, title):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[col], bins=20, kde=True)
    plt.title(title)
    plt.show()

# create scatter plots
def scatter_plots(df, x, y, title):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x, y=y, data=df)
    plt.title(title)
    plt.show()
