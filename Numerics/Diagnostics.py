import numpy as np


def shear_energy(dbp, dbm):
    return dbp**2 + dbm**2



def axial_energy(A, dA, MA):
    return 0.5 * dA**2 + 0.5 * MA**2 * A**2



def hamiltonian_residual(H, rho_total):
    if H == 0:
        return np.inf

    return abs(1 - rho_total / (3 * H**2))
