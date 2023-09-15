import numpy as np

def euc(query: np.array, data: np.array):
     distances = np.sqrt(np.sum(np.square((query - data)), axis=1))
     return distances

