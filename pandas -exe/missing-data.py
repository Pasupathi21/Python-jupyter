import pandas as pd
import numpy as np

# print(None)
# print(__name__ == '__main___')
# def loop(value):
#     return value * 10
# # help()

# new_list = map(loop, [1,2, 3, 4])
# print(list(new_list))
dict_for_missing_data = {
    'Col 1': [
        23456,
        234567,
        34567
    ],
    'Col 2':[
        None,
        None,
        23456789765
    ],
    'Col 3': [
        None,
        234567,
        2345678
    ]
}

df = pd.DataFrame(dict_for_missing_data)
print('----------------DF fill value ----------------------')
print(df.fillna(0))
print('--------------------- drop value axis based row or column wise----------------------')
print(df.dropna(axis=0))
