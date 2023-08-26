import pandas as pd


s_data = [10, 20, 30, 40]
s_label = ['Apple', 'Banana', 'Orange', 'Kiwi']
pd_one = pd.Series(data= s_data, index=s_label)
print(pd_one['Kiwi'])

print('--------------------------Dictionary----------------------------')
# Dictionary to PD series

dict_data_series = { 'Apple': 10, 'Banana': 20, 'Orange':30, 'Kiwi': 40}

pd_two = pd.Series(data=dict_data_series)

print(pd_two)

print('--------------------------Series default index----------------------')

pd_three = pd.Series(data=s_label)
print(pd_three)