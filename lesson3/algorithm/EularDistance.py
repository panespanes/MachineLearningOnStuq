import numpy as np


def distance(va, vb):
    vc = va - vb
    power = np.power(vc, 2)
    sum = np.sum(power)
    return np.sqrt(sum)
