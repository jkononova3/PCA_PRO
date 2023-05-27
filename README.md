# Principal Component Analysis Documentation

### What is PCA?
Principal component analysis is a clustering algorithm to reduce dimensionality of data. This tool was designed to reduce the dimensionality of SNP genotypes. The output will be a cluster graph of these SNP genotypes.  

The pipeline includes taking a vcf file, performing clustering analysis of the variants, and outputting a graph to show the analysis of the genome in the vcf file. 

### How to install this tool? (Still in process)
This tool is a command line script thus you have to install using 

```
  git clone https://github.com/jkononova3/pca
  cd pca
  make
```

tada! you have officially installed our tool

### Installation of VCFTools and Usage

Documentation: 
https://vcftools.sourceforge.net/man_latest.html

Installation:
https://training.nih-cfde.org/en/latest/Bioinformatic-Analyses/GWAS-in-the-cloud/vcftools_install/

We used VCFTools to convert our VCF File into 3 different files, 
1) .012 - Is a matrix of all the genotypes of individuals with one individual per line and each allele represented by 0, 1, or 2
2) .012.indv - Is a file detailing all individuals in the main file
3) .012.pos - Is a file with all the positions in the main file

__The usage of VCF is to create a matrix to run our PCA on.__

How to Install:
We used Anaconda to install and run our script since it already has all the packages needed for VCF installation. The installation can be a little tricky. A few things to keep in mind. 

You are going to need a few packages for installation:
Link to github question where we got this list of packages: https://github.com/vcftools/vcftools/issues/55

- autoconf
- pkg-config
- libtools
- automake
- zlib

You can either download all of these into conda or use your terminal to download these. We did them in conda because we didn't want to potentially mess up anything in our OS. We also created a completely new environment for this project in conda. 

Again conda is not needed to run this tool, it just makes it easier to have all the packages. 
If you are using conda to make VCF Tools:
Use this command
```
conda install -c bioconda vcftools
```
https://anaconda.org/bioconda/vcftools

If not using conda (in terminal):
```
git clone https://github.com/vcftools/vcftools.git
cd vcftools
./autogen.sh
./configure
make
sudo make install
```

https://training.nih-cfde.org/en/latest/Bioinformatic-Analyses/GWAS-in-the-cloud/vcftools_install/

### How to use this tool?

Once you have download this tool you have to run with this command:

After cd'ing into your directory with the vcf file run this command.
```
python pca_1.py -f filename.vcf.gz
```

