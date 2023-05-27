# Principal Component Analysis Documentation

### What is PCA?
Principal component analysis is is a popular dimensionality reduction method that can be used to analyze large datasets that contain a high number of dimensions per observation. PCA increases data interpretability by reducing the dataset’s dimensionality, and using the principal components to visualize this simplified data while minimizing information loss.
This tool was designed to reduce the dimensionality of SNP genotypes. The output will be a scatterplot cluster graph of these SNP genotypes.  

The pipeline includes taking a VCF.GZ-formatted file, performing clustering analysis of the variants, and outputting a scatterplot that displays the PCA-computed clusters of the genome. 

### How to install this tool?
This script can be installed via the following command line prompts:  

```
  git clone https://github.com/jkononova3/pca
  cd pca
  make
```

### How to use this tool?

Once the tool has been installed, change your working directory to the one containing your VCF.GZ file of interest.

Execute the script from the command line as follows:
```
python pca_1.py -f [filename.vcf.gz]
```

### Detour: Installation and Usage of VCFTools

Documentation: 
https://vcftools.sourceforge.net/man_latest.html

Installation:
https://training.nih-cfde.org/en/latest/Bioinformatic-Analyses/GWAS-in-the-cloud/vcftools_install/

We used VCFTools to convert our VCF File into 3 different files 
1) .012 - Is a matrix of all the genotypes of individuals with one individual per line and each allele represented by 0, 1, or 2
2) .012.indv - Is a file detailing all individuals in the main file
3) .012.pos - Is a file with all the positions in the main file

__VCF is used to create a matrix for our PCA run.__

Install:
We used Anaconda to install and run our script, since it already has all the packages needed for VCF installation.

- List of required packages: https://github.com/vcftools/vcftools/issues/55
- VCF Tools installation using conda: https://anaconda.org/bioconda/vcftools
- VCF Tools installation using command line: https://training.nih-cfde.org/en/latest/Bioinformatic-Analyses/GWAS-in-the-cloud/vcftools_install/
