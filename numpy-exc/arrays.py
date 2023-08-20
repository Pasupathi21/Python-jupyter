import numpy as np


# Arrrayb creation
# List to Array
list_data = [123, 234, 3456, 3456, 34567,234567, 234568, 2345]

print(list_data)
np_array = np.array(list_data)
print(np_array)


print('-------------------- two dimensonal array-------------------')
np_arange = np.arange(0, 100).reshape(10, 10)
print(np_arange)

print('-------------------- Access two dimensonal array ( 55 - 99 )-------------------')

print(np_arange[5: , 5: ])

