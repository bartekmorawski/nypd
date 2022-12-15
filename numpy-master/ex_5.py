import os
import numpy as np

#prints the list of numbers of objects (rows) in which the final size is at least twice the initial size
def double_size_rows(out):
    #in - 2-dim. array, out - list of numbers of rows in which last number is >= 2*first number
    doubles = []
    for i in range(out.shape[0]):
        if 2 * out[i][0] <= out[i][-1]:
            doubles += [i]
    return doubles

dane = np.load(os.path.join(os.getcwd(), 'data', 'sample_treated.npz'))
out = dane['outputs']
print(double_size_rows(out))