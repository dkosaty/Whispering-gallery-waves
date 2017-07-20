# the solution of the whispering gallery equation


import matplotlib.pyplot as plt
from airy_funcs import *
from Y import *
import script_2
import script_3


class FAnother(script_2.F):
    def initialize_consts(self):
        self.N = 160

        self.p = 1

        self.p_prime = 1 - self.p ** 3

        Lambda = 0.1
        # Lambda = 10
        # Lambda = 1

        k0 = script_3.compute_k0(Lambda)

        m = script_3.compute_m(k0)

        # N0 = 1e-6
        N0 = 5 * 1e-6

        h = 50

        self.y0 = Y0(m, self.p, N0)

        self.y2 = Y2(k0, h, m, self.p)

        self.y1 = Y1(self.y0.wave_2, self.y2.wave_2)

    def get_roots(self):
        all_roots = np.roots(self.coefficients)

        # for root in all_roots:
        #     print(root, np.abs(self.model(root)))

        return self.sample_roots(all_roots, eps=0.7)

    roots = property(get_roots)

    def W(self, i, t=0):
        t_1 = self.p ** 2 * t - self.y2.wave_1
        t_2 = t - self.y1.wave_2

        if i == 1:
            return w(t_1) * v(t_2)
        elif i == 2:
            return dw(t_1) * v(t_2)
        elif i == 3:
            return w(t_1) * dv(t_2)
        elif i == 4:
            return dw(t_1) * dv(t_2)
        else:
            raise IndexError


def display(roots):
    x = np.real(roots)
    y = np.imag(roots)
    plt.plot(x, y, '.')
    plt.show()


if __name__ == '__main__':
    f = FAnother()

    print(f.roots)

    display(f.roots)
