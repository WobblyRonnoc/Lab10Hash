# Lab 10 Connor MacNeil
import hashlib
import sys
import os

# get the zip file from the command line argument
zip_file = sys.argv[1]

# get the name of the zip file
file_name = os.path.basename(zip_file)

# create an md5 hash object using the hashlib module
m = hashlib.md5()

# read the zip file in binary mode and update the hash object
m.update(open(zip_file, 'rb').read())

# print the md5 hash of the zip file
print(f"\nmd5 hash of {file_name}: {m.hexdigest()}\n")