import pandas as pd
import numpy as np


np_random_series = np.random.randn(5, 5)

# print(np_random_series)
df_one = pd.DataFrame(np_random_series, ['Q', 'W', 'E', 'R', 'T'], ['A', 'S', 'D', 'F', 'G'])

print(df_one)

print('-----------------------Conditional based column and row selection--------------')

less_zero = df_one < 0
print('---------------- Return Boolean DataFrame --------------')
print(less_zero)

print('----------------Actual DataFrame---------------------')
print(df_one[less_zero])

print('--------------Chaining selection ---------------------')
chaining_selection = df_one[less_zero].loc[['Q','E', 'T'], ['A', 'D', 'G']]
print(chaining_selection)


print('------------------Logical operator with number --------------')
print(df_one[(df_one.loc['R'] < 0) | (df_one['G'] > 1)])


print('--------------Index reset for DataFrame ------------')
print(df_one.reset_index())

print('---------------------- New column added ---------------')

df_one['K'] = [1, 2, 3, 4, 5]
print(df_one)

print('---------------New column set to index ---------------------')\

print(df_one.set_index('K'))