from matplotlib import pyplot, colors
import script_3
from Y import *
from whispering_gallery import *


class FAnother(WhisperingGallery):
    def __init__(self, Lambda):
        self.Lambda = Lambda
        script_2_modified.F.__init__(self)

    def initialize_consts(self):
        self.N = 100

        self.p = 1

        self.p_prime = 1 - self.p ** 3

        k0 = script_3.compute_k0(self.Lambda)

        m = script_3.compute_m(k0)

        h = 100

        N0 = 1e-6

        self.y0 = Y0(m, self.p, N0)

        self.y2 = Y2(k0, h, m, self.p)

        self.y1 = Y1(self.y0.wave_2, self.y2.wave_2)

        self.t_0 = 0.01

    def get_roots(self):
        all_roots = np.roots(self.coefficients)

        # for root in all_roots:
        #     print(root, np.abs(self.model(root)))

        return self.sample_roots(all_roots, eps=0.1)

    roots = property(get_roots)

if __name__ == '__main__':
    # colors = list(map(lambda x: x[1], enumerate(colors.cnames)))
    colors = ['red', 'orange', 'yellow', 'green', 'lightblue', 'blue', 'violet', 'black', 'gray', 'brown']

    values = list(np.linspace(0.1, 1, num=10))

    for Lambda in values:
        f = FAnother(Lambda)
        roots = f.roots

        print(Lambda, roots)

        x = np.real(roots)
        y = np.imag(roots)

        label = '$\lambda=$' + str(Lambda)
        pyplot.plot(x, y, color=colors[values.index(Lambda)], linestyle='None', marker='.', markersize=15, label=label)

        pyplot.title("Roots trajectory by variance length of radiowave ($h = 100$, $N_0 = 10^{-6}$)")

    pyplot.legend(bbox_to_anchor=(1, 0.5), loc='center left', numpoints=1)

    pyplot.xlabel("Re(t)")
    pyplot.ylabel("Im(t)")

    pyplot.show()

