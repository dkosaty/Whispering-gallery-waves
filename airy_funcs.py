from scipy.special import airy
import numpy as np


def u(t):
    return np.sqrt(np.pi) * airy(t)[2]
    # return airy(t)[2]


def du(t):
    return np.sqrt(np.pi) * airy(t)[3]
    # return airy(t)[3]


def v(t):
    return np.sqrt(np.pi) * airy(t)[0]
    # return airy(t)[0]


def dv(t):
    return np.sqrt(np.pi) * airy(t)[1]
    # return airy(t)[1]


def w(t, j=1):
    if j == 2:
        j = -1

    return complex(u(t), j * v(t))


def dw(t, j=1):
    if j == 2:
        j = -1

    return complex(du(t), j * dv(t))
