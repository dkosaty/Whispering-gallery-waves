class B41:
    def __init__(self, p, p_prime, y0, y2):
        a = 4 * p_prime * (1 + p ** 3) / p ** 2

        b = (p ** 3 * y0.wave_2 - p_prime * y2.wave_2) ** 2

        self._value = a * b

    def get_value(self):
        return self._value

    value = property(get_value)


class B40:
    def __init__(self, p, p_prime, y0, y2):
        a = 4 / p ** 2

        b = p ** 3 * y0.wave_2 - p_prime * y2.wave_2

        c1 = p_prime ** 2 * y2.wave_2 ** 2
        c2 = p_prime ** 2 * y0.wave_2 * y2.wave_2
        c3 = -p ** 3 * y0.wave_2 ** 2
        c = c1 + c2 + c3

        d = -p_prime ** 3 / p ** 2 * (1 + p ** 3)

        self._value = a * b * c + d

    def get_value(self):
        return self._value

    value = property(get_value)


class B30:
    def __init__(self, p, p_prime, y0, y2):
        a = 4 * p_prime / p ** 2

        b = 1 + p ** 3

        c1 = p ** 6 * y0.wave_2 ** 2
        c2 = 2 * p_prime * p ** 3 * y0.wave_2 * y2.wave_2
        c3 = p_prime ** 2 * y2.wave_2 ** 2
        c = c1 + c2 + c3

        self._value = a * b * c

    def get_value(self):
        return self._value

    value = property(get_value)


class B22:
    def __init__(self, p, p_prime, y0, y2):
        a = -8 / p ** 2

        b = 1 - p ** 12

        c = (p ** 3 * y0.wave_2 - p_prime * y2.wave_2) ** 2

        self._value = a * b * c

    def get_value(self):
        return self._value

    value = property(get_value)


class B21:
    def __init__(self, p, p_prime, y0, y2):
        a = 2 / p ** 2

        b = 4 * (p ** 3 * y0.wave_2 - p_prime * y2.wave_2)

        c1 = 2 * p ** 3 * y0.wave_2 ** 2
        c2 = -2 * (1 - 2 * p ** 3 + p ** 12) * y0.wave_2 * y2.wave_2
        c3 = -2 * p_prime ** 2 * (p ** 6 + p ** 3 + 1) * y2.wave_2 ** 2
        c = c1 + c2 + c3

        d = p_prime ** 2 * (1 - p ** 12)

        self._value = a * (b * c + d)

    def get_value(self):
        return self._value

    value = property(get_value)


class B20:
    def __init__(self, p, p_prime, y0, y2):
        a = 2 / p ** 2

        b1 = p ** 3 * y0.wave_2 ** 2
        b2 = -p_prime ** 2 * y0.wave_2 * y2.wave_2
        b3 = -p_prime ** 2 * y2.wave_2 ** 2
        b = 4 * (b1 + b2 + b3)

        c1 = (1 - 2 * p ** 3 - p ** 6) * y0.wave_2 * y2.wave_2
        c2 = (1 - p ** 6) * y2.wave_2 ** 2
        c3 = -p ** 3 * y0.wave_2 ** 2
        c = c1 + c2 + c3

        d = -p_prime * (1 - p ** 12)

        self._value = a * (b * c + d)

    def get_value(self):
        return self._value

    value = property(get_value)


class B11:
    def __init__(self, p, p_prime, y0, y2):
        a = 4 * p_prime / p ** 2

        b1 = p_prime ** 2
        b2 = p ** 6 + 1
        b3 = p ** 3 * y0.wave_2 ** 2 - p_prime * y0.wave_2 * y2.wave_2
        b = b1 * b2 * b3

        c1 = -2 * (1 - 3 * p ** 2 + p ** 6)
        c2 = 1 + p ** 3
        c3 = (p ** 3 * y0.wave_2 - p_prime * y2.wave_2) ** 2
        c = c1 * c2 * c3

        d1 = p_prime ** 3
        d2 = (1 - 2 * p ** 3 - p ** 6) * y0.wave_2 * y2.wave_2
        d3 = (1 - p ** 6) * y2.wave_2 ** 2
        d4 = -p ** 3 * y0.wave_2 ** 2
        d = d1 * (d2 + d3 + d4)

        self._value = a * (b + c + d)

    def get_value(self):
        return self._value

    value = property(get_value)


class B10:
    def __init__(self, p, p_prime, y0, y2):
        a = 2 / p ** 2

        b1 = 4 * (1 - 3 * p ** 3 + p ** 6)
        b2 = p ** 3 * y0.wave_2 - p_prime * y2.wave_2
        b3 = p ** 3 * y0.wave_2 ** 2 - p_prime ** 2 * y2.wave_2 ** 2 - p_prime ** 2 * y0.wave_2 * y2.wave_2
        b = b1 * b2 * b3

        c1 = 2 * (1 + p ** 6) * y0.wave_2
        c2 = p ** 3 * (3 * p ** 3 - 1) * y0.wave_2 ** 2
        c3 = -p_prime * (p ** 6 + 4 * p ** 3 - 1) * y0.wave_2 * y2.wave_2
        c4 = p_prime ** 2 * (1 + p ** 3) * y2.wave_2 ** 2
        c = c1 * (c2 + c3 + c4)

        d1 = 2 * p_prime
        d2 = (3 * p ** 3 - 1) * y0.wave_2 - (1 - p ** 6) * y2.wave_2

        def d3():
            alpha = (1 - 2 * p ** 3 - p ** 6) * y0.wave_2 * y2.wave_2
            beta = p_prime * (1 + p ** 3) * y2.wave_2 ** 2
            gamma = -p ** 3 * y0.wave_2 ** 2
            return alpha + beta + gamma
        d = d1 * d2 * d3()

        e = p_prime ** 3 * (1 - 3 * p ** 3 + p ** 6) * (1 + p ** 6)

        self._value = a * (b + c + d + e)

    def get_value(self):
        return self._value

    value = property(get_value)


class B03:
    def __init__(self, p, p_prime, y0, y2):
        a = 4 / p ** 2
        b = (1 + p ** 3) ** 3
        c = (p_prime * y2.wave_2 - p ** 3 * y0.wave_2) ** 2
        d = p_prime ** 3

        self._value = a * b * c * d

    def get_value(self):
        return self._value

    value = property(get_value)


class B02:
    def __init__(self, p, p_prime, y0, y2):
        a = 2 * p_prime ** 3 / p ** 2 * (p ** 12 - 1)

        b1 = 4 / p ** 2
        b2 = (1 + p ** 3) ** 2
        b3 = p_prime * y2.wave_2 - p ** 3 * y0.wave_2
        b4 = p ** 3 * y0.wave_2 ** 2 - p_prime ** 2 * y0.wave_2 * y2.wave_2 - p_prime ** 2 * y2.wave_2 ** 2
        b5 = p_prime
        b = b1 * b2 * b3 * b4 * b5

        c1 = -2 / p ** 2
        c2 = 1 + p ** 3
        c3 = p_prime * y2.wave_2 - p ** 3 * y0.wave_2

        def c4():
            alpha = 2 * (5 * p ** 9 - 2 * p ** 6 - p ** 3) * y0.wave_2
            beta = 2 * p_prime * (p ** 9 - 2 * p ** 6 - 4 * p ** 3 + 2) * y0.wave_2 * y2.wave_2
            gamma = 4 * p_prime ** 3 * (1 + p ** 3) * y2.wave_2 ** 2
            return alpha + beta + gamma

        c = c1 * c2 * c3 * c4()

        d = p_prime ** 6 / p ** 2 * (1 + p ** 3)

        self._value = p_prime * (a + b + c + d)

    def get_value(self):
        return self._value

    value = property(get_value)


class B01:
    def __init__(self, p, p_prime, y0, y2):
        a1 = 2 * p_prime ** 3 / p ** 2
        a2 = 1 + p ** 6
        a3 = 3 * p_prime ** 2 * y2.wave_2 + (2 - 3 * p ** 3 + p ** 6) * y0.wave_2
        a = a1 * a2 * a3

        b1 = 2 * p_prime / p ** 2 * (1 + p ** 3) * (p_prime * y2.wave_2 - p ** 3 * y0.wave_2)

        def b2():
            alpha = (y0.wave_2 - p_prime * y2.wave_2)
            beta = 2 * (1 - p ** 3 - 2 * p ** 6) * y0.wave_2 * y2.wave_2
            gamma = (1 + 2 * p ** 3 - 3 * p ** 6) * y2.wave_2 ** 2 + (1 - 4 * p ** 3) * y0.wave_2 ** 2
            return alpha * (beta + gamma)

        def b3():
            alpha = p_prime * y2.wave_2 + (1 - 2 * p ** 3) * y0.wave_2
            beta = 2 * (1 - 3 * p ** 3) * y0.wave_2 * y2.wave_2
            gamma = p_prime * (3 + p ** 3) * y2.wave_2 ** 2 - y0.wave_2 ** 2
            return alpha * (beta + gamma)

        b = b1 * (b2() + b3())

        c1 = 2 / p ** 2
        c2 = p ** 3 * y0.wave_2 ** 2 - p_prime ** 2 * y0.wave_2 * y2.wave_2 - p_prime ** 2 * y2.wave_2 ** 2
        c3 = 4 * p_prime * (1 + p ** 3)
        c4 = p ** 3 * y0.wave_2 - p_prime ** 2 * y0.wave_2 * y2.wave_2 - p_prime ** 2 * y2.wave_2 ** 2
        c = c1 * c2 * c3 * c4

        self._value = a + b + c

    def get_value(self):
        return self._value

    value = property(get_value)


class B00:
    def __init__(self, p, p_prime, y0, y2):
        a1 = -2 * (p_prime / p) ** 2
        a2 = 1 + p ** 6
        a3 = 3 * p_prime ** 2 * y0.wave_2 * y2.wave_2 + p_prime * (1 - 2 * p ** 3) * y2.wave_2 ** 2

        a = a1 * a2 * a3

        b1 = 2 / p ** 2
        b2 = p ** 3 * y0.wave_2 ** 2 - p_prime ** 2 * y0.wave_2 * y2.wave_2 - p_prime ** 2 * y2.wave_2 ** 2

        def b3():
            alpha = y0.wave_2 - p_prime * y2.wave_2

            beta_1 = 2 * (1 - p ** 3 - 2 * p ** 6) * y0.wave_2 * y2.wave_2
            beta_2 = (1 + 2 * p ** 3 - 3 * p ** 6) * y2.wave_2 ** 2 + (1 - 4 * p ** 3) * y0.wave_2 ** 2
            beta = beta_1 + beta_2

            gamma = p_prime * y2.wave_2 + (1 - 2 * p ** 3) * y0.wave_2

            zeta_1 = 2 * (1 - 3 * p ** 3) * y0.wave_2 * y2.wave_2
            zeta_2 = p_prime * (3 - p ** 3) * y2.wave_2 ** 2 - y0.wave_2 ** 2
            zeta = zeta_1 + zeta_2

            return alpha * beta + gamma * zeta

        b = b1 * b2 * b3()

        c1 = p_prime ** 3 / p ** 2

        def c2():
            alpha = 2 * (2 * p ** 9 + 3 * p ** 6 - 8 * p ** 3 + 3) * y0.wave_2 * y2.wave_2
            beta = 5 * p_prime ** 2 * (1 + p ** 3) * y2.wave_2 ** 2
            gamma = (1 - 7 * p ** 3 + 4 * p ** 6) * y0.wave_2 ** 2
            return alpha + beta + gamma

        c = c1 * c2()

        self._value = a + b + c

    def get_value(self):
        return self._value

    value = property(get_value)
