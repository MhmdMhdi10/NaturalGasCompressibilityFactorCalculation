import math

def wichert_aziz_correction_v2(composition_dict, seven_plus_properties_dict, tc_pc_dict, tp_dict):
    """
    Calculate corrected pseudo-critical temperature and pressure using the Wichert-Aziz equation.

    :param composition_dict: Dictionary of component compositions (e.g., mole fractions of components).
    :param seven_plus_properties_dict: Properties dictionary for heptanes plus (e.g., molecular weight and specific gravity).
    :param tc_pc_dict: Dictionary of pseudo-critical properties for each component.
    :param tp_dict: Dictionary of temperature and pressure data (e.g., current system conditions).
    :return: Corrected Tpc and Ppc as a dictionary.
    """
    # Step 1: Extract H2S and CO2 fractions from composition_dict
    H2S_fraction = composition_dict.get("Hydrogen sulfide", 0.0) / 100  # Convert % to fraction
    CO2_fraction = composition_dict.get("Carbon dioxide", 0.0) / 100    # Convert % to fraction

    # Step 2: Calculate epsilon using B-17 equation
    epsilon = 120 * (H2S_fraction**0.9 - H2S_fraction**1.6) + 15 * (math.sqrt(CO2_fraction) - CO2_fraction**4)

    # Step 3: Calculate uncorrected Tpc and Ppc
    Tpc_uncorrected, Ppc_uncorrected = 0, 0
    total_composition = sum(composition_dict.values())

    for component, mole_fraction in composition_dict.items():
        fraction = mole_fraction / total_composition
        component_props = tc_pc_dict.get(component, {})
        Tc = component_props.get("tc", None)
        Pc = component_props.get("pc", None)

        # Skip if critical properties are missing or not applicable
        if Tc == "-" or Pc == "-":
            continue

        Tpc_uncorrected += fraction * float(Tc)
        Ppc_uncorrected += fraction * float(Pc)

    # Step 4: Apply corrections to Tpc and Ppc
    Tpc_corrected = Tpc_uncorrected - epsilon
    Ppc_corrected = Ppc_uncorrected * math.exp(-epsilon / Tpc_uncorrected)

    # Step 5: Return results
    return {
        "Tpc_corrected": round(Tpc_corrected, 2),
        "Ppc_corrected": round(Ppc_corrected, 2)
    }
