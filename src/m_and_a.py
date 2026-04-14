import pandas as pd

class MAScreener:
    def __init__(self):
        # Transaction data structured from the KRITI 2026 M&A Screening table
        self.deals = [
            {
                "transaction": "Wipro acquires Meesho",
                "logic": "Enterprise-grade cloud/AI infrastructure for 7L seller base",
                "synergies_cr": 2200,  # 1,800-2,200 Cr in cloud cost savings
                "risk": "Cultural mismatch between IT services and platform cultures"
            },
            {
                "transaction": "Eternal acquires Urban Company",
                "logic": "Shared hyperlocal delivery network & home-life services fulfillment",
                "synergies_cr": 500,   # 300-500 Cr in logistics savings
                "risk": "Minimal; strong cultural fit with asset-light models"
            },
            {
                "transaction": "HCLTech merges with Eternal (JV)",
                "logic": "Supply chain tech for Blinkit and new domestic revenue stream",
                "synergies_cr": 800,   # 500-800 Cr in logistics optimization
                "risk": "Regulatory scrutiny and governance complexity"
            }
        ]

    def evaluate_deals(self):
        print("--- KRITI 2026: Strategic M&A Screening Analysis ---")
        
        # Ranking based on "Actionability" as per report conclusion
        # The report flags Eternal + Urban Co. as the most accretive
        print("Evaluating potential transactions based on strategic logic and risk...")
        
        for deal in self.deals:
            print(f"\nPotential Deal: {deal['transaction']}")
            print(f"Logic: {deal['logic']}")
            print(f"Projected Synergies: {deal['synergies_cr']} Crore")
        
        print("\n" + "="*50)
        print("TOP RECOMMENDATION: Eternal acquires Urban Company")
        print("RATIONALE: Most actionable transaction; transforms Eternal into a")
        print("comprehensive home-life services platform with high cultural fit.")
        print("="*50)

if __name__ == "__main__":
    screener = MAScreener()
    screener.evaluate_deals()