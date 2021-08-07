import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import linalg
data = pd.read_csv('processed.csv',
        dtype={
            'New Positives': 'int',
            'Cumulative Number of Positives': 'int',
            'Total Number of Tests Performed': 'int',
            'Cumulative Number of Tests Performed': 'int'}, parse_dates=['Test Date'])
def matrify(data):
    data = list(data)
    X = []
    for i in range(28,len(data)):
        row = [1] + data[i - 14:i]
        X.append(row)
    X = np.matrix(X)
    return X

def lin_reg():
    X = None
    Y = []
    for _, df in data.groupby('County'):
        if X is None:
            X = matrify(df['New Positives'])
        else:
            X = np.append(X, matrify(df['New Positives']), 0)
        Y += [y for y in df['New Positives'][28:]]
    X = np.array(X)
    Y = np.array(Y)
    # Y = np.matrix(Y)
    # Xi = np.linalg.inv((np.transpose(X)@X))@(np.transpose(X))
    # W = Xi@Y
    W = linalg.lstsq(X, Y)[0]
    return W

def predict(W, county):
    true = list(data[data['County'] == county]['New Positives'])[28:]
    county_data = matrify(data[data['County'] == county]['New Positives'])
    pred = np.array(county_data @ W)[0]
    index = data[data['County'] == county]['Test Date'][28:]
    plt.plot(index, pred, 'r')
    plt.plot(index, true, 'g')
    plt.savefig("./diff.png")
    plt.close()

def predict_future(W, county):
    future = list(data[data['County'] == county]['New Positives'])[-14:]
    for _ in range(7):
        future.append(([1] + future[-14:]) @ W)
    plt.plot(range(7), future[-7:])
    plt.savefig("./predict.png")
    plt.close()

def get_county():
    county_list = data['County'].unique()
    return county_list

def predi_covid(county):
    data = pd.read_csv('processed.csv',
        dtype={
            'New Positives': 'int',
            'Cumulative Number of Positives': 'int',
            'Total Number of Tests Performed': 'int',
            'Cumulative Number of Tests Performed': 'int'}, parse_dates=['Test Date'])
    W = lin_reg()
    predict(W, county)
    predict_future(W, county)
