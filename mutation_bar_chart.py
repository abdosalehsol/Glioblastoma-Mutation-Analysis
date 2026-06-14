import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("patient_mutations.csv")

mutation_counts = {
    "TP53": (df["TP53"] == "Mutated").sum(),
    "EGFR": (df["EGFR"] == "Amplified").sum(),
    "IDH1": (df["IDH1"] == "R132H").sum(),
    "PTEN": (df["PTEN"] == "Deleted").sum(),
    "TERT": (df["TERT"] == "Mutated").sum()
}

print(mutation_counts)

plt.figure(figsize=(8,5))
plt.bar(mutation_counts.keys(), mutation_counts.values())

plt.title("Glioblastoma Mutation Frequency")
plt.xlabel("Genes")
plt.ylabel("Number of Patients")

plt.tight_layout()
plt.savefig("mutation_bar_chart.png")

print("Chart saved successfully")