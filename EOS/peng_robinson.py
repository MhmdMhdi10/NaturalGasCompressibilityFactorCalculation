
import numpy as np

# Universal gas constant (in ft³·psia/(lbmol·°R))
R = 10.7316

# Peng-Robinson EOS function for Z
def peng_robinson_eos(T, P, a, b):
    """
    Calculate compressibility factor (Z) using Peng-Robinson EOS.

    :param T: Temperature in °R
    :param P: Pressure in psia
    :param a: Parameter 'a' (in psia·ft³)
    :param b: Parameter 'b' (in ft³)
    :return: Compressibility factor Z
    """
    # Cubic equation coefficients
    A = (a * P) / (R ** 2 * T ** 2)
    B = (b * P) / (R * T)
    C = (P / (R * T))

    # Cubic equation coefficients for Z (z^3 - Bz^2 + Az - C = 0)
    coef = [1, -B, A, -C]

    # Solve the cubic equation
    roots = np.roots(coef)
    # Only real, positive roots are valid for Z
    real_roots = [root.real for root in roots if root.imag == 0 and root.real > 0]
    if real_roots:
        return min(real_roots)  # Return the smallest real root
    else:
        return None

