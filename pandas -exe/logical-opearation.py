import pandas as pd
import numpy as np

characters = [
    ['Captain', 'Iron man', 'Thor'],
    ['Thanos', 'Dark side', 'Wolf'],
    ['Spider man', 'Bat Man', 'Super Man'],
    ['Wonder women', 'Balck widow', 'Cat women'],
    ['Dr Strange', 'Black panther', 'Hulk']
]

df = pd.DataFrame(characters, [1, 2, 3, 4, 5], [1, 2, 3])
print(df)
print(df[(df.loc[[3]] == 'Spider man') | (df.loc[[3], [3]] == 'Super Man')])