import math


def B11(P_pr, T_pr, z):
    """
    Calculate a component for Equation B-10.
    """
    p_pr = 0.27 * (P_pr / z * T_pr)
    return p_pr


def B10(T_pr, p_pr, coefficients):


    """
    Calculate compressibility factor z using Equation B-10.
    A: List of coefficients [A1, A2, ..., A7].
    T_pr: Pseudo-reduced temperature.
    p_pr: Pseudo-reduced pressure.
    """
    A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11 = coefficients
    z = (
            1 + (A1 + A2 / T_pr + A3 / T_pr ** 3 + A4 / T_pr ** 4 + A5 / T_pr ** 5)*p_pr
            + (A6 + A7 / T_pr + A8/T_pr ** 2) * p_pr**2
            - A9 * (A7/T_pr + A8/T_pr**2) * p_pr**5
            + A10 * (1 + A11 * (p_pr**2)) * (p_pr**2 / T_pr ** 3) * math.exp(-A11 * (p_pr ** 2))
    )
    return z

def B12(y_c7_plus, T_b):
    """
    Calculate pseudo-critical pressure P_pc using Equation B-12.
    y_c7_plus: Molecular weight ratio of C7+.
    T_b: Boiling temperature in Rankine.
    """
    P_pc = math.exp(
        8.3634 - 0.0566 * y_c7_plus
        - 0.24244 * y_c7_plus ** 2
        + 0.11857 * y_c7_plus ** 3
        - 0.4627 * math.log10(y_c7_plus)
        - 0.42019 * y_c7_plus / T_b
    )
    return P_pc


def B13(y_c7_plus, T_b):
    """
    Calculate pseudo-critical temperature T_pc using Equation B-13.
    """
    T_pc = 341.7 + 0.4244 * y_c7_plus + 0.1174 * T_b - 3.2623 * (y_c7_plus / T_b)
    return T_pc


def B14(M_c7_plus, y_c7_plus):
    """
    Calculate boiling temperature T_b using Equation B-14.
    """
    T_b = 547.58 * (M_c7_plus ** 0.15178) * (y_c7_plus ** -0.13147)
    return T_b


def B17(A, B):
    """
    Calculate epsilon using Equation B-17.
    """
    epsilon = 120 * (A ** 0.9 - A ** 1.6) + 15 * (B ** 0.5 - B ** 4)
    return epsilon


# Example usage
def main():
    # Example constants and inputs
    T_pr = 1.5
    p_pr = 1.2
    A_coefficients = [
        0.3265, -1.0700, -0.5339, 0.01569, -0.05165, 0.5475, -0.7361, 0.1844, 0.1056, 0.6134, 0.7210
    ]

    y_c7_plus = 0.85
    M_c7_plus = 150
    T_b = B14(M_c7_plus, y_c7_plus)

    # Calculations
    z = B10(T_pr, p_pr, A_coefficients)
    P_pc = B12(y_c7_plus, T_b)
    T_pc = B13(y_c7_plus, T_b)
    epsilon = B17(1.5, 2.0)

    # Output results
    print(f"Compressibility Factor (z): {z:.4f}")
    print(f"Pseudo-critical Pressure (P_pc): {P_pc:.4f}")
    print(f"Pseudo-critical Temperature (T_pc): {T_pc:.4f}")
    print(f"Epsilon: {epsilon:.4f}")


if __name__ == "__main__":
    main()
