import matplotlib.pyplot as plt
from Y import Y0
from airy_funcs import *
import script_1
import script_3


p = 1

Lambda = 0.3

k0 = script_3.compute_k0(Lambda)

m = script_3.compute_m(k0)

eps = script_3.eps
sigma = script_3.sigma

sigma_u = script_3.compute_sigmaU('m', eps, sigma, Lambda)

q = script_3.compute_q(m, sigma_u, p)

N0 = 1e-6

y0 = Y0()

N = 100


class FAnother(script_1.F):
    def initialize_consts(self):
        self.N = N

        self.p = p

        self.q = q

        self.y0 = y0

    def get_roots(self):
        [print(root) for root in self.coefficients]

        all_roots = np.roots(self.coefficients)

        return self.sample_roots(all_roots, eps=1e-4)

    roots = property(get_roots)

    def model(self, t):
        real = du(t) - self.q * u(t)
        imaginary = dv(t) - self.q * v(t)

        # return -2j * np.complex(real, imaginary)
        return np.complex(real, imaginary)


def display(roots):
    # [print(root) for root in roots]

    x = np.real(roots)
    y = np.imag(roots)
    plt.plot(x, y, '.')
    plt.show()


if __name__ == '__main__':
    f = FAnother()

    roots = f.roots

    # a = [root - y0.wave_2 for root in roots]
    # b = [root + y0.wave_2 for root in roots]

    display(roots)
