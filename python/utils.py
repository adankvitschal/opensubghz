import numpy as np

def indexof(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

