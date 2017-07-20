# the solution of the modified whispering gallery equation by t0 != 0


from airy_funcs import *
import script_2_modified


class WhisperingGallery(script_2_modified.F):
    def W(self, i, t=None):
        if t is None:
            t = self.t_0

        t_1 = self.p ** 2 * t - self.y2.wave_1
        t_2 = t - self.y1.wave_2

        if i == 1:
            return w(t_1) * v(t_2)
        elif i == 2:
            return dw(t_1) * v(t_2)
        elif i == 3:
            return w(t_1) * dv(t_2)
        elif i == 4:
            return dw(t_1) * dv(t_2)
        else:
            raise IndexError
