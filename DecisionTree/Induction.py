'''
Model : Decision Tree
Algorithm : Induction
'''

import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def shuffle(data):
    length = len(data)
    new_list = []
    for _ in range(length):
        random_index = math.floor(random.random() * length)
        new_list.append(data.pop(random_index))
        length -= 1
    return new_list

dataset = [[True, False, True, 'A']] * 100
dataset += [[True, True, True, 'B']] * 150
dataset += [[True, True, False, 'A']] * 50
dataset = shuffle(dataset)

df = pd.DataFrame(dataset, columns=['x1', 'x2', 'x3', 'y'])
print(df)

