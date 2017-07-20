from airy_funcs import *
from Y import *
import script_2
import script_3


p = 1

Lambda = 0.1

h = 0

k0 = script_3.compute_k0(Lambda)

m = script_3.compute_m(k0)

eps = script_3.eps
sigma = script_3.sigma

sigma_u = script_3.compute_sigmaU('e', eps, sigma, Lambda)

q = script_3.compute_q(m, sigma_u, p)

N0 = 1e-6

y0 = Y0(m, p, N0)

y2 = Y2(k0, h, m, p)

y1 = Y1(y0.wave_2, y2.wave_2)

N = 160


class FAnother(script_2.F):
    def initialize_consts(self):
        self.N = N

        self.p = p

        self.p_prime = 0

        self.y0 = y0

        self.y1 = y1

        self.y2 = y2

    def initialize_const_coefficients(self):
        b = dict()

        b['40'] = -4 * y0.wave_1 ** 3
        b['20'] = -8 * y0.wave_1 ** 4
        b['21'] = 16 * y0.wave_1 ** 3
        b['10'] = 8 * y0.wave_1 ** 3
        b['00'] = -4 * y0.wave_1 ** 5

        return b

    def compute_init_coefficients(self):
        a = np.ndarray(shape=(7,), dtype=np.complex)

        b = self.initialize_const_coefficients()

        a[0] = self.model(0)
        a[1] = y0.wave_1 * self.W(1)
        a[2] = y0.wave_1 * (self.W(2) + 0.5 * self.W(3))
        a[3] = 1/6 * (-y0.wave_1 ** 2 * self.W(1) + 2 * y0.wave_1 * self.W(4))
        a[4] = 1/24 * (2 * y0.wave_1 * self.W(1) - 3 * y0.wave_1 ** 2 * self.W(2) - y0.wave_1 ** 2 * self.W(3))
        a[5] = -1/(120 * b['40']) * (6 * b['20'] * a[3] + 2 * (b['21'] + b['10']) * a[2] + b['00'] * a[1])
        a[6] = -1/(360 * b['40']) * (12 * b['20'] * a[4] + 3 * (2 * b['21'] + b['10']) * a[3] + b['00'] * a[2])

        [print('b' + str(key), b.get(key)) for key in b.keys()]
        [print('a' + str(i), a[i]) for i in range(a.size)]

        return a

    def W(self, i, t=0):
        if self.i not in range(1, 3) and self.j not in range(1, 3):
            raise IndexError("index i \in [1, 2], index j \in [1, 2]")

        if i == 1:
            return self.W_1(t)
        elif i == 2:
            return self.W_2(t)
        elif i == 3:
            return self.W_3(t)
        elif i == 4:
            return self.W_4(t)
        else:
            raise IndexError

    def W_1(self, t):
        t_1 = t
        t_2 = t - self.y1.wave_2

        if self.i == 1:
            if self.j == 1:
                return u(t_1) * u(t_2)
            else:
                return u(t_1) * v(t_2)
        else:
            if self.j == 1:
                return v(t_1) * u(t_2)
            else:
                return v(t_1) * v(t_2)

    def W_2(self, t):
        t_1 = t
        t_2 = t - self.y1.wave_2

        if self.i == 1:
            if self.j == 1:
                return du(t_1) * u(t_2)
            else:
                return du(t_1) * v(t_2)
        else:
            if self.j == 1:
                return dv(t_1) * u(t_2)
            else:
                return dv(t_1) * v(t_2)

    def W_3(self, t):
        t_1 = t
        t_2 = t - self.y1.wave_2

        if self.i == 1:
            if self.j == 1:
                return u(t_1) * du(t_2)
            else:
                return u(t_1) * dv(t_2)
        else:
            if self.j == 1:
                return v(t_1) * du(t_2)
            else:
                return v(t_1) * dv(t_2)

    def W_4(self, t):
        t_1 = t
        t_2 = t - self.y1.wave_2

        if self.i == 1:
            if self.j == 1:
                return du(t_1) * du(t_2)
            else:
                return du(t_1) * dv(t_2)
        else:
            if self.j == 1:
                return dv(t_1) * du(t_2)
            else:
                return dv(t_1) * dv(t_2)


if __name__ == '__main__':
    for i in range(1, 3):
        for j in range(1, 3):
            print('f' + str(i) + str(j))

            f = FAnother(i, j)
            f.compute_init_coefficients()

            print()
