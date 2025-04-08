import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",")

X = df.values[:,:-1]
print(type(X))
print(X)

Y = df.values[:,:-1]
print(Y)

fit = LinearRegression().fit(X,Y)

m = fit.coef_.flatten()
b = fit.intercept_.flatten()
print(f"m = {m}")
print(f"b = {b}")

plt.plot(X,Y, "+")
plt.plot(X, m*X+b)
plt.show()