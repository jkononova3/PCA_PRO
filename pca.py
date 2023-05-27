import numpy as np
import pandas as pd
import subprocess
import argparse
import matplotlib.pyplot as plt

# Read in user's input parameters
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required=True)
args = vars(parser.parse_args())
filename = args["file"]

command = 'vcftools --gzvcf' + filename +'--012 --out matrix --temp matrix_files'
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
# vcftools --gzvcf ~/Downloads/gtdata_1000Genomes_pruned.vcf.gz --012 --out matrix
command = 'cd matrix_files'
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
# Read in file for VCF tools 012 genotype matrix
# data = pd.read_table("C:\\Users\\Julia Kononova\\Downloads\\matrix.012")
data = pd.read_table("matrix.012")
#data.head()


# from sklearn.decomposition import PCA
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