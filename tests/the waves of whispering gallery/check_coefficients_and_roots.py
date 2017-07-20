# the test of whispering gallery waves


from airy_funcs import *
from Y import *
import script_3


p = 1

Lambda = 0.1

k0 = script_3.compute_k0(Lambda)

m = script_3.compute_m(k0)

N0 = 10 ** (-6)

h = 50

y0 = Y0(m, p, N0)

y2 = Y2(k0, h, m, p)

y1 = Y1(y0.wave_2, y2.wave_2)


def W(i):
    t_1 = -y2.wave_1
    t_2 = -y1.wave_2

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


def compute_b():
    b = dict()
    b['40'] = -4 * y0.wave_1 ** 3
    b['20'] = -8 * y0.wave_1 ** 3 * (y1.wave_2 + y2.wave_1)
    b['21'] = 16 * y0.wave_1 ** 3
    b['10'] = 8 * y0.wave_1 ** 3
    b['00'] = -4 * y0.wave_1 ** 5

    [print('b' + str(key), b.get(key)) for key in b.keys()]

    return b


def compute_a():
    a = np.ndarray(shape=(7,), dtype=np.complex)

    b = compute_b()

    a[0] = W(2) - W(3)
    a[1] = y0.wave_1 * W(1)
    a[2] = y0.wave_1 * (W(2) + 0.5 * W(3))
    a[3] = 1/6 * (-(2 * y0.wave_1 * y2.wave_1 + y0.wave_1 ** 2) * W(1) + 2 * y0.wave_1 * W(4))
    a[4] = 1/24 * (2 * y0.wave_1 * W(1) - (4 * y0.wave_1 * y2.wave_1 + 3 * y0.wave_1 ** 2) * W(2) - (4 * y0.wave_1 * y2.wave_1 + y0.wave_1 ** 2) * W(3))
    a[5] = -(6 * b['20'] * a[3] + 2 * (b['21'] + b['10']) * a[2] + b['00'] * a[1]) / (120 * b['40'])
    a[6] = -(12 * b['20'] * a[4] + 3 * (2 * b['21'] + b['10']) * a[3] + b['00'] * a[2]) / (360 * b['40'])

    [print('a' + str(i), a[i]) for i in range(a.size)]

    return a


def model(t):
    t_1 = t - y1.wave_2
    t_2 = p ** 2 * t - y2.wave_1
    return dv(t_1) * w(t_2) - v(t_1) * dw(t_2)


def check_roots():
    roots = {1: -3.5 + 0.7j,
             2: -2.4 + 0.7j,
             3: -1.25 + 0.7j,
             4: -0.1 + 0.7j,
             5: 1.15 + 0.7j,
             6: 2.8 + 0.7j}

    for root in roots.values():
        print(root, np.abs(model(root)))


if __name__ == '__main__':
    # check_roots()

    # print(W(1), W(2), W(3), W(4))

    a = compute_a()
