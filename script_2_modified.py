from airy_funcs import *
from FAbstract import *
from B import *
import script_3


class F(FAbstract):
    def __init__(self, i=None, j=None):
        self.i = i
        self.j = j

        self.initialize_consts()

        self.c = self.initialize_const_modified_coefficients()

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

        self.p_prime = script_3.p_prime

        self.y0 = script_3.y0

        self.y1 = script_3.y1

        self.y2 = script_3.y2

        self.t_0 = script_3.F.t_0

    def compute_init_coefficients(self):
        a = np.ndarray(shape=(7,), dtype=np.complex)

        a[0] = self.model(self.t_0)
        a[1] = A1(self.p, self.p_prime, self.y0, self.t_0, self.W).value
        a[2] = A2(self.p, self.p_prime, self.y0, self.y2, self.t_0, self.W).value
        a[3] = A3(self.p, self.p_prime, self.y0, self.y2, self.t_0, self.W).value
        a[4] = A4(self.p, self.p_prime, self.y0, self.y2, self.t_0, self.W).value
        a[5] = A5(a.tolist()[:5], self.c).value
        a[6] = A6(a.tolist()[:6], self.c).value

        return a

    def initialize_const_coefficients(self):
        return {'41': B41(self.p, self.p_prime, self.y0, self.y2).value,
                '40': B40(self.p, self.p_prime, self.y0, self.y2).value,
                '30': B30(self.p, self.p_prime, self.y0, self.y2).value,
                '22': B22(self.p, self.p_prime, self.y0, self.y2).value,
                '21': B21(self.p, self.p_prime, self.y0, self.y2).value,
                '20': B20(self.p, self.p_prime, self.y0, self.y2).value,
                '11': B11(self.p, self.p_prime, self.y0, self.y2).value,
                '10': B10(self.p, self.p_prime, self.y0, self.y2).value,
                '00': B00(self.p, self.p_prime, self.y0, self.y2).value,
                '03': B03(self.p, self.p_prime, self.y0, self.y2).value,
                '02': B02(self.p, self.p_prime, self.y0, self.y2).value,
                '01': B01(self.p, self.p_prime, self.y0, self.y2).value}

    def initialize_const_modified_coefficients(self):
        b = self.initialize_const_coefficients()

        c = dict()

        c['41'] = b['41']
        c['40'] = b['41'] * self.t_0 + b['40']

        c['30'] = b['30']

        c['22'] = b['22']
        c['21'] = 2 * b['22'] * self.t_0 + b['21']
        c['20'] = b['22'] * self.t_0 ** 2 + b['21'] * self.t_0 + b['20']

        c['11'] = b['11']
        c['10'] = b['11'] * self.t_0 + b['10']

        c['03'] = b['03']
        c['02'] = 3 * b['03'] * self.t_0 + b['02']
        c['01'] = 3 * b['03'] * self.t_0 ** 2 + 2 * b['02'] * self.t_0 + b['01']

        c['00'] = b['03'] * self.t_0 ** 3 + b['02'] * self.t_0 ** 2 + b['01'] * self.t_0 + b['00']

        return c

    def model(self, t):
        return 1 / self.p * self.W(2, t) - self.W(3, t)

    def compute_coefficients(self):
        a = self.compute_init_coefficients()

        coefficients = [self.compute_coefficient(self.N - i, a) for i in range(self.N + 1)]

        return coefficients

    def compute_coefficient(self, n, a):
        if n in range(7):
            return a[n]
        elif n >= 7:
            d = np.ndarray(shape=(7,), dtype=np.complex)

            d[0] = self.c['03']
            d[1] = self.c['02']
            d[2] = self.c['01']

            return self.iter_compute_coefficient(n, d, a)

    def iter_compute_coefficient(self, n, d, a):
        coefficient = np.complex()

        for i in range(7, n + 1):
            d[3] = (i - 4) * (i - 5) * self.c['22'] + (i - 4) * self.c['11'] + self.c['00']
            d[4] = (i - 3) * ((i - 4) * self.c['21'] + self.c['10'])
            d[5] = (i - 2) * (i - 3) * self.c['20']
            d[6] = (i - 1) * (i - 2) * (i - 3) * ((i - 4) * self.c['41'] - self.c['30'])

            coefficient = -np.sum(d * a) / (i * (i - 1) * (i - 2) * (i - 3) * self.c['40'])

            a = np.array(a.tolist()[1:] + [coefficient])

        return coefficient

    def W(self, i, t=None):
        if t is None:
            t = self.t_0

        if i == 1:
            funcs_matrix = np.matrix([[u, v], [u, v]])
        elif i == 2:
            funcs_matrix = np.matrix([[du, dv], [u, v]])
        elif i == 3:
            funcs_matrix = np.matrix([[u, v], [du, dv]])
        elif i == 4:
            funcs_matrix = np.matrix([[du, dv], [du, dv]])
        else:
            raise IndexError

        return self._W(funcs_matrix, t)

    def _W(self, f, t):
        if self.i not in range(1, 3) and self.j not in range(1, 3):
            raise IndexError("index i \in [1, 2], index j \in [1, 2]")

        t_1 = self.p ** 2 * t - self.y2.wave_1
        t_2 = t - self.y1.wave_2

        if self.i == 1:
            if self.j == 1:
                _w = f[0, 0](t_1) * f[1, 0](t_2)
            else:
                _w =  f[0, 0](t_1) * f[1, 1](t_2)
        else:
            if self.j == 1:
                _w = f[0, 1](t_1) * f[1, 0](t_2)
            else:
                _w = -f[0, 1](t_1) * f[1, 1](t_2)

        return _w


class A1:
    def __init__(self, p, p_prime, y0, t_0, W):
        a = y0.wave_2 - p_prime * t_0
        d = p_prime / p
        self._value = a * W(1) + d * W(4)

    def get_value(self):
        return self._value

    value = property(get_value)


class A2:
    def __init__(self, p, p_prime, y0, y2, t_0, W):
        a = -p_prime
        b = 1 / p * (p_prime ** 2 * t_0 - p_prime * y2.wave_2 - (1 - 2 * p ** 3) * y0.wave_2)
        c = -(p_prime ** 2 * t_0 + p_prime * y2.wave_2 - y0.wave_2)
        self._value = 1 / 2 * (a * W(1) + b * W(2) + c * W(3))

    def get_value(self):
        return self._value

    value = property(get_value)


class A3:
    def __init__(self, p, p_prime, y0, y2, t_0, W):
        a1 = -p_prime ** 3 * t_0 ** 2
        a2 = ((2 - 3 * p ** 3 + 3 * p ** 6) * y0.wave_2 - (1 - p ** 6) * y2.wave_2) * t_0
        a3 = (1 - 3 * p ** 3) * y0.wave_2 * y2.wave_2 + 2 * p_prime * y2.wave_2 ** 2 - y0.wave_2 ** 2
        a = a1 + a2 + a3

        b = p_prime / p * (1 - 2 * p ** 3)

        c = -p_prime * (2 - p ** 3)

        d = 1 / p * (p_prime ** 3 * t_0 + (3 * p ** 3 - 1) * y0.wave_2 - (1 - p ** 6) * y2.wave_2)

        self._value = 1 / 6 * (a * W(1) + b * W(2) + c * W(3) + d * W(4))

    def get_value(self):
        return self._value

    value = property(get_value)


class A4:
    def __init__(self, p, p_prime, y0, y2, t_0, W):
        a = 2 * (2 - 3 * p ** 3 + 2 * p ** 6) * (y0.wave_2 - p_prime * t_0)

        b1 = p_prime ** 4 * t_0 ** 2
        b2 = 2 * ((2 * p ** 9 - 3 * p ** 6 + 4 * p ** 3 - 1) * y0.wave_2 - p_prime * (1 + p ** 6) * y2.wave_2) * t_0
        b3 = 2 * (p_prime - 2 * p ** 6) * y0.wave_2 * y2.wave_2 + (1 + 2 * p ** 3 - 3 * p ** 6) * y2.wave_2 ** 2
        b4 = (1 - 4 * p ** 3) * y0.wave_2 ** 2
        b = 1 / p * (b1 + b2 + b3 + b4)

        c1 = -p_prime ** 4 * t_0 ** 2
        c2 = 2 * ((3 * p ** 6 - 2 * p ** 3 + 1) * y0.wave_2 - p_prime * (1 + p ** 6) * y2.wave_2) * t_0
        c3 = 2 * (1 - 3 * p ** 3) * y0.wave_2 * y2.wave_2 + p_prime * (3 + p ** 3) * y2.wave_2 ** 2 - y0.wave_2 ** 2
        c = c1 + c2 + c3

        d = 2 * p_prime / p * (1 - 3 * p ** 3 + p ** 6)

        self._value = 1 / 24 * (a * W(1) + b * W(2) + c * W(3) + d * W(4))

    def get_value(self):
        return self._value

    value = property(get_value)


class A5:
    def __init__(self, a, c):
        d = np.ndarray(shape=(5,), dtype=np.complex)

        d[4] = 24 * (c['41'] - c['30']) * a[4]
        d[3] = 6 * c['20'] * a[3]
        d[2] = 2 * (c['21'] + c['10']) * a[2]
        d[1] = (c['11'] + c['00']) * a[1]
        d[0] = c['01'] * a[0]

        self._value = -np.sum(d) / (120 * c['40'])

    def get_value(self):
        return self._value

    value = property(get_value)


class A6:
    def __init__(self, a, c):
        d = np.ndarray(shape=(6,), dtype=np.complex)

        d[5] = 60 * (2 * c['41'] - c['30']) * a[5]
        d[4] = 12 * c['20'] * a[4]
        d[3] = 3 * (2 * c['21'] + c['10']) * a[3]
        d[2] = (2 * (c['22'] + c['11']) + c['00']) * a[2]
        d[1] = c['01'] * a[1]
        d[0] = c['02'] * a[0]

        self._value = -np.sum(d) / (360 * c['40'])

    def get_value(self):
        return self._value

    value = property(get_value)
