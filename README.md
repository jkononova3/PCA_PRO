# PCA_PRO Documentation

### What is PCA?
PCA (Principal Component Analysis) is is a popular dimensionality reduction method that can be used to analyze large datasets that contain a high number of dimensions per observation. PCA increases data interpretability by reducing the dataset’s dimensionality, and using the principal components to visualize this simplified data while minimizing information loss.
This tool was designed to reduce the dimensionality of SNP genotypes. 

### Installation
This script can be installed via the following command line prompts:  

```
  git clone https://github.com/jkononova3/PCA_PRO
  cd PCA_PRO
  make
```

### Usage

Once the tool has been installed, change your working directory to the one containing your VCF file of interest.

Execute the script from the command line as follows:
```
python pca_pro.py -f [--file] -z [--gzipped] -n [--pc_num] -t [--tabs]
```
Example:
```
python pca_pro.py -f gtdata_1000Genomes_pruned.vcf.gz -z -n 5 -t 
```
#### Input

An overview of the parameters:
| Flag Name | Argument Name | Description                                                                                                                                                                                             |
|-----------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -f        | --file        | This argument should be followed by the path to the VCF or gzipped VCF file. - If the file is located in your current working directory, a relative path can be used. Use an absolute path otherwise.   |
| -z        | --gzipped     | The inclusion of this argument indicates that the input is a gzipped VCF file; omit if the VCF file is *not* gzipped.                                                                                   |
| -n        | --pc_num      | This argument should be followed by the desired number of principal components to conduct PCA. If omitted, 20 principal components will be used by default.                                             |
| -t        | --tabs        | The inclusion of this argument will produce a tab-delimited file of eigenvalues. If omitted, the eigenvalues file will be space-delimited by default.                                                   |

#### Output
The script will generate a matrix_files folder in your working directory, containing the following matrix files:
1) .012 - matrix of all the genotypes of individuals with one individual per line and each allele represented by 0, 1, or 2
2) .012.indv - details all individuals in the main file
3) .012.pos - contains all the positions in the main file

Within the matrix_files folder, an additional eigen_values folder contains:
1) eigenvectors.txt -- a text file containing all computed eigenvectors
2) eigenvalues.txt -- a text file containing all computed eigenvalues
3) projected.txt -- a text file containing the data transformed according to the PCA projection
4) PC_1_v_2.png -- an image with the scatterplot displaying any correlation between principal components 1 and 2

### Debugging
If you come upon an error indicating that you have missing (NaN) valus or INF values, use our pruning step to prune your data to get rid of those values. 
Execute the script from the command line as follows:
```
python pruning.py -f [filename.vcf.gz]
```
This will return a pruned_data.vcf.gz file in a folder called pruned, please take this file out and put it in the same folder as the pca_1.py file. Now it should run without a hitch.

For the pruning to work we used PLINK thus please make sure PLINK is installed whereever this script is running so you don't run into any major problems. We would also like to add that we have included the pruning steps as a jupyter notebook as well. If you are from CSE 185 and have access to the datahub it may be easier to use the notebook since the datahub already has PLINK access.


### Detour: Installation and Usage of VCF Tools

Documentation: 
https://vcftools.sourceforge.net/man_latest.html

Installation:
https://training.nih-cfde.org/en/latest/Bioinformatic-Analyses/GWAS-in-the-cloud/vcftools_install/

We used VCF Tools for the conversion from VCF to matrix files.

__VCF is used to create a matrix for our PCA run.__

Install:
We used Anaconda to install and run our script, since it already has all the packages needed for VCF installation.

- List of required packages: https://github.com/vcftools/vcftools/issues/55
- VCF Tools installation using conda: https://anaconda.org/bioconda/vcftools
- VCF Tools installation using command line: https://training.nih-cfde.org/en/latest/Bioinformatic-Analyses/GWAS-in-the-cloud/vcftools_install/
