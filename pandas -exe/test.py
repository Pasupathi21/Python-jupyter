import pandas as pd
import numpy as np
import random


# random seed function repeats the same values  
np_list_rand = []
py_list_rand = []
for n in range(10):
    np.random.seed()
    np_list_rand.append(np.random.randint(1, 100))
    random.seed(0)
    py_list_rand.append(random.randint(1, 100))

print('Py', py_list_rand)
print('Np', np_list_rand)


print('---------------- Two dimentional array -------------')
np_two = np.random.rand(10, 10)

all_data = []
for n in np_two:
    for m in n:
        all_data.append(m)
print(all_data)
print(all_data.reverse())
