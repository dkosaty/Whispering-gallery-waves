from airy_funcs import *
from Y import *
import script_3


p = 1

Lambda = 0.3

h = 100

k0 = script_3.compute_k0(Lambda)

m = script_3.compute_m(k0)

eps = 80
sigma = 3

sigma_u = script_3.compute_sigmaU('e', eps, sigma, Lambda)

q = script_3.compute_q(m, sigma_u, p)

N0 = 1e-6

y0 = Y0(m, p, N0)

y2 = Y2(k0, h, m, p)

y1 = Y1(y0.wave_2, y2.wave_2)


class G(script_3.F):
    def initialize_consts(self):
        self.p = p
        self.q = q

        self.y0 = y0
        self.y1 = y1
        self.y2 = y2


class F:
    def __init__(self, j):
        self.j = j

    def model(self, t):
        tau = t - y0.wave_2

        return dw(tau, self.j) - q * w(tau, self.j)


class F1:
    def __init__(self, j):
        self.j = j

    def model(self, t):
        t_1 = p ** 2 * t - y2.wave_1
        t_2 = t - y1.wave_2

        return 1 / p * dw(t_1) * w(t_2, self.j) - w(t_1) * dw(t_2, self.j)


class H:
    def __init__(self):
        self.f_12 = F1(2)
        self.f_1 = F(1)
        self.f_11 = F1(1)
        self.f_2 = F(2)

    def model(self, t):
        return self.f_12.model(t) * self.f_1.model(t) - self.f_11.model(t) * self.f_2.model(t)


if __name__ == '__main__':
    roots = {1: 2.22 + 1.01j,
             2: 0.64 + 1.18j,
             3: 4.31 + 1.18j,
             4: -1.43 + 1.81j,
             5: -4.3 + 2.56j,
             6: 5.76 + 3.1j,
             7: -7.92 + 3.37j,
             8: 6.65 + 4.45j,
             9: 7.39 + 5.6j,
             10: 8 + 6.6j}

    obj_1 = H()
    obj_2 = G()

    for root in roots.values():
        discrepancy_1 = np.abs(obj_1.model(root))

        discrepancy_2 = np.abs(obj_2.model(root))

        print(root, discrepancy_1, discrepancy_2, discrepancy_1 / discrepancy_2)
