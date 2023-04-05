#Python scripting

#Easy to understand
#Many libraries
#Large communities
#Language interoportability (Python can talk to other languages and software easily)


#Why do we need scripting?

#Automate repetetive manual tasks using code

#Some examples of things we can write scripts for as DevOps Engineer:

#Python to query a database
#Write script to execute a shell command
#Script to create a backup
#Python script to fetch IP adrresses of an autoscaling
#Script to check the expiry date of an SSL certificate

#Seven in built modules that allow us to do some interesting things:

#sys
#os
#subprocess
#math
#random
#datetime
#json

# sys module

import sys

print(sys.version)

#os module
# import os
# print(os.getcwd())
# os.chdir("D:/PythonProjects")
# print(os.getcwd())
# os.mkdir("new_dir")


# subprocess module
import subprocess

#Be careful to not create infite loop. Automate only after you are happy with the manual process.
subprocess.run(["python", "hello_world.py"])

#math module
import math

pi = math.pi
pi_string = str(pi)
print("The value of pi is " + pi_string)

#random module
import random
random = random.randrange(1, 10)
print(random)

#datetime
import datetime

whatisthedate = datetime.datetime.now()
print(whatisthedate)

#JSON module
import json

# x = {
#     "name": "John",
#     "age": 36,
#     "city": "London"
# }
#
# y = json.dumps(x)
#
# print(y)

