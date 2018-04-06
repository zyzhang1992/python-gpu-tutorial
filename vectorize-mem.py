import numpy as np
from numba import vectorize

@vectorize(['int64(int64, int64)'], target='cuda')
def add_ufunc(x, y):
    return x + y

n = 100000
a = np.arange(n).astype(np.float32)
b = 2 * a

print(a)
print(b)
print('a+b:\n', add_ufunc(a, b))
print()
