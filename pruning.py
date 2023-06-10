import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required=True)
args = vars(parser.parse_args())
filename = args["file"]

command = 'mkdir pruned'
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

command = 'cd pruned'
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

command = 'plink ' + filename + ' --indep-pairwise 50 5 0.2 --out pruned_files'
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

command = 'plink --vcf ' + filename + ' --double-id --allow-extra-chr --extract pruned_files.prune.in --make-bed --out pruned'
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()


command = 'plink --bfile pruned --recode vcf --out pruned_data'
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

command = 'bgzip -c pruned_data.vcf > pruned_data.vcf.gz'
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()