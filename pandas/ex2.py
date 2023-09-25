import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)

print(reviews.country)
print(reviews.iloc[0]) #first row
print(reviews.iloc[:, 0]) #first column
print(reviews.iloc[:3, 0]) #first 3 rows
print(reviews.iloc[1:3, 0]) #second and third
print(reviews.iloc[[0, 1, 2], 0])
print(reviews.iloc[-5:]) #last five
print(reviews.loc[0, 'country'])
print(reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']])

reviews.set_index("title")

print(reviews.loc[reviews.country == 'Italy'])
print(reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)])
print(reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)])

print(reviews.loc[reviews.country.isin(['Italy', 'France'])])
print(reviews.loc[reviews.price.notnull()])

reviews['critic'] = 'everyone'
print(reviews['critic'])

reviews['index_backwards'] = range(len(reviews), 0, -1)
print(reviews['index_backwards'])