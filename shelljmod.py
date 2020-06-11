#Script to unpack jmods

import os

source = "C:\\Program Files\\Java\\jdk-11\\jmods\\"
target = "C:\\programming\\extract-classes\\"

for dirpath, dirs, files in os.walk(source):
    for file in files:
        newDirectory = target + file.replace(".", "\\")
        if not os.path.isdir(newDirectory):
            print("Extracting " + file)
            os.makedirs(newDirectory)
            os.chdir(newDirectory)
            path = "\"%s\"" % os.path.join(dirpath, file)
            os.system("jmod extract " + path)
            print("Extracted " + file)
        else:
            print(file + " has already been extracted")
