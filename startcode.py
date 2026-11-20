import os

import pandas as pd

# DF20-Mini: metadata CSVs and the DF20M/ image folder
train = pd.read_csv("DF20M-train_metadata_PROD.csv")
test = pd.read_csv("DF20M-public_test_metadata_PROD.csv")
df = pd.concat([train, test])

print("Images:      ", len(df), f"(train {len(train)}, test {len(test)})")
print("Image files: ", len(os.listdir("DF20M")))
print("Observations:", df["gbifID"].nunique())
print("Species:     ", df["scientificName"].nunique())
print("Genera:      ", df["genus"].nunique())
print()
print(df["genus"].value_counts())
print()
print("Images per species:")
print(df["scientificName"].value_counts().describe())
