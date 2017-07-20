# the test of the Fock equation


import numpy as np
from Y import Y0
import script_1


class FAnother(script_1.F):
    def initialize_consts(self):
        self.N = 100

        self.q = 10 ** 6

        self.y0 = Y0()


if __name__ == '__main__':
    obj = FAnother()

    modules = np.abs(obj.roots)

    print(modules)
