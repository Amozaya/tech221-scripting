import json
import os
import sys
import yaml

#check there is file passed
if len(sys.argv) > 1:
    #opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()
    #if file isn't found
    else:
        print("Error: " + sys.argv[1] + " not found")
        exit(1)
else:
    print("Wrong execution format")


#processing the conversion
output = yaml.dump(source_content)

target_file = open(sys.argv[2], "w")
target_file.write(output)
target_file.close()