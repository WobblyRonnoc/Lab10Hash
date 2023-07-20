# unzips the file from the command line argument
# renames each file inside
# zips the directory and its contents into a new zip file
# prompts the user to run hash_md5.py on the new zip file

import zipfile
import sys
import os

#extract the zip file from the command line argument and rename each file inside
zip_file = sys.argv[1]

prompt = "Would you like to run hash_md5.py on the provided zip file before altering it's contents? (y/n)"

if input(prompt) == 'y':
    os.system(f"python hash_md5.py {zip_file}")
else:
    print("Continuing...")
    pass

#get the base name of the zip file
new_dir = os.path.basename(zip_file).replace('.zip', '')

# check for the correct number of arguments
if len(sys.argv) != 2:
    print("Usage: unzip_rename.py <zipfile>")
    sys.exit(1)

#? main program

# create a directory for the extracted files
# unzip the files into it
# rename the files
# zip the directory and its contents into a new zip file

print(f"Extracting {zip_file} to {new_dir}...")
os.makedirs(new_dir, exist_ok=True)



with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(path=new_dir)
    
print(f"Renaming files in {new_dir}...")
for file in os.listdir(new_dir):
    os.rename(os.path.join(new_dir, file), os.path.join(new_dir, file.replace('.txt', '_renamed.txt')))
zip_ref.close()


print (f"Zipping {new_dir} into {new_dir}.zip...")

# zip the created directory and its contents into a new zip file
with zipfile.ZipFile(f'{new_dir}.zip', 'w') as zip_ref:
    for file in os.listdir(new_dir):
        zip_ref.write(os.path.join(new_dir, file))
zip_ref.close()

print (f"Deleting {new_dir}...")
# delete the new directory and its contents
for file in os.listdir(new_dir):
    os.remove(os.path.join(new_dir, file))
os.rmdir(new_dir)

print(f"Done! {new_dir}.zip created.")

prompt = "would you like to run hash_md5.py on the new zip file? (y/n)"
if input(prompt) == 'y':
    os.system(f"python hash_md5.py {new_dir}.zip")
else:
    print("Exiting...")
    exit(0)


