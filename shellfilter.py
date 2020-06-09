import os
import shutil

path = "C:\\programming\\extract-classes"
output = "C:\\programming\\output"
searchString = "java.lang.invoke.CallSite"

for dirpath, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".bc"):
            filePath = os.path.join(dirpath, file)
            with open(filePath) as f:
                if searchString in f.read():
                    destPath = os.path.join(output, file)
                    shutil.copy(filePath, destPath)
