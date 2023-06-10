import sys
import numpy as np
import pandas as pd
import subprocess
import argparse
import matplotlib.pyplot as plt

# Read in user's input parameters
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required=True)
parser.add_argument('-z', "--gzipped", action='store_true')
parser.add_argument('-n',"--pc_num", nargs='?', const=20, type=int, default=20)
parser.add_argument('-t',"--tabs", action='store_true')

args = vars(parser.parse_args())
filename = args["file"]
if_zipped = args["gzipped"]
num_components = args["pc_num"]
if_tab = args["tabs"]

command = 'mkdir pca_pro_files'
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

command = 'cd pca_pro_files'
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

command = 'mkdir matrix_files'
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

if(if_zipped):
    command = 'vcftools --gzvcf ' + filename +' --012 --out matrix --temp matrix_files'
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
else:
    command = 'vcftools --vcf ' + filename +' --012 --out matrix --temp matrix_files'
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
# vcftools --gzvcf ~/Downloads/gtdata_1000Genomes_pruned.vcf.gz --012 --out matrix
command = 'cd matrix_files'
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

# Read in file for VCF tools 012 genotype matrix
# data = pd.read_table("C:\\Users\\Julia Kononova\\Downloads\\matrix.012") -- don't mind this LOL
data = pd.read_table("matrix.012")

data = data.values
data = data[:,1:]
# print(data)

command = 'cd ..'
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

command = 'mkdir eigen_files'
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

# STEP 1: Scale/standardize data by Z-normalizing SNPs (helps reduce effects of rare SNPs)
# normalize by row, using average and standard deviation
mean_val = data.mean(axis=0)
stand_dev = data.std(axis=0)

# normalized data has mean = 0, variance of each SNP = 1
data_norm = (data-mean_val)/stand_dev

# STEP 2: Calc covariance matrix
features = data_norm.T # transposes data array (interchange rows and cols)
covar_matrix = np.cov(features)

#print("array preview: ")
#print(covar_matrix[0:5, 0:5])

# STEP 3: Eigendecomposition of covariance matrix
eig_values, eig_vectors = np.linalg.eig(covar_matrix)

# Adjust eigenvectors with largest magnitudes (abs val) to be positive
max_rows_idx = np.argmax(np.abs(eig_vectors), axis=0) # get indices of maximum rows
signs = np.sign(eig_vectors[max_rows_idx, range(eig_vectors.shape[0])]) # get sign of each element in the max rows
eig_vectors = eig_vectors*signs[np.newaxis,:] # add new dimension with transformed signs
eig_vectors = eig_vectors.T # transpose

#print('Eigenvalues \n', eig_values)
#print('Eigenvectors \n', eig_vectors)

# STEP 4: Rearrange the eigenvectors and eigenvalues

# make list of matched eigenvalue-eigenvector pairings, stored as tuples
eig_pairs = [(np.abs(eig_values[i]), eig_vectors[i,:]) for i in range(len(eig_values))]
# sort tuples in decreasing order based on eigenvalues' magnitude
eig_pairs.sort(key=lambda x: x[0], reverse=True)

# store as separate variables, for the purpose of testing validation + additional calculations we might want to perform later
eig_values_sorted = np.array([x[0] for x in eig_pairs])
eig_vectors_sorted = np.array([x[1] for x in eig_pairs])

# print(eig_pairs)

# STEP 5: Choose principal components (using any given number, using 5 here as default, for testing purposes)
# num_components = 5 # TODO: make customizable with parameter
proj_matrix = eig_vectors_sorted[:num_components, :] # projection matrix

# Step 6: Project the data, using the projection matrix to transform data to have its dimensions = num_components
data_transformed = data_norm.dot(proj_matrix.T)

# Plot the first 2 principal components
plt.scatter(np.negative(data_transformed[:, 0]), data_transformed[:, 1])
plt.xlabel('PC1'); plt.xticks([])
plt.ylabel('PC2'); plt.yticks([])
plt.title('First 2 PCA components')
plt.show()
plt.savefig("PC_1_v_2")

if(if_tab):
    np.savetxt("eigenvectors.txt",eig_vectors_sorted, delimiter='\t')
else:
    np.savetxt("eigenvectors.txt",eig_vectors_sorted)
    
np.savetxt("eigenvalues.txt",eig_values_sorted, delimiter='\n')
# np.savetxt("eigenvectors.txt",eig_vectors_sorted)
np.savetxt("projected.txt", data_transformed)

sys.exit()