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

# Store results
genes = ["TP53", "EGFR", "IDH1", "PTEN", "TERT"]

counts = [
    tp53_count,
    egfr_count,
    idh1_count,
    pten_count,
    tert_count
]

print("Mutation Counts")
print("----------------")

for gene, count in zip(genes, counts):
    print(gene, ":", count)