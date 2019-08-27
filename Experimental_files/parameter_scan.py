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
#print(params)

outputfile=re.sub(".dat","_exp.dat",re.sub("\A([\S]+)/",'output/',inputfile))
print("output_exp: "+outputfile)

with open(outputfile,'w') as fout:
    fout.write("#m [GeV]  tau [ps] BRexp(B+->K+mumu)\n")

for i in range(params.shape[0]):
	cmd="root -b -q  BRmtau.C'({mass},{tau},\"{outfile}\")'".\
            format(mass=params[i,0]*10**3,tau=params[i,2],outfile=outputfile)
	subprocess.call([cmd],shell=True)

# calculates if BRtheory is allowed and combines together (m, alpha, tau, BRtheory, BRexp, allowed/not allowed)

expparams=genfromtxt(outputfile,  comments="#", delimiter='\t') 

combooutput=re.sub(".dat","_comb.dat",re.sub("\A([\S]+)/",'output_combined/',inputfile))
with open(combooutput,'w') as foutcomb:
print("output_comb: "+combooutput)
    allparams=[]
    foutcomb.write("#m [GeV]  alpha  tau [ps] BRtheo(B+->K+mumu) BRexp allowed/excluded(1/0)\n")
    
    for i in range(params.shape[0]):
        ifallowed=0
        if (float(params[i,3])<float(expparams[i,2])):
            ifallowed=1
        newparams=np.append(params[i],[expparams[i,2],ifallowed])
        allparams.append(newparams)
    allparams=np.array(allparams)
    #print(allparams)
    np.savetxt(foutcomb, allparams, fmt='%5e', delimiter='\t')

