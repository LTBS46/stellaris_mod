import sys
import os.path

print(sys.argv[1].rsplit(os.path.extsep,1)[0])