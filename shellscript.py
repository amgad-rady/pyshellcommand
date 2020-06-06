import re
import os

path = "c:\\programming\\extract-classes"

for dirpath, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".class"):
            absPath = os.path.join(dirpath, file)
            newFile = re.split(r"\.", absPath)[0]
            os.system("javap -verbose " + newFile + ".class > " + newFile + ".bc")
