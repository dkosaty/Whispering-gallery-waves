from Y import *
import script_1
import script_2
import script_3


p = 1

Lambda = 0.3

h = 10

k0 = script_3.compute_k0(Lambda)

m = script_3.compute_m(k0)

eps = script_3.eps
sigma = script_3.sigma

sigma_u = script_3.compute_sigmaU('e', eps, sigma, Lambda)

q = script_3.compute_q(m, sigma_u, p)

N0 = 0

y0 = Y0(m, p, N0)

y2 = Y2(k0, h, m, p)

y1 = Y1(y0.wave_2, y2.wave_2)

N = 160


class Namespace_1:
    class F(script_1.F):
        def initialize_consts(self):
            self.N = N

            self.q = q

            self.p = p

            self.y0 = y0


class Namespace_2:
    class F(script_2.F):
        def initialize_consts(self):
            self.N = N

            self.p = p

            self.p_prime = 0

            self.y0 = y0

            self.y1 = y1

            self.y2 = y2

        def initialize_const_coefficients(self):
            return {'41': 0j,
                    '40': 1j,
                    '30': 0j,
                    '22': 0j,
                    '21': -4j,
                    '20': 4 * y1.wave_2,
                    '11': 0j,
                    '10': -2j,
                    '00': 0j,
                    '03': 0j,
                    '02': 0j,
                    '01': 0j}


class FAnother(script_3.F):
    def initialize_consts(self):
        self.N = N

        self.p = p
        self.q = q

        self.y0 = y0
        self.y1 = y1
        self.y2 = y2

    def initialize_functions(self):
        self.f_1 = Namespace_1.F(1)
        self.f_2 = Namespace_1.F(2)
        self.f_11 = Namespace_2.F(1, 1)
        self.f_12 = Namespace_2.F(1, 2)
        self.f_21 = Namespace_2.F(2, 1)
        self.f_22 = Namespace_2.F(2, 2)


if __name__ == '__main__':
    f = FAnother()

    print(f.roots)
