# displacement into an elastic bar exerted to a force
def simulate_elastic_bar(E=200e9, A=0.01, L=1.0, F=1000):
    """
        E — Young modulus
        A — section area
        L — bar length
        F — force exterted

        Returns: displacement u
    """
    return F * L / (A * E)
