import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

melbourne_data = pd.read_csv('melb_data.csv') 
melbourne_data = melbourne_data.dropna(axis=0)

y = melbourne_data.Price

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

melbourne_model = DecisionTreeRegressor(random_state=1)
melbourne_model.fit(X, y)

predicted_home_prices = melbourne_model.predict(X)
print(mean_absolute_error(y, predicted_home_prices))

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

melbourne_model = DecisionTreeRegressor()
melbourne_model.fit(train_X, train_y)

val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))


