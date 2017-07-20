from airy_funcs import *
from FAbstract import *
from Y import *
import script_1
import script_2


a = 6.37 * 1e6


def compute_sigmaU(polarization_parameter, eps, sigma, Lambda):
    eps_ = np.complex(eps, 60 * sigma * Lambda)

    if polarization_parameter == 'e':
        # vertical polarization
        return 1 / np.sqrt(eps_)
    elif polarization_parameter == 'm':
        # horizontal polarization
        return np.sqrt(eps_)
    else:
        raise AttributeError


def compute_k0(Lambda):
    return 2 * np.pi / Lambda


def compute_m(k0):
    return (0.5 * k0 * a) ** (1 / 3)


def compute_q(m, sigma_u, p):
    return np.complex(0, m * sigma_u) / p


N0 = 1e-6

h = 100

g = N0 / h

p = (1 - a * g) ** (1 / 3)

p_prime = 1 - p ** 3

Lambda = 0.1

k0 = compute_k0(Lambda)

m = compute_m(k0)

eps = 80
sigma = 3

sigma_u = compute_sigmaU('e', eps, sigma, Lambda)

q = compute_q(m, sigma_u, p)

y0 = Y0(m, p, N0)

y2 = Y2(k0, h, m, p)

y1 = Y1(y0.wave_2, y2.wave_2)

N = 160


class F(FAbstract):
    t_0 = 0.1

    def __init__(self):
        self.initialize_consts()

        self.initialize_functions()

    def get_coefficients(self):
        return self.compute_coefficients()

    coefficients = property(get_coefficients)

    def get_roots(self):
        all_roots = np.roots(self.coefficients)

        return self.sample_roots(all_roots)

    roots = property(get_roots)

    def initialize_consts(self):
        self.N = N

        self.p = p
        self.q = q

        self.y0 = y0
        self.y1 = y1
        self.y2 = y2

    def initialize_functions(self):
        self.f_1 = script_1.F(1)
        self.f_2 = script_1.F(2)
        self.f_11 = script_2.F(1, 1)
        self.f_12 = script_2.F(1, 2)
        self.f_21 = script_2.F(2, 1)
        self.f_22 = script_2.F(2, 2)

    def model(self, t):
        t_1 = self.p ** 2 * t - self.y2.wave_1
        t_2 = t - self.y1.wave_2
        t_3 = t - self.y0.wave_2

        real = (1 / self.p * dv(t_1) * v(t_2) - v(t_1) * dv(t_2)) * (du(t_3) - self.q * u(t_3)) -\
               (1 / self.p * dv(t_1) * u(t_2) - v(t_1) * du(t_2)) * (dv(t_3) - self.q * v(t_3))

        imaginary = (1 / self.p * du(t_1) * u(t_2) - u(t_1) * du(t_2)) * (dv(t_3) - self.q * v(t_3)) -\
                    (1 / self.p * du(t_1) * v(t_2) - u(t_1) * dv(t_2)) * (du(t_3) - self.q * u(t_3))

        return np.complex(real, imaginary)

    def compute_coefficients(self):
        a_1 = self.f_1.coefficients
        a_2 = self.f_2.coefficients
        a_11 = self.f_11.coefficients
        a_12 = self.f_12.coefficients
        a_21 = self.f_21.coefficients
        a_22 = self.f_22.coefficients

        coefficients = np.zeros(shape=(self.N + 1,), dtype=np.complex)

        for n in range(self.N + 1):
            for k in range(n + 1):
                real = a_22[k] * a_1[n - k] - a_21[k] * a_2[n - k]
                imaginary = a_11[k] * a_2[n - k] - a_12[k] * a_1[n - k]

                coefficients[n] += np.complex(real, imaginary)

        return np.fliplr([coefficients])[0]
