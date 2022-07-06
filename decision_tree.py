import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import numpy as np

path = 'database.csv'
dataset = pd.read_csv(path)

y = dataset.Signal_Distortion.values
features = ['Duration']
X = dataset[features].values

regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X, y)

y_pred = regressor.predict(np.array([5]).reshape(-1,1))

X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Duration SDR Regression')
plt.xlabel('Duration')
plt.ylabel('SDR')
plt.show()
