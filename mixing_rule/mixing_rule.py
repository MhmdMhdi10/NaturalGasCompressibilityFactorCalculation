# mixing_rule.py
import math


def calculate_mixing_rules(composition_dict, seven_plus_properties_dict, tc_pc_dict, tp_dict):
    """
    Calculate the mixture parameters (a_mix and b_mix) using mixing rules.

    :param composition_dict: Dictionary of component compositions (mole fractions).
    :param seven_plus_properties_dict: Properties dictionary for heptanes plus (e.g., molecular weight and specific gravity).
    :param tc_pc_dict: Dictionary of pseudo-critical properties (Tc and Pc) for each component.
    :param tp_dict: Dictionary of temperature and pressure data (current system conditions).
    :return: Dictionary with a_mix and b_mix.
    """
    R = 10.7316  # Universal gas constant (ft³·psia/(lbmol·°R))

    # Extract current temperature and pressure from tp_dict
    T = tp_dict.get("temperature", 520)  # Default to 520 °R if not found
    P = tp_dict.get("pressure", 1000)  # Default to 1000 psia if not found

    # Calculate a_i and b_i for each component
    a_values = {}
    b_values = {}
    for component, mole_fraction in composition_dict.items():
        # Get critical properties for the component
        props = tc_pc_dict.get(component, {})
        Tc = props.get("tc")
        Pc = props.get("pc")

        # Skip if critical properties are missing
        if Tc is None or Pc is None or Tc == "-" or Pc == "-":
            continue

        Tc = float(Tc)
        Pc = float(Pc)

        # Calculate a_i and b_i for the component
        a = (0.42748 * R ** 2 * Tc ** 2) / Pc
        b = (0.08664 * R * Tc) / Pc

        a_values[component] = a
        b_values[component] = b

    # Calculate a_mix and b_mix using Van der Waals mixing rules
    a_mix = 0
    b_mix = 0
    total_composition = sum(composition_dict.values())

    for i, mole_fraction_i in composition_dict.items():
        fraction_i = mole_fraction_i / total_composition
        b_mix += fraction_i * b_values.get(i, 0)

        for j, mole_fraction_j in composition_dict.items():
            fraction_j = mole_fraction_j / total_composition
            a_i = a_values.get(i, 0)
            a_j = a_values.get(j, 0)
            # Binary interaction coefficient (default 0 if not provided)
            k_ij = 0
            a_mix += fraction_i * fraction_j * math.sqrt(a_i * a_j) * (1 - k_ij)

    return {"a_mix": round(a_mix, 4), "b_mix": round(b_mix, 4)}
