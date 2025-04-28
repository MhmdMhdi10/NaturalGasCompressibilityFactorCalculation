
import numpy as np

# Universal gas constant (in ft³·psia/(lbmol·°R))
R = 10.7316

# Soave-Redlich-Kwong EOS function for Z
def srk_eos(T, P, a, b, Tc, Pc):
    """
    Calculate compressibility factor (Z) using Soave-Redlich-Kwong EOS.

    :param T: Temperature in °R
    :param P: Pressure in psia
    :param a: Parameter 'a' (in psia·ft³)
    :param b: Parameter 'b' (in ft³)
    :param Tc: Critical temperature of the component in °R
    :param Pc: Critical pressure of the component in psia
    :return: Compressibility factor Z
    """
    # Calculate alpha using Soave's modification
    Tr = T / Tc  # Reduced temperature
    alpha = (1 + 0.480 + 1.574 * Tr - 0.176 * Tr ** 2) ** 2

    # Cubic equation coefficients
    A = (a * P) / (R ** 2 * T ** 2)
    B = (b * P) / (R * T)

    # Cubic equation coefficients for Z (z^3 - Bz^2 + Az - C = 0)
    coef = [1, -B, A, -P / (R * T)]

    # Solve the cubic equation
    roots = np.roots(coef)
    # Only real, positive roots are valid for Z
    real_roots = [root.real for root in roots if root.imag == 0 and root.real > 0]
    if real_roots:
        return min(real_roots)  # Return the smallest real root
    else:
        return None
