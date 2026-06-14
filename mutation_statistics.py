import pandas as pd

df = pd.read_csv("patient_mutations.csv")

genes = ["TP53", "EGFR", "IDH1", "PTEN", "TERT"]

print("\nMutation Statistics\n")

for gene in genes:
    mutated = (df[gene] != "Wildtype").sum()
    percentage = mutated / len(df) * 100

    print(f"{gene}:")
    print(f" Mutated Patients = {mutated}")
    print(f" Percentage = {percentage:.1f}%")
    print()