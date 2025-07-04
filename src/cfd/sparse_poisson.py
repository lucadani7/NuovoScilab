import numpy as np
import scipy as sp
import scipy.sparse.linalg as spla


# solve Poisson 1D equation with rare matrix
def solve_poisson(n=100):
    h = 1 / (n + 1)
    x = np.linspace(h, 1 - h, n)
    f = np.sin(np.pi * x)

    diagonals = [
        -1 * np.ones(n - 1),
        2 * np.ones(n),
        -1 * np.ones(n - 1)
    ]
    A = sp.diags(diagonals, [-1, 0, 1]) / h ** 2

    u = spla.spsolve(A, f)
    return x, u
