from airy_funcs import *
from FAbstract import *
import script_3


class F(FAbstract):
    def __init__(self, j=None):
        if j == 1:
            self.f = u
            self.df = du
        elif j == 2:
            self.f = v
            self.df = dv
        else:
            self.f = w
            self.df = dw

        self.initialize_consts()

        self.b = self.initialize_b()

    def get_coefficients(self):
        return self.compute_coefficients()

    coefficients = property(get_coefficients)

    def get_roots(self):
        all_roots = np.roots(self.coefficients)

        return self.sample_roots(all_roots)

    roots = property(get_roots)

    def initialize_consts(self):
        self.N = script_3.N

        self.p = script_3.p

        self.q = script_3.q

        self.y0 = script_3.y0

    def initialize_b(self):
        y = self.y0.wave_2

        b_1 = self.q ** 2 + y
        b_2 = self.q ** 2 - 2 * y
        b_3 = y * self.q ** 2 + self.q + y ** 2

        return {'1': b_1,
                '2': b_2,
                '3': b_3}

    def model(self, t):
        return self.df(t - self.y0.wave_2) - self.q * self.f(t - self.y0.wave_2)

    def compute_coefficients(self):
        y = self.y0.wave_2

        a_0 = self.model(-y)
        a_1 = -(y * self.f(-y) + self.q * self.df(-y))

        a_2 = -(a_0 * self.b['3'] + a_1) / (2 * self.b['1'])
        a_3 = (a_0 * self.b['2'] - a_1 * self.b['3']) / (6 * self.b['1'])

        a = np.array([a_0, a_1, a_2, a_3])

        coefficients = [self.compute_coefficient(self.N - i, a) for i in range(self.N + 1)]

        return coefficients

    def compute_coefficient(self, n, a):
        if n in range(4):
            return a[n]
        elif n >= 4:
            d = np.array([-1, self.b['2'], -self.b['3'], np.complex()])

            return self.iter_compute_coefficient(n, d, a)

    def iter_compute_coefficient(self, n, d, a):
        coefficient = np.complex()

        for i in range(4, n + 1):
            d[3] = (i - 1) * (i - 3)

            coefficient = np.sum(d * a) / (i * (i - 1) * self.b['1'])

            a = np.array(a.tolist()[1:] + [coefficient])

        return coefficient
