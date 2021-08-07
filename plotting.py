import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import linalg

def matrify(county_data):
    county_data = list(county_data)
    X = []
    for i in range(28,len(county_data)):
        row = [1] + county_data[i - 14:i]
        X.append(row)
    X = np.matrix(X)
    return X

def lin_reg(county_data):
    X = None
    Y = []
    for _, df in data.groupby('County'):
        if X is None:
            X = matrify(df['14-day Average Positives'])
        else:
            X = np.append(X, matrify(df['14-day Average Positives']), 0)
        Y += [y for y in df['14-day Average Positives'][28:]]
    X = np.array(X)
    Y = np.array(Y)
    # Y = np.matrix(Y)
    # Xi = np.linalg.inv((np.transpose(X)@X))@(np.transpose(X))
    # W = Xi@Y
    W = linalg.lstsq(X, Y)[0]
    return W

def predict(W, county):
    true = list(data[data['County'] == county]['14-day Average Positives'])[28:]
    county_data = matrify(data[data['County'] == county]['14-day Average Positives'])
    pred = np.array(county_data @ W)[0]
    index = data[data['County'] == county]['Test Date'][28:]
    plt.plot(index, pred)
    plt.plot(index, true)
    plt.show()
    diff = np.array(true) - pred
    plt.plot(index, diff)
    plt.show()
    error = np.linalg.norm(diff) / len(diff)
    print(error)

data = pd.read_csv('processed.csv',
    dtype={
        'New Positives': 'int',
        'Cumulative Number of Positives': 'int',
        'Total Number of Tests Performed': 'int',
        'Cumulative Number of Tests Performed': 'int'}, parse_dates=['Test Date'])
W = lin_reg(data)
print(W.shape)
predict(W, 'New York')
