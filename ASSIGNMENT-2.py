import pandas as pd
import numpy as np
df=pd.read_csv("Placement_Data_Full_Class.csv")
df['status']=df['status'].map({'Placed':1,'Not Placed':0})
corr=df.corr(method='kendall')
import seaborn as sns
import matplotlib
matplotlib.rcParams['figure.figsize']=[20,10]
sns.heatmap(corr,
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values,
            cmap="YlGnBu",
            annot=True)
