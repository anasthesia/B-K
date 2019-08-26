import glob
import re
import numpy as np
from numpy import genfromtxt
import subprocess
import sys

#run python file-with-masses&taus. Output stored in the output folder

inputfile=sys.argv[1]
params = genfromtxt(inputfile,  comments="#", delimiter='\t')
print(params)

outputfile=re.sub(".dat","_exp.dat",re.sub("\A([\S]+)/",'output/',inputfile))
print("output: "+outputfile)

with open(outputfile,'w') as fout:
    fout.write("#m [GeV]  tau [ps] BRexp(B+->K+mumu)")

for i in range(params.shape[0]):
	cmd="root -b -q  BRmtau.C'({mass},{tau},\"{outfile}\")'".\
            format(mass=params[i,0]*10**3,tau=params[i,2],outfile=outputfile)
	subprocess.call([cmd],shell=True)
