import numpy as np
import matplotlib.pyplot as plt
from script_3 import F


def display(roots):
    [print(root) for root in roots]

    x = np.real(roots)
    y = np.imag(roots)
    plt.plot(x, y, '.')
    plt.show()


if __name__ == '__main__':
    PQ = F()
    roots = PQ.roots

    print(roots)
    # display(roots)
