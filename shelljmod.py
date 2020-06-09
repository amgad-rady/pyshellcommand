import os

source = "C:\\Program Files\\Java\\jdk-11\\jmods\\"
target = "C:\\programming\\extract-classes\\"

for dirpath, dirs, files in os.walk(source):
    for file in files:
        newDirectory = target + file.replace(".", "\\")
        os.makedirs(newDirectory)
        os.chdir(newDirectory)
        path = "\"%s\"" % os.path.join(dirpath, file)
        os.system("jmod extract " + path)
