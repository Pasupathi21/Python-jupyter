import pandas as pd
import numpy as np

tech = [
    'FE',
    'API',
    'BE',
    'FE',
    'API',
    'BE',
    'FE',
    'API',
    'BE'
]

framework = [
  'React Js',
  'Node Js',
  'SQL',
  'Angular',
  'Python',
  'MongoDB',
  'Vue Js',
  'Java',
  'Oracle'
]

country = [
    'USA',
    'UK',
    'IND',
    'UAE'
]

# ratings = np.random.randint(1, 5)
data_list = []
for out_s in range(9):
    in_list = []
    for in_s in range(4):
        in_list.append(np.random.randint(1000, 5000))        
    data_list.append(in_list)
print('data list', data_list)
    
# print(ratings)
multi_index = pd.MultiIndex.from_tuples(list(zip(tech, framework)))
tech_df = pd.DataFrame(data_list, multi_index, country)
print(tech_df)

print('--------------retrive specific outside index ------------')
print(tech_df.loc['FE'])

print('Name multi index')

tech_df.index.names = ['Tech', 'Frameworks'] 
print(tech_df)

print('-----------------Cross access pick by the Named index xs(index, level= olumn Name of the index )----------------')
print(tech_df.xs('BE', level="Tech"))