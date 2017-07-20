import numpy as np


class FAbstract(object):
    def compute_coefficients(self):
        pass

    def model(self, t):
        raise NotImplementedError

    def sample_roots(self, all_roots, eps=1e-3):
        roots = []

        for root in all_roots:
            discrepancy = np.abs(self.model(root))

            if discrepancy < eps:
                roots.append(root)

        return roots
