import pandas as pd
import matplotlib.pyplot as plt
import os.path

<<<<<<< HEAD
data = pd.read_csv('New_York_State_Statewide_COVID-19_Testing.csv', 
    dtype={
        'New Positives': 'int',
        'Cumulative Number of Positives': 'int',
        'Total Number of Tests Performed': 'int',
        'Cumulative Number of Tests Performed': 'int'}, parse_dates=['Test Date'], thousands=',')
data['Positive Rate'] = data['New Positives'] / data['Total Number of Tests Performed']
for i in range(data.shape[0]):
    row = data.iloc[i]
    if row['Test Date'] >= pd.to_datetime('2020-03-07'):
        positives = [data.iloc[i - x]['New Positives'] for x in range(7)]
        data.loc[i, '7-day Average Positives'] = sum(positives) // 7
        test_rates = [data.iloc[i - x]['Positive Rate'] for x in range(7)]
        data.loc[i, '7-day Average Test Rate'] = sum(test_rates) / 7
    if row['Test Date'] >= pd.to_datetime('2020-03-14'):
        positives = [data.iloc[i - x]['New Positives'] for x in range(7)]
        data.loc[i, '7-day Average Positives'] = sum(positives) // 14
        test_rates = [data.iloc[i - x]['Positive Rate'] for x in range(7)]
        data.loc[i, '7-day Average Test Rate'] = sum(test_rates) / 14
# print(data)
data.to_csv('processed.csv')
=======

if (not os.path.isfile('testing.csv')):
    data = pd.read_csv('New_York_State_Statewide_COVID-19_Testing.csv')
    for i in range(data.shape[0]):
        row = data.iloc[i]
        if row['Test Date'][-1:] != '0' or row['Test Date'][:2] != '03' or row['Test Date'][3:5] >= '07':
            positives = [int(data.iloc[i - x]['New Positives'].replace(',', '')) for x in range(7)]
            data.loc[i, '7-day Average'] = int(sum(positives) / 7)
    data.to_csv('testing.csv')
else:
    data = pd.read_csv('testing.csv')
print(data[data['County'] == 'Albany'])
>>>>>>> 12da158b59bfc6bde0ca8c59ee5b9362497d599a
