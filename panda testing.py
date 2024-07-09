import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Indexing and filtering

df = pd.read_csv(r"C:\Users\basil\OneDrive\Documents\Basil Rehan Siddiqui\Other\Datasets\world_population.csv")
pd.set_option('display.max_columns',5)
pd.set_option('display.max_rows',235)

specific_countries = ['Bangladesh', 'Brazil']
df2 = df.set_index('Country')

df[df['Rank'] < 10].sort_values(by=['Rank'], ascending= False)
df.set_index(['Continent','Country'], inplace= True)
df.sort_index(ascending= True)
df.loc['Asia','Pakistan']

#Groupby and aggregate fucntions

df2 = pd.read_csv(r'C:\Users\basil\OneDrive\Documents\Basil Rehan Siddiqui\Other\Datasets\Flavors.csv')
pd.set_option('display.max_columns',6)

grouped_frame = df2.groupby('Base Flavor')
grouped_frame.mean()
grouped_frame.count()
grouped_frame.agg({'Flavor Rating': ['min', 'mean', 'max', 'count'],'Texture Rating': ['min', 'mean', 'max', 'count']})
df2.groupby(['Base Flavor', "Liked"]).agg({'Flavor Rating': ['min', 'mean', 'max', 'count']})
df2.groupby('Base Flavor').describe() #All the numerical analysis

#Merge, join and concatenate

df3 = pd.read_csv(r'C:\Users\basil\OneDrive\Documents\Basil Rehan Siddiqui\Other\Datasets\LOTR.csv')

df4 = pd.read_csv(r'C:\Users\basil\OneDrive\Documents\Basil Rehan Siddiqui\Other\Datasets\LOTR 2.csv')

df3.merge(df4, how = 'right')

#Visualization

df5 = pd.read_csv(r'C:\Users\basil\OneDrive\Documents\Basil Rehan Siddiqui\Other\Datasets\Ice Cream Ratings.csv')
df5.set_index('Date')
df5

plt.style.use('dark_background')

df5.plot(kind = 'line', subplots = True, title = 'Ice cream ratings', xlabel = 'Daily rating', ylabel = 'Scores')
df5.plot(kind = 'barh', stacked = True, xlabel= 'Scores')
df5.plot(kind = 'scatter',x = 'Texture Rating', y = 'Overall Rating', s = 500, c = 'green')
df5.plot(kind = 'hist', bins = 20)
df5.boxplot()
df5.plot( kind = 'area', figsize = (10,5))
df5.plot.pie(y = 'Overall Rating')
