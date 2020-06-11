#Script to disassemble Java .class files into bytecode .bc files

import re
import os

path = "c:\\programming\\extract-classes"

for dirpath, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".class"):
            absPath = os.path.join(dirpath, file)
            newFile = re.split(r"\.", absPath)[0]
            if not os.path.exists(newFile + ".bc"):
                os.system("javap -verbose " + newFile + ".class > " + newFile + ".bc")
                print("The file " + newFile + ".class is now disassembled")
            else:
                print("The file " + newFile + ".bc already exists")
