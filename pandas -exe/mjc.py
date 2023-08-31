# '''
# M- MERGE
# J- JOIN
# C- CONCATE
# '''


import pandas as pd
import numpy as np


print('-------------------- JOIN ---------------------')

d_one = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}

d_two = {
    'D': [12, 13, 14, 15],
    'E': [15, 16, 17, 18],
    'F': [18, 19, 20, 21]
}

df_one = pd.DataFrame(data=d_one)

df_two = pd.DataFrame(data=d_two)

# print(df_one)

# Combaine two data

c_data = pd.concat([df_one, df_two], axis=1)
print(c_data)