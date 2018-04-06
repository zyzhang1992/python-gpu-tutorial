import numpy as np
from numba import vectorize

@vectorize(['int64(int64, int64)'], target='cuda')
def add_ufunc(x, y):
    return x + y

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print('a+b:\n', add_ufunc(a, b))
print()
print('b_col + c:\n', add_ufunc(b_col, c))
