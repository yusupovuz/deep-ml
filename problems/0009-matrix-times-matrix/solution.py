import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    a = np.array(a)
    b = np.array(b)
    if a[0].shape != b[0].shape:
        return -1
    c = a.dot(b)
    return c