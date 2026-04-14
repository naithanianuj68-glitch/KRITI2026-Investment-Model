import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Data from KRITI 2026 Analysis
data = {
    'WACC (%)': [7.5, 8.5, 9.5, 11.5, 11.0, 12.0, 13.0, 15.0],
    'Enterprise Value (Cr)': [348000, 304000, 285006, 224000, 74000, 61000, 57345, 37000],
    'Sector': ['Legacy IT', 'Legacy IT', 'Legacy IT', 'Legacy IT', 'New Age', 'New Age', 'New Age', 'New Age']
}

df = pd.DataFrame(data)

def create_sensitivity_plot():
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid")
    
    # Create the scatter and line plot
    plot = sns.lineplot(data=df, x='WACC (%)', y='Enterprise Value (Cr)', hue='Sector', marker='o', linewidth=2.5)
    
    # Customizing the chart for professional look
    plt.title('Valuation Sensitivity: Legacy IT vs. New Age Tech', fontsize=15, pad=20)
    plt.xlabel('WACC (Cost of Capital %)', fontsize=12)
    plt.ylabel('Enterprise Value (Crore)', fontsize=12)
    
    # Annotating the "New Age" Sensitivity
    plt.annotate('High Sensitivity (-35% EV drop)', xy=(13.0, 57345), xytext=(13.5, 150000),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8))

    plt.tight_layout()
    
    # Save the plot for GitHub README
    plt.savefig('../sensitivity_plot.png')
    print("Plot generated and saved as 'sensitivity_plot.png' in the main folder.")
    plt.show()

if __name__ == "__main__":
    create_sensitivity_plot()