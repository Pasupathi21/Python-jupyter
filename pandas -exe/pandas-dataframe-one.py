import pandas as pd
import numpy as np
import random

pd_one = np.random.randn(5, 5)
# print(pd_one)
pd_row_index = ['A','S', 'D', 'F', 'G']
pd_column_index = ['Q', 'W', 'E', 'R', 'T']
f_one =pd.DataFrame(pd_one, pd_row_index, pd_column_index)
# print(f_one[['E', 'R']])


print('--------------Drop --------')
print(f_one.drop('D',axis=0, inplace=False))
# axis=0 --> row, axis=1 --> column inplace = True will hard delete the items from DataFrame

print('-------------------- Original after drop ---------')
print(f_one)
# print(f_one['new value'] = f_one['Q'] + f_one['T'])


# Row selection 
print('Type one label Row D', f_one.loc['D'])
print('Type two index Row D ', f_one.iloc[2])

print('--------------- Access X and Y axies value and set of values -------------')

print(' A and E point value', f_one.loc['A', 'E'])

print('Multiple row and column value eg: D,F and E,R,T')

print(f_one.loc[ ['D', 'F'], ['E', 'R', 'T']])