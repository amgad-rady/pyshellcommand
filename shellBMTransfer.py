#Script to search the filtered files for specifc hits and copy uniques into a new directory.

import re
import os
import collections

inputDir = "C:\\programming\\output"
outputDir = "C:\\programming\\output2"

if not os.path.isdir(outputDir):
    os.makedirs(outputDir)

matchString = "java/.+\..+:(.+)Ljava/lang/invoke/CallSite;"

outputFilePath = os.path.join(outputDir, "bootstrapMethods.bc")
rawOutFilePath = os.path.join(outputDir, "raw_output.txt")

open(outputFilePath, "w")
open(rawOutFilePath, "w")

for dirpath, dirs, files in os.walk(inputDir):
    for file in files:
        filePath = os.path.join(dirpath, file)
        print("Processing file " + filePath)
        with open(filePath, "r") as f:
            for line in f:
                bmMatchList = re.search(matchString, line)
                if bmMatchList is not None:
                    with open(outputFilePath, "a") as o:
                        o.write(bmMatchList.group() + "\n")
                        o.close()
            f.close()

with open(outputFilePath) as infile:
    counts = collections.Counter(line.strip() for line in infile)
    infile.close()
with open(rawOutFilePath, "a") as infile:
    for line, count in counts.most_common():
        infile.write(count.__str__() + " instances of " + line + "\n")
    infile.close()