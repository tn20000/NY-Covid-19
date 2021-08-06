import pandas as pd

data = pd.read_csv('New_York_State_Statewide_COVID-19_Testing.csv')
for i in range(data.shape[0]):
    row = data.iloc[i]
    if row['Test Date'][-1:] != '0' or row['Test Date'][:2] != '03' or row['Test Date'][3:5] >= '07':
        positives = [int(data.iloc[i - x]['New Positives'].replace(',', '')) for x in range(7)]
        data.loc[i, '7-day Average'] = int(sum(positives) / 7)
print(data[data['County'] == 'Albany'])