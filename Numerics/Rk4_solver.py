import numpy as np


class MATCSolver:
    def __init__(self, alpha=0.08, MA=1e-3, Mstar=1e-1):
        self.alpha = alpha
        self.MA = MA
        self.Mstar = Mstar

    def derivatives(self, t, y):
        """
        State vector:
        y = [Omega, beta_p, beta_m,
             dOmega, dbeta_p, dbeta_m,
             A, dA,
             phi, dphi]
        """

        Omega, bp, bm, dOmega, dbp, dbm, A, dA, phi, dphi = y

        H = dOmega

        # Simplified Bianchi-IX potential
        Vix = np.exp(-4 * Omega) * (bp**2 + bm**2)

        # Effective parity source
        source = -(2 * self.alpha / self.Mstar) * A * dphi

        # Evolution equations
        ddOmega = -0.5 * (dbp**2 + dbm**2 + dA**2 + dphi**2)

        ddbp = -3 * H * dbp - bp - 0.01 * A**2
        ddbm = -3 * H * dbm - bm - 0.01 * A**2

        ddA = -3 * H * dA - self.MA**2 * A + source

        ddphi = -3 * H * dphi - 0.1 * phi

        return np.array([
            dOmega,
            dbp,
            dbm,
            ddOmega,
            ddbp,
            ddbm,
            dA,
            ddA,
            dphi,
            ddphi
        ])

    def rk4_step(self, t, y, dt):
        k1 = self.derivatives(t, y)
        k2 = self.derivatives(t + dt/2, y + dt*k1/2)
        k3 = self.derivatives(t + dt/2, y + dt*k2/2)
        k4 = self.derivatives(t + dt, y + dt*k3)

        return y + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)
