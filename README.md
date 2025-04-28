# NaturalGasCompressibilityFactorCalculation

📖 Introduction

This project calculates the compressibility factor (Z) for a natural gas sample at specified pressure and temperature conditions using multiple methods:

    Peng-Robinson (PR) Equation of State

    Soave-Redlich-Kwong (SRK) Equation of State

    Standing-Katz Chart (Dranchuk and Abou-Kassem correlation)

The project also includes the estimation of C7+ critical properties, pseudo-critical property correction using the Wichert-Aziz method, and proper application of EOS mixing rules.
📦 Project Structure

    ├── main.py
    ├── Data/
    │   └── gas_composition.xlsx
    ├── Utilities/
    │   ├── c7plus_properties.py
    │   ├── wichert_aziz_correction.py
    │   ├── mixing_rules.py
    │   ├── eos_peng_robinson.py
    │   ├── eos_srk.py
    │   ├── standing_katz_correlation.py
    └── README.md

⚙️ Installation

Clone the repository:

    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name

Install the required Python packages:

    pip install numpy pandas scipy

🚀 How to Run

Make sure the Excel file with gas composition (gas_composition.xlsx) is located inside the Data/ directory.

Run the main script:

    python main.py

The script will:

    Import gas composition
    
    Estimate C7+ critical properties
    
    Correct mixture pseudo-critical properties
    
    Apply mixing rules
    
    Solve for the compressibility factor (Z) using PR, SRK, and Standing-Katz methods
    
    Results will be printed for comparison.

📊 Example Output

    Peng-Robinson Z-factor: 0.8675
    Soave-Redlich-Kwong Z-factor: 0.8720
    Standing-Katz (Dranchuk-Abou-Kassem) Z-factor: 0.8652

🧮 Methods Used

    Antoine Equation (for vapor pressures, if needed)

    Peng-Robinson EOS (cubic EOS model)

    Soave-Redlich-Kwong EOS (cubic EOS model)

    Wichert-Aziz Correction (for H₂S and CO₂ rich gas mixtures)

    Standing-Katz Chart via Dranchuk-Abou-Kassem correlation

📚 References

    McCain, W. D. Jr., The Properties of Petroleum Fluids, 2nd Edition

    Dranchuk, P.M., Abou-Kassem, J.H., Calculation of Z Factors for Natural Gases Using Equations Fitted to Laboratory Data (1975)

    Wichert, E., Aziz, K., Interpretation of Z-Factor Calculations for Sour Gas Mixtures (1972)
