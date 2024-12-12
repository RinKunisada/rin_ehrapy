from anndata import AnnData

from anndata import read_h5ad

# Use the read_h5ad function to load the AnnData object
adata_reloaded = read_h5ad("processed1.h5ad")

# Inspect the reloaded AnnData object
print(adata_reloaded)

# Check the data matrix, column names, and row names
print("Data Matrix:")
print(adata_reloaded.X)

print("Column Names (Variables):")
print(adata_reloaded.var_names)

print("Row Names (Observations):")
print(adata_reloaded.obs_names)
