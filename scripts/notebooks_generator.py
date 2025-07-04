import os
import nbformat
from nbformat.v4 import new_notebook, new_code_cell

NOTEBOOKS_CFD = {
    "01_heat1d_simulation": """from src.cfd.heat1d import simulate_heat1d
import matplotlib.pyplot as plt

x, u0, uf = simulate_heat1d(n=100, alpha=0.02, t_end=1.0)

plt.plot(x, u0, label="Initial")
plt.plot(x, uf, label="Final")
plt.title("Simulation of warm equation 1D")
plt.xlabel("x")
plt.ylabel("Temperature u(x)")
plt.legend()
plt.grid()
plt.show()
""",
    "02_elasticity_bar": """from src.cfd.elasticity_solver import simulate_elastic_bar

E, A, L, F = 200e9, 0.01, 1.0, 1000
u = simulate_elastic_bar(E, A, L, F)

print(f"Displacement: {u:.6f} m")
""",
    "03_sparse_poisson": """from src.cfd.sparse_poisson import solve_poisson
import matplotlib.pyplot as plt

x, u = solve_poisson(n=100)

plt.plot(x, u, label="Poisson solution")
plt.legend()
plt.grid()")
plt.title("Poisson 1D equation with Dirichlet conditions")
plt.xlabel("x")
plt.ylabel("u(x)")
plt.grid()
plt.legend()
plt.show()
"""
}


def generate_notebooks():
    os.makedirs("../notebooks", exist_ok=True)
    for name, code in NOTEBOOKS_CFD.items():
        nb = new_notebook(cells=[new_code_cell(code)])
        path = f"../notebooks/{name}.ipynb"
        with open(path, "w", encoding="utf-8") as f:
            nbformat.write(nb, f)
        print(f" Notebook generated: {path}")


if __name__ == "__main__":
    generate_notebooks()
