#!/usr/bin/env python3
import subprocess
import re

def getMissingDLL(filename):
    libraries=[]
    lddout=subprocess.check_output(["ldd", filename]).split("\n")
    for line in lddout:
        if re.search("not found", line):
            libraries.append(line.split()[0])
    return libraries

def findPackages(fileNames):
    aptProcess=subprocess.Popen(["apt-file","-lf","search"],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    out,err=aptProcess.communicate(b"\n".join(fileNames))
    return list(filter(lambda x:x!=b'',out.split(b"\n")))

if __name__=="__main__":
    infilename="ninja-bin32"
    staticObjects=getMissingDLL(infilename)
    packageNames=findPackages(staticObjects)
    print(packageNames)
    
    
    
