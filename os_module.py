#OS module

#Basic use of OS module

import os
import shutil

#prints message to terminal
os.system('echo "Hello World!"')

# os module to manipulate directories

#Directory
directory = "test_dir"

#Path to parent directory
parent_dir = "D:/PythonProjects"

#Path
path = os.path.join(parent_dir, directory)

# #Create the dir
# os.mkdir(path)
# print("Directory '% s' created" % directory)

#Put a file in the new directory

file_name = "testfile.txt"
file_path = os.path.join(path, file_name)

with open(os.path.join(path, file_name), "w") as file1:
    toFile = "content of the file is written here"
    file1.write(toFile)
print("File " + file_name + " created in " + directory + " folder")


