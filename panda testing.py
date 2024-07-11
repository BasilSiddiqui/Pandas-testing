import pandas as pd
import numpy as np
import seaborn as sns
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
df5.plot(kind = 'area', figsize = (10,5))
df5.plot.pie(y = 'Overall Rating')

#Data cleaning

df6 = pd.read_excel(r'C:\Users\basil\OneDrive\Documents\Basil Rehan Siddiqui\Other\Datasets\Customer Call List.xlsx')
df6 = df6.set_index('CustomerID')
df6 = df6.drop_duplicates()
df6 = df6.drop(columns = 'Not_Useful_Column')
df6['Last_Name'] = df6['Last_Name'].str.strip('123._/')
df6['Last_Name'] = df6['Last_Name'].str.strip()
df6['Phone_Number'] = df6['Phone_Number'].str.replace('[^a-zA-Z0-9]','')
df6['Phone_Number'] = df6['Phone_Number'].str.strip()

def format_phone_number(number):
    number = str(number)
    if len(number) == 10:
        return f"{number[:3]}-{number[3:6]}-{number[6:]}"
    return number  # Return as is if not 10 digits (handle unexpected cases)

df6['Phone_Number'] = df6['Phone_Number'].apply(format_phone_number)
df6['Phone_Number'] = df6['Phone_Number'].replace('nan','')
df6['Phone_Number'] = df6['Phone_Number'].replace('Na','')
df6[['Street', 'State', 'Zipcode']] = df6['Address'].str.split(',',2, expand = True)
df6['Paying Customer'] = df6['Paying Customer'].replace('Y','Yes')
df6['Paying Customer'] = df6['Paying Customer'].replace('N','No')
df6['Do_Not_Contact'] = df6['Do_Not_Contact'].replace('Y','Yes')
df6['Do_Not_Contact'] = df6['Do_Not_Contact'].replace('N','No')
df6['Do_Not_Contact'] = df6['Do_Not_Contact'].replace('','No')
df6 = df6.drop(columns = 'Address')
df6 = df6.replace('N/a', '')
df6 = df6.fillna('')

for x in df6.index:
    if df6.loc[x, 'Do_Not_Contact'] == 'Yes':
        df6.drop(x, inplace = True)
        
for x in df6.index:
    if df6.loc[x, 'Phone_Number'] == '':
        df6.drop(x, inplace = True)
        
df6

#Exploratory data analysis

df7 = pd.read_csv(r'C:\Users\basil\OneDrive\Documents\Basil Rehan Siddiqui\Other\Datasets\world_population (1).csv')
pd.set_option('display.float_format', '{:.2f}'.format)

test1 = df7.describe()

test2 = df7.isnull().sum()
test3 = df7.nunique()

test4 = df7.sort_values(by = '2022 Population', ascending= False).head()

test5 = df.corr()

sns.heatmap(df7.corr(), annot = True)
plt.rcParams['figure.figsize'] = (20,7)
plt.show()

test6 = df7[df7['Continent'] == 'Oceania']
test7 = df7.groupby('Continent')['1970 Population','1980 Population', '1990 Population', '2000 Population','2010 Population', '2015 Population', '2020 Population','2022 Population'].mean().sort_values(by = '2022 Population', ascending = False)
test8 = test7.transpose()

test8.plot()

df7.boxplot()
test9 = df7.select_dtypes(include = 'float')

#That was fun