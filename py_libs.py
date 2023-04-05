# Python libraries and modules

# Extensive libraries in Python - External collections of useful functions and methods

#Python come with some integrated libraries

#import entire library
# import random
#
# print(random.randint(1, 1000))

#imports function from the library
# from random import random
#
# print(random())

# import math
# num_float = 23.66
#
# print(math.ceil(num_float))
# print(math.floor(num_float))
# print(math.pi)


# Modules
# import os #Operating System
# import datetime, sys
#
# working_dir = os.getcwd()
# print(working_dir)
#
# print(datetime.date.today())
#
# print(sys.path)
#
# def operating_system_information():
#     print(os.cpu_count())
#
# operating_system_information()


#pip - python package manager. 'pip install ***'
import requests

requests_bbc = requests.get("https://www.bbc.co.uk")

print(requests_bbc.status_code)
print(requests_bbc.content)