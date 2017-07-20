import numpy as np
import matplotlib.pyplot as plt
from Y import *
import script_1
import script_2
import script_3


p = 1

Lambda = 1
# Lambda = 0.3

h = 100
# h = 200
# h = 300

k0 = script_3.compute_k0(Lambda)

m = script_3.compute_m(k0)

eps = script_3.eps
sigma = script_3.sigma

sigma_u = script_3.compute_sigmaU('e', eps, sigma, Lambda)

q = script_3.compute_q(m, sigma_u, p)

N0 = 1e-5
# N0 = 1e-6

y0 = Y0(m, p, N0)

y2 = Y2(k0, h, m, p)

y1 = Y1(y0.wave_2, y2.wave_2)

N = 160


class name_space_1:
    class F(script_1.F):
        def initialize_consts(self):
            self.N = N

            self.q = q

            self.p = p

            self.y0 = y0


class name_space_2:
    class F(script_2.F):
        def initialize_consts(self):
            self.N = N

            self.p = p

            self.p_prime = 1 - self.p ** 3

            self.y0 = y0

            self.y1 = y1

            self.y2 = y2


class FAnother(script_3.F):
    def initialize_consts(self):
        self.N = N

        self.p = p
        self.q = q

        self.y0 = y0
        self.y1 = y1
        self.y2 = y2

    def initialize_functions(self):
        self.f_1 = name_space_1.F(1)
        self.f_2 = name_space_1.F(2)
        self.f_11 = name_space_2.F(1, 1)
        self.f_12 = name_space_2.F(1, 2)
        self.f_21 = name_space_2.F(2, 1)
        self.f_22 = name_space_2.F(2, 2)

    def get_roots(self):
        all_roots = np.roots(self.coefficients)

        filtered_roots = list(filter((lambda x: np.imag(x) > 0), all_roots))

        for root in filtered_roots:
            discrepancy = np.abs(self.model(root))

            module = np.abs(root)

            print(root, discrepancy, module)

        self.min_discrepancy(filtered_roots)

        return self.sample_roots(all_roots)

    def min_discrepancy(self, filtered_roots):
        discrepances = [np.abs(self.model(root)) for root in filtered_roots]

        roots = dict(zip(discrepances, filtered_roots))

        min_root = roots[min(roots.keys())]

        print("min discrepancy=",min(roots.keys()), "root=",min_root, "module=",np.abs(min_root))

    roots = property(get_roots)

    # def get_roots(self):
    #     all_roots = np.roots(self.coefficients)
    #
    #     rs = []
    #
    #     for root in all_roots:
    #         module = np.abs(root)
    #
    #         if module < 0.05:
    #             rs.append(root)
    #
    #     return rs
    #
    # roots = property(get_roots)


def display(roots):
    x = np.real(roots)
    y = np.imag(roots)
    plt.plot(x, y, '.')
    plt.show()


if __name__ == '__main__':
    f = FAnother()

    roots = f.roots

    # display(roots)
