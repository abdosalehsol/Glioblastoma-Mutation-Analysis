import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("patient_mutations.csv")

# Count mutations
tp53_count = (df["TP53"] == "Mutated").sum()

egfr_count = (df["EGFR"] == "Amplified").sum()

idh1_count = (df["IDH1"] == "R132H").sum()

pten_count = (df["PTEN"] == "Deleted").sum()

tert_count = (df["TERT"] == "Mutated").sum()

# Labels and values
labels = ["TP53", "EGFR", "IDH1", "PTEN", "TERT"]

sizes = [
    tp53_count,
    egfr_count,
    idh1_count,
    pten_count,
    tert_count
]

# Pie chart
plt.figure(figsize=(8,8))

plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%"
)

plt.title("Glioblastoma Mutation Distribution")

plt.savefig("mutation_pie_chart.png")

print("Pie chart saved successfully")