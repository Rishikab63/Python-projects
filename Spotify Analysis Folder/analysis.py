# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:00:32 2024

@author: Rishika
"""

#libraries to import for analysis and visualization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  #seaborn is based on matplotlib

#dataset folder import
df= pd.read_csv("C:\\Users\\Rishika\\Desktop\\python project for resume\\spotify analysis\\SpotifyFeatures.csv")  
dfa=pd.read_csv("C:\\Users\\Rishika\\Desktop\\python project for resume\\spotify analysis\\artists.csv")
#print(dfa.head())

#null value. checking total null variable present in each column
pd.isnull(df).sum()
#data type and memory usage


df.info()

#least popular song
sorted_df = df.sort_values('popularity',ascending=True).head(10)

#descreptive statistics for numerical variable present, max, min...
df.describe().transpose()

#top 10 song with popularity greater than 90, inplace false since do not want to change the original dataframe,
#sorting in desc order
most_popular=df.query('popularity>90', inplace = False).sort_values('popularity', ascending=False)
most_popular[:10]

#index setting according to release date
df.set_index("time_signature", inplace=True)
df.index=pd.to_datetime(df.index)  #changing  to date time format
df.head()

#check artist in 18th row
df["artists"].iloc[18]

#converting duration in mllesec to sec
df["duration"]=df["duration_ms"].apply(lambda x:round(x/1000))
df.drop("duration_ms",inplace=True, axis=1)
df.duration.head()

#----------------------------------------------------------------------------------------------------------
#visualisation- corelation map
#dropping unwanted col key, mode, explicit and applying pearson method
corr_df=df.drop(["key","mode","genre"],axis=1).corr(method="pearson")
plt.figure(figsize=(14,6))
heatmap=sns.heatmap(corr_df,annot=True,fmt=".ig",vmin=1,center=0,cmap="inferno",linewidths=1,linecolor="black")
heatmap.set_title("correlation heatmap between variable")
heatmap.set_xticklabels(heatmap.get_xticklabels(),rotation=90)


#regression line plot b/w loudness and energy
plt.figure(figsize=(10,6))

sample_df=df.sample(int(0.004*len(df)))
sns.regplot(data=sample_df, y="loudness", x="energy", color="c").set(title="loudness vs energy correlation")


#another regression plot
#regression line plot b/w loudness and energy
plt.figure(figsize=(10,6))

sample_df=df.sample(int(0.004*len(df)))
sns.regplot(data=sample_df, y="popularity", x="acousticness", color="b").set(title="popularity vs acousticness correlation")


#bar plot for duration pf song for diff genres
plt.title("duration of song in different genres")
sns.color_palette("rocket", as_cmap=True)
sns.barplot(y='genre', x='duration_ms',data=df)
plt.xlabel("duration in ms")
plt.ylabel("genres")

    
