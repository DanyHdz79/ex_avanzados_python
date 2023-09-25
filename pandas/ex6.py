import pandas as pd

pd.set_option('display.max_rows', 5)
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

print(reviews.rename(columns={'points': 'score'}))

print(reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'}))

print(reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns'))

canadian_youtube = pd.read_csv("CAvideos.csv")
british_youtube = pd.read_csv("GBvideos.csv")

print(pd.concat([canadian_youtube, british_youtube]))

left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

print(left.join(right, lsuffix='_CAN', rsuffix='_UK'))