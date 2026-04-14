import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Data derived from KRITI 2026 Sensitivity Analysis
# Format: [WACC, Terminal Growth (g), Sector (0=Legacy, 1=NewAge)]
training_data = [
    # HCLTech (Legacy IT - Sector 0)
    [0.095, 0.035, 0], [0.095, 0.025, 0], [0.095, 0.045, 0], [0.085, 0.035, 0], [0.075, 0.035, 0],
    # Eternal (New Age Tech - Sector 1)
    [0.130, 0.050, 1], [0.130, 0.035, 1], [0.130, 0.070, 1], [0.120, 0.050, 1], [0.110, 0.050, 1]
]

# Target: Enterprise Value in Crore
ev_targets = [
    285006, 248000, 314000, 304000, 348000, # HCLTech Values
    57345, 44000, 65000, 61000, 74000      # Eternal Values
]

def run_valuation_model():
    # Convert to Dataframe
    X = np.array(training_data)
    y = np.array(ev_targets)

    # Scaling features is critical for financial regression
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Initialize and Train Linear Regression Model
    model = LinearRegression()
    model.fit(X_scaled, y)

    print("--- KRITI 2026: Investment Analysis Model ---")
    print(f"Model Training Status: Complete")
    
    # Example Prediction: New Age Tech with 14% WACC and 5% Growth
    test_input = scaler.transform([[0.14, 0.05, 1]])
    prediction = model.predict(test_input)
    
    print(f"Predicted EV for High-Risk New Age Tech: {prediction[0]:.2f} Cr")
    print("-" * 45)
    print("CV WORK COMPLETED:")
    print("1. Quantified valuation sensitivity to WACC and Terminal Growth.")
    print("2. Integrated multi-sector DCF logic into a Python-based regressor.")

if __name__ == "__main__":
    run_valuation_model()