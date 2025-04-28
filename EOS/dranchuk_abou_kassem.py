# import math
#
#
# def B11(P_pr, T_pr, z):
#     """
#     Calculate a component for Equation B-10.
#     """
#     p_pr = 0.27 * (P_pr / z * T_pr)
#     return p_pr
#
#
# def B10(T_pr, p_pr, coefficients):
#     """
#     Calculate compressibility factor z using Equation B-10.
#
#     :param T_pr: Pseudo-reduced temperature (T/Tc).
#     :param p_pr: Pseudo-reduced pressure.
#     :param coefficients: List of coefficients [A1, A2, ..., A11].
#     :return: Compressibility factor z.
#     """
#     A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11 = coefficients
#     z = (
#         1
#         + (A1 + A2 / T_pr + A3 / T_pr ** 3 + A4 / T_pr ** 4 + A5 / T_pr ** 5) * p_pr
#         + (A6 + A7 / T_pr + A8 / T_pr ** 2) * p_pr ** 2
#         - A9 * (A7 / T_pr + A8 / T_pr ** 2) * p_pr ** 5
#         + A10 * (1 + A11 * (p_pr ** 2)) * (p_pr ** 2 / T_pr ** 3) * math.exp(-A11 * (p_pr ** 2))
#     )
#     return z
#
# # range of acceptability 0.2 < ppr < 30 ,  1< tpr < 3
# def solve_for_z_and_ppr(P_pr, T_pr, coefficients, tol=6 * 1e-3, max_iter=10000):
#     """
#     Iteratively solve for z and p_pr using B-10 and B-11.
#
#     :param P_pr: Pseudo-reduced pressure (P/Pc).
#     :param T_pr: Pseudo-reduced temperature (T/Tc).
#     :param coefficients: List of coefficients [A1, A2, ..., A11].
#     :param tol: Tolerance for convergence.
#     :param max_iter: Maximum number of iterations.
#     :return: Converged z and p_pr values.
#     """
#     z = 0.56  # Initial guess for z
#
#     for _ in range(max_iter):
#         p_pr = B11(P_pr, T_pr, z)
#         z_new = B10(T_pr, p_pr, coefficients)
#
#         if abs(z_new - z) < tol:
#             return z_new, p_pr
#
#         z = z_new
#         print(z)
#
#     raise ValueError("Solution did not converge after maximum iterations.")
#
#
# # Example usage
# if __name__ == "__main__":
#     coefficients = [
#         0.3265, -1.0700, -0.5339, 0.01569, -0.05165, 0.5475, -0.7361, 0.1844, 0.1056, 0.6134, 0.7210
#     ]
#
#     P_pr = 8  # Example pseudo-reduced pressure
#     T_pr = 1.3  # Example pseudo-reduced temperature
#
#     try:
#         z, p_pr = solve_for_z_and_ppr(P_pr, T_pr, coefficients)
#         print(f"Converged z: {z:.6f}")
#         print(f"Converged p_pr: {p_pr:.6f}")
#     except ValueError as e:
#         print(e)


import sympy as sp

def combined_equation(P_pr, T_pr, coefficients):
    """
    Combined equation that calculates the compressibility factor z from the given
    parameters P_pr, T_pr, and coefficients.

    The equation to solve is:
    p_pr = 0.27 * (P_pr / (z * T_pr))
    """
    # Extract the coefficients
    A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11 = coefficients

    # Define the symbolic variable for z
    z = sp.symbols('z', positive=True)

    # Calculate p_pr using the given equation
    p_pr = 0.27 * (P_pr / (z * T_pr))

    # Define the compressibility factor z equation
    z_eq = (
        1
        + (A1 + A2 / T_pr + A3 / T_pr ** 3 + A4 / T_pr ** 4 + A5 / T_pr ** 5) * p_pr
        + (A6 + A7 / T_pr + A8 / T_pr ** 2) * p_pr ** 2
        - A9 * (A7 / T_pr + A8 / T_pr ** 2) * p_pr ** 5
        + A10 * (1 + A11 * (p_pr ** 2)) * (p_pr ** 2 / T_pr ** 3) * sp.exp(-A11 * (p_pr ** 2))
    )

    # Create the equation z = z_eq
    equation = sp.Eq(z, z_eq)

    # Solve the equation for z
    solutions = sp.solve(equation, z)

    # Filter out any non-physical solutions (e.g., negative or complex values)
    real_solutions = [sol.evalf() for sol in solutions if sol.is_real and sol > 0]

    return real_solutions


# # Example usage
# P_pr = 8  # Example pseudo-reduced pressure
# T_pr = 1.5  # Example pseudo-reduced temperature
# coefficients = [
#     0.3265, -1.0700, -0.5339, 0.01569, -0.05165, 0.5475, -0.7361, 0.1844, 0.1056, 0.6134, 0.7210
# ]
#
# z_value = combined_equation(P_pr, T_pr, coefficients)
# print("Calculated compressibility factor z:", z_value)
