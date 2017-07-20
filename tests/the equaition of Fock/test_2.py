# the test of the Fock equation


import numpy as np
import matplotlib.pyplot as plt
from Y import Y0
import script_1
import script_3


class FAnother(script_1.F):
    def get_roots(self):
        all_roots = np.roots(self.coefficients)

        return self.sample_roots(all_roots, eps=1e-4)

    roots = property(get_roots)

    def initialize_consts(self):
        Lambda = 0.3

        p = 1

        k0 = script_3.compute_k0(Lambda)

        m = script_3.compute_m(k0)

        eps = script_3.eps
        sigma = script_3.sigma

        sigma_u = script_3.compute_sigmaU('m', eps, sigma, Lambda)

        self.q = script_3.compute_q(m, sigma_u, p)

        self.y0 = Y0()

        self.N = 100


def display(roots):
    x = np.real(roots)
    y = np.imag(roots)
    plt.plot(x, y, '.')
    plt.show()


if __name__ == '__main__':
    f = FAnother()
    roots = f.roots

    for root in roots:
        module = np.abs(root)
        discrepancy = np.abs(f.model(root))
        print(root, module, discrepancy)

    display(roots)
