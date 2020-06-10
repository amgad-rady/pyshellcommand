#Script to search the filtered files for specifc hits and copy uniques into a new directory.

import re
import os

inputDir = "C:\\programming\\output"
outputDir = "C:\\programming\\output2"

matchString = "java.lang.invoke.CallSite .+;"

outputFilePath = os.path.join(outputDir, "bootstrapMethods.bc")
rawOutFilePath = os.path.join(outputDir, "raw_output.txt")


for dirpath, dirs, files in os.walk(inputDir):
    for file in files:
        filePath = os.path.join(dirpath, file)
        print(filePath)
        with open(filePath, "r") as f:
            for line in f:
                bmMatchList = re.search(matchString, line)
                if bmMatchList is not None:
                    with open(outputFilePath, "a") as o:
                        o.write(file + " " + bmMatchList.group() + "\n")

set = set()

for dirpath, dirs, files in os.walk(outputDir):
    for file in files:
        filePath = os.path.join(dirpath, file)
        print(filePath)
        with open(filePath, "r") as f:
            for line in f:
                #bmMatch = re.split("", line)[1]
                #set.add(bmMatch)
                set.add(line)

with open(rawOutFilePath, "a") as o:
    for s in set:
        o.write(s)
