import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import linalg
data = pd.read_csv('New_York_State_Statewide_COVID-19_Testing.csv',
        dtype={
            'New Positives': 'int',
            'Cumulative Number of Positives': 'int',
            'Total Number of Tests Performed': 'int',
            'Cumulative Number of Tests Performed': 'int'}, parse_dates=['Test Date'], thousands=',')
def matrify(data):
    data = list(data)
    X = []
    for i in range(14, len(data)):
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
        Y += [y for y in df['New Positives'][14:]]
    X = np.array(X)
    Y = np.array(Y)
    W = linalg.lstsq(X, Y)[0]
    return W

def predict(W, county):
    true = list(data[data['County'] == county]['New Positives'])[14:]
    county_data = matrify(data[data['County'] == county]['New Positives'])
    pred = np.array(county_data @ W)[0]
    index = data[data['County'] == county]['Test Date'][14:]
    predicted, = plt.plot(index, pred, 'r', label='Predicted New Positives')
    actual, = plt.plot(index, true, 'g', label='Actual New Positives')
    plt.xlabel('Date')
    plt.ylabel('New Positives per Day')
    plt.legend(handles=[predicted, actual])
    plt.title('History of New Positives with Prediction')
    plt.savefig("./diff.png")
    plt.close()

def predict_future(W, county):
    future = list(data[data['County'] == county]['New Positives'])[-14:]
    for _ in range(7):
        future.append(([1] + future[-14:]) @ W)
    last_date = data['Test Date'].max()
    index = [pd.DateOffset(x) + last_date for x in range(1, 8)]
    index = [str(x.month) + '-' + str(x.day) for x in index]
    plt.plot(index, future[-7:])
    plt.xlabel('Date')
    plt.ylabel('Predicted New Positives per Day')
    plt.title('Future Prediction of New Positives')
    plt.savefig("./predict.png")
    plt.close()

def get_county():
    county_list = data['County'].unique()
    return county_list

def predi_covid(county):
    W = lin_reg()
    predict(W, county)
    predict_future(W, county)
