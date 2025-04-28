import pandas as pd
from wichert_aziz.witchert_aziz import wichert_aziz_correction_v2
from pprint import pprint
from Utility.utility import B12, B13, B14
from mixing_rule.mixing_rule import calculate_mixing_rules  # Import the new function
from EOS.peng_robinson import peng_robinson_eos
from EOS.srk import srk_eos
# from EOS.dranchuk_abou_kassem import solve_for_z_and_ppr, B10 , B11
from EOS.dranchuk_abou_kassem import combined_equation

# Load the composition data
file_path = "./Data-project-02.xlsx"
composition = pd.read_excel(file_path, sheet_name="Composition")
seven_plus_properties = pd.read_excel(file_path, sheet_name="7plus-properties")
tc_pc = pd.read_excel(file_path, sheet_name="tc-pc")
tp = pd.read_excel(file_path, sheet_name="t-p")

# Extract data into dictionaries
composition_dict = composition.set_index("component")["composition"].to_dict()
seven_plus_properties_dict = seven_plus_properties.to_dict(orient="records")[0]
tc_pc_dict = tc_pc.set_index("component").T.to_dict()
tp_dict = tp.iloc[0].to_dict()

# Print the data to inspect
pprint(composition_dict)
print('\n')
pprint(seven_plus_properties_dict)
print('\n')
pprint(tc_pc_dict)
print('\n')
pprint(tp_dict)
print('\n')

# Step 2: C7+ Critical Properties Estimation
# For the C7+ fraction, let's extract the required data
# You may need to adjust this part based on how the data is structured in your file.

# Extracting C7+ properties from the seven_plus_properties_dict or another source
# Example values (replace these with actual data extracted from your dataset)
y_c7_plus = seven_plus_properties_dict.get("y_c7_plus", 0.85)  # This is an assumed molecular weight ratio for C7+
M_c7_plus = seven_plus_properties_dict.get("M_c7_plus", 150)   # This is an assumed molecular weight of C7+

# Calculate Boiling Temperature (T_b) for C7+ using B-14 equation
T_b = B14(M_c7_plus, y_c7_plus)

# Calculate Pseudo-Critical Temperature (T_pc) for C7+ using B-13 equation
T_pc = B13(y_c7_plus, T_b)

# Calculate Pseudo-Critical Pressure (P_pc) for C7+ using B-12 equation
P_pc = B12(y_c7_plus, T_b)

# STEP 2
# Print the calculated C7+ critical properties
print(f"Boiling Temperature (T_b) for C7+: {T_b:.2f} Rankine")
print(f"Pseudo-Critical Temperature (T_pc) for C7+: {T_pc:.2f} Rankine")
print(f"Pseudo-Critical Pressure (P_pc) for C7+: {P_pc:.2f} psia")


# STEP 3
# Apply the Wichert-Aziz adjustment
adjusted_properties = wichert_aziz_correction_v2(composition_dict, seven_plus_properties_dict, tc_pc_dict, tp_dict)

# Display results
print("\nAdjusted Pseudo-Critical Properties:")
print(f"Corrected Tpc: {adjusted_properties['Tpc_corrected']} Rankine")
print(f"Corrected Ppc: {adjusted_properties['Ppc_corrected']} psia")


# Step 4: Mixing Rule Application
mixing_results = calculate_mixing_rules(composition_dict, seven_plus_properties_dict, tc_pc_dict, tp_dict)

# Display mixing results
print("\nMixing Rule Results:")
print(f"a_mix: {mixing_results['a_mix']} psia·ft³")
print(f"b_mix: {mixing_results['b_mix']} ft³")


# Step 5: Calculate Z-factors using SRK and PR EOS
T = tp_dict.get("Temperature", 520)  # Default temperature in °R
P = tp_dict.get("Pressure", 1000)    # Default pressure in psia
a_mix = mixing_results["a_mix"]
b_mix = mixing_results["b_mix"]

# SRK EOS Z-factor calculation
z_srk = srk_eos(T, P, a_mix, b_mix, T, P)
print(f"\nZ-factor (SRK): {z_srk:.4f}")

# PR EOS Z-factor calculation
z_pr = peng_robinson_eos(T, P, a_mix, b_mix)
print(f"Z-factor (PR): {z_pr:.4f}")



coefficients = [
        0.3265, -1.0700, -0.5339, 0.01569, -0.05165, 0.5475, -0.7361, 0.1844, 0.1056, 0.6134, 0.7210
    ]

P_pr = P / adjusted_properties['Ppc_corrected']  # Example pseudo-reduced pressure
T_pr = T / adjusted_properties['Tpc_corrected']  # Example pseudo-reduced temperature

print("Ppr :", P_pr)
print("Tpr :", T_pr)
# try:
#     z, p_pr = solve_for_z_and_ppr(P_pr, T_pr, coefficients)
#     print(f"Converged z: {z:.6f}")
#     print(f"Converged p_pr: {p_pr:.6f}")
# except ValueError as e:
#     print(e)

z_value = combined_equation(P_pr, T_pr, coefficients)
print("Calculated compressibility factor z:", z_value)
