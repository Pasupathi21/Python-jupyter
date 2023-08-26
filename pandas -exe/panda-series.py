import pandas as pd

print('----------------------- one------------------------')
s_data = [10, 20, 30, 40]
s_label = ['Apple', 'Banana', 'Orange', 'Kiwi']
pd_one = pd.Series(data= s_data, index=s_label)
print(pd_one)

print('--------------------------Dictionary----------------------------')
# Dictionary to PD series

dict_data_series = { 'Apple': 10, 'Banana': 20, 'Orange':30, 'Kiwi': 40}

pd_two = pd.Series(data=dict_data_series)

print(pd_two)

print('--------------------------Series default index----------------------')

pd_three = pd.Series(data=s_label)
print(pd_three)


print('---------------------------------Addition operation of two series-----------------------------------------------')

pd_addition = pd_one + pd_two
print(pd_addition)

print('-------------------Addtion with different data series------------------------')
print(pd_three + pd_two)