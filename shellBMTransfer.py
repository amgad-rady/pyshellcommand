import re
import os

inputDir = "C:\\programming\\output"
outputDir = "C:\\programming\\output2"

matchString = "[0-9]+: #[0-9]+ REF_.*:"

outputFilePath = os.path.join(outputDir, "bootstrapMethods.bc")
rawOutFilePath = os.path.join(outputDir, "raw_output.bc")


for dirpath, dirs, files in os.walk(inputDir):
    for file in files:
        filePath = os.path.join(dirpath, file)
        print(filePath)
        with open(filePath, "r") as f:
            for line in f:
                bmMatchList = re.search(matchString, line)
                if bmMatchList is not None:
                    with open(outputFilePath, "a") as o:
                        o.write(bmMatchList.group() + "\n")

set = set()

for dirpath, dirs, files in os.walk(outputDir):
    for file in files:
        filePath = os.path.join(dirpath, file)
        print(filePath)
        with open(filePath, "r") as f:
            for line in f:
                bmMatch = re.split("REF_", line)[1]
                set.add(bmMatch)

with open(rawOutFilePath, "a") as o:
    for s in set:
        o.write(s)
