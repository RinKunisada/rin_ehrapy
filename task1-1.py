#read csv
import pandas as pd
from anndata import AnnData  

data_path = "data1.csv"

df = pd.read_csv(data_path) #read csv into pandas dataframe
print("CSV file loaded successfully!")

# Preprocess the data
df = df.astype(str)  # Convert all columns to strings for nominal data
df.fillna("unknown", inplace=True)  # Handle missing values

print("Processed DataFrame:")
print(df.head())

# Convert to AnnData
adata = AnnData(df.values)
adata.obs_names = df.index.astype(str)  # Set row indices (e.g., patient IDs)
adata.var_names = df.columns.astype(str)  # Set column names (e.g., clinical variables)

print("AnnData object created:")
print(adata)

# Save the AnnData object
adata_path = "processed1.h5ad"
adata.write(adata_path)
print(f"AnnData object saved to {adata_path}")

# Verify by reloading the AnnData object
adata_reloaded = AnnData.read(adata_path)
print("Reloaded AnnData object:")
print(adata_reloaded)
