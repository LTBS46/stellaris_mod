from sys import path
from os.path import join, realpath

print(realpath(join(path[5],'..\\Scripts')))