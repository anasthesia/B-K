import glob
import re
import numpy as np
from numpy import genfromtxt
import subprocess
import sys

#run python file-with-masses&taus. Output stored in the output folder

#reads m and tau from input file, runs root macro to get BR and writes (m, tau, BRexp) to a file 
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

# calculates if BRtheory is allowed and combines together (m, alpha, tau, BRtheory, BRexp, allowed/not allowed)

expparams=genfromtxt(outputfile,  comments="#", delimiter='\t') 

for i in range(params.shape[0]):
    ifallowed=0
    if (params[i,3]<expparams[i,2]):
        ifallowed=1

combinedoutput=re.sub(".dat","_comb.dat",re.sub("\A([\S]+)/",'output_combined/',inputfile))
