import numpy as np
from scipy.integrate import solve_ivp


# warm equation 1D: derivate in time
def heat_rhs(t, u, alpha, dx):
    up = np.roll(u, -1)
    um = np.roll(u, +1)
    return alpha * (up - 2 * u + um) / dx ** 2


# numerical simulation of temperature propagation
def simulate_heat1d(n=100, alpha=0.01, t_end=1.0):
    x = np.linspace(0, 2 * np.pi, n, endpoint=False)
    u0 = np.sin(x)
    dx = x[1] - x[0]
    sol = solve_ivp(heat_rhs, (0, t_end), u0, args=(alpha, dx), method='RK23')
    return x, u0, sol.y[:, -1]
