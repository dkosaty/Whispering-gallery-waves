class Y0:
    def __init__(self, m=None, p=None, N0=None):
        if m is not None and p is not None and N0 is not None:
            self.wave_1 = 2 * m ** 2 * N0
            self.wave_2 = self.wave_1 / p ** 2
        else:
            self.wave_1 = 0
            self.wave_2 = 0

    def __getattr__(self, item):
        if item == 'wave_1':
            return self.wave_1
        elif item == 'wave_2':
            return self.wave_2
        else:
            raise AttributeError


class Y1:
    def __init__(self, y0_wave2=None, y2_wave2=None):
        if y0_wave2 is not None and y2_wave2 is not None:
            self.wave_2 = y0_wave2 + y2_wave2
        else:
            self.wave_2 = 0

    def __getattr__(self, item):
        if item == 'wave_2':
            return self.wave_2
        else:
            raise AttributeError


class Y2:
    def __init__(self, k0=None, h=None, m=None, p=None):
        if k0 is not None and h is not None and m is not None and p is not None:
            self.wave_1 = k0 * h / float(m)
            self.wave_2 = p * self.wave_1
        else:
            self.wave_1 = 0
            self.wave_2 = 0

    def __getattr__(self, item):
        if item == 'wave_1':
            return self.wave_1
        elif item == 'wave_2':
            return self.wave_2
        else:
            raise AttributeError
