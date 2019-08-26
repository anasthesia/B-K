import glob
import re
import numpy as np
from numpy import genfromtxt
import subprocess
import sys

inputfile=sys.argv[1]
params = genfromtxt(inputfile,  comments="#", delimiter=' ')
print(params)

outputfile='output/'+re.sub(".dat","_exp.dat",inputfile)
print("output: "+outputfile)

with open(outputfile,'w') as fout:
fout.write("m [GeV]  tau [ps] BR(B+->K+mumu)")

for i in range(masses.shape[0]):
	cmd='root -b'+' && .x BRmtau.C({mass},{tau},{outfile})'.format(mass=,tau=,)+' && .q'
	subprocess.call([cmd],shell=True)
