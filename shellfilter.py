#Script to search javap disassembler output for strings (usually type signatures) and copy the hits to a new directory

import os
import shutil

path = "C:\\programming\\extract-classes"
output = "C:\\programming\\output"
searchString = "CallSite"

if not os.path.isdir(output):
    os.makedirs(output)

for dirpath, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".bc"):
            filePath = os.path.join(dirpath, file)
            print("Searching file " + filePath)
            with open(filePath) as f:
                if searchString in f.read():
                    destPath = os.path.join(output, file)
                    shutil.copy(filePath, destPath)
