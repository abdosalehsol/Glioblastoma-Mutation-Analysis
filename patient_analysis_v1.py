import pandas as pd

# Load patient dataset
df = pd.read_csv("patient_mutations.csv")

print("\nGlioblastoma Patient Dataset\n")

print(df)

print("\n====================")

print("Number of patients:")

print(len(df))