import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def matrify(county_data):
    county_data = list(county_data)
    X = []
    for i in range(28,len(county_data)):
        row = [1]
        for j in range(14):
            row.append(county_data[i-14+j])
        X.append(row)
    X = np.matrix(X)
    return X

def lin_reg(county_data):
    county_data = list(county_data)
    X = matrify(county_data)
    Y = []
    for i in range(28,len(county_data)):
        Y.append([county_data[i]])
    Y = np.matrix(Y)
    Xi = np.linalg.inv((np.transpose(X)@X))@(np.transpose(X))
    W = Xi@Y
    index = list(data[data['County']=='Saratoga']['Test Date'])[28:]
    predict = []
    M = matrify(data[data['County']=='Saratoga']['7-day Average Positives'])
    for i in range(28,len(county_data)):
        predict.append(np.array(M[i-28]@W)[0][0])
    plt.plot(index,predict)
    plt.show()
    print(W)

data = pd.read_csv('processed.csv',
    dtype={
        'New Positives': 'int',
        'Cumulative Number of Positives': 'int',
        'Total Number of Tests Performed': 'int',
        'Cumulative Number of Tests Performed': 'int'}, parse_dates=['Test Date'], thousands=',')
county = input('Enter the county\n')
xlabel = input('Enter the x axis\n')
ylabel = input('Enter the y axis\n')
county_data = data[data['County']==county][ylabel]
plt.plot(list(data[data['County']==county][xlabel]),county_data)
max_window = plt.get_current_fig_manager()
max_window.window.state('zoomed')
plt.show()
lin_reg(county_data)



