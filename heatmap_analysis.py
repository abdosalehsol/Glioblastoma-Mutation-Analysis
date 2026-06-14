import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("patient_mutations.csv")

# Convert mutations to numbers

df["TP53"] = df["TP53"].apply(lambda x: 1 if x == "Mutated" else 0)

df["EGFR"] = df["EGFR"].apply(lambda x: 1 if x == "Amplified" else 0)

df["IDH1"] = df["IDH1"].apply(lambda x: 1 if x == "R132H" else 0)

df["PTEN"] = df["PTEN"].apply(lambda x: 1 if x == "Deleted" else 0)

df["TERT"] = df["TERT"].apply(lambda x: 1 if x == "Mutated" else 0)

heatmap_data = df[["TP53","EGFR","IDH1","PTEN","TERT"]]

plt.figure(figsize=(8,6))

plt.imshow(
    heatmap_data,
    aspect="auto"
)

plt.colorbar(label="Mutation Status")

plt.xticks(
    range(len(heatmap_data.columns)),
    heatmap_data.columns
)

plt.yticks(
    range(len(df)),
    df["Patient_ID"]
)

plt.title("Glioblastoma Mutation Heatmap")

plt.savefig("heatmap.png")

print("Heatmap saved successfully")