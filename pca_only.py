import sys
import numpy as np
import pandas as pd
import subprocess
import argparse
import matplotlib.pyplot as plt

# Read in user's input parameters
# Read in file for VCF tools 012 genotype matrix
data = pd.read_table("C:\\Users\\Julia Kononova\\Downloads\\matrix.012")
print(data.head(50))
# data = pd.read_table("matrix.012")
data = data.values
data = data[:,1:]
# print(data)

# Step 1: Scale/standardize data
mean_ = data.mean(axis =0)
std_ = data.std(axis=0)

X_scaled = (data-mean_)/std_

# Step 2: Calc covariance matrix
features = X_scaled.T
cov_matrix = np.cov(features)

#print("array preview: ")
#print(cov_matrix[0:5, 0:5])

# Step 3: Eigendecomposition
eig_values, eig_vectors = np.linalg.eig(cov_matrix)

max_abs_idx = np.argmax(np.abs(eig_vectors), axis=0)
signs = np.sign(eig_vectors[max_abs_idx, range(eig_vectors.shape[0])])
eig_vectors = eig_vectors*signs[np.newaxis,:]
eig_vectors = eig_vectors.T

print('Eigenvalues \n', eig_values)
print('Eigenvectors \n', eig_vectors)

# Step 4: Rearrange the eigenvectors and eigenvalues

# We first make a list of (eigenvalue, eigenvector) tuples
eig_pairs = [(np.abs(eig_values[i]), eig_vectors[i,:]) for i in range(len(eig_values))]

# Then, we sort the tuples from the highest to the lowest based on eigenvalues magnitude
eig_pairs.sort(key=lambda x: x[0], reverse=True)

# For further usage
eig_vals_sorted = np.array([x[0] for x in eig_pairs])
eig_vecs_sorted = np.array([x[1] for x in eig_pairs])

print(eig_pairs)

# Step 5: Choose principal components
n_comp = 5 #k
W = eig_vecs_sorted[:n_comp, :]

# Step 6: Project the data
X_proj = X_scaled.dot(W.T)

# Plot the first 2 principal components
plt.scatter(X_proj[:, 0], X_proj[:, 1])
plt.xlabel('PC1'); plt.xticks([])
plt.ylabel('PC2'); plt.yticks([])
# plt.title('2 components, captures {} of total variation'.format(cum_explained_variance[1]))
plt.title('2 components')
plt.show()

'''
from sklearn.decomposition import PCA
pca = PCA(n_components=5)
pca.fit(data)
print("components: ")
print(pca.components_)
print('explained variance: ')
print(pca.explained_variance_)

data_transformed_sklearn = pca.transform(data)

plt.scatter(data_transformed_sklearn[:,0], data_transformed_sklearn[:,1])
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
'''
'''
import sklearn.decomposition
pca = sklearn.decomposition.PCA()
pca.fit(data)

pc_magnitudes = pca.explained_variance_
pcs = pca.components_
print("PC 1 - magnitude: %s"%pc_magnitudes[0])
print("PC 1: %s"%pcs[0])
print("PC 2 - magnitude: %s"%pc_magnitudes[1])
print("PC 2: %s"%pcs[1])

# Project data onto top PCs:

# Using sklearn transform method
data_transformed_sklearn = pca.transform(data)

# Compare
#fig = plt.figure()
#ax = fig.add_subplot(111)
plt.scatter(data_transformed_sklearn[:,0], data_transformed_sklearn[:,1])
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()

sys.exit()
'''