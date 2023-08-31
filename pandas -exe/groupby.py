import pandas as pd
import numpy as np

data = {
    'mobile': ['OPPO', 'VIVO', 'SAMSUNG', 'REDMI', 'SONY', 'APPLE', '1+', 'REDMI'],
    'ratings': [7, 6, 7, 5, 4, 8, 8, 4],
    'price': [18000, 24000, 30000, 150000, 60000, 55000, 31000, 10000]
}

df_one = pd.DataFrame(data=data)

print(df_one.groupby('ratings').sum())

print('---------------- overall describe -----------------')
print(df_one.groupby('mobile').describe().transpose())