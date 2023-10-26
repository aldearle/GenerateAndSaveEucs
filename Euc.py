import numpy as np
import math

def euc(query: np.array, data: np.array):
     distances = np.sqrt(np.sum(np.square((query - data)), axis=1))
     return distances

def euc_scalar(p1: np.array, p2: np.array):
    distances = math.sqrt(np.sum(np.square((p1 - p2))))
    return distances

