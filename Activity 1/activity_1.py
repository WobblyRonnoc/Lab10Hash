import zipfile
import sys
import os

# Check for the correct number of arguments
if len(sys.argv) != 2:
    print("Usage: unzip_rename.py <zipfile>")
    sys.exit(1)

# Unzips the file from the command line argument and renames each file inside
zip_file = sys.argv[1]

prompt = "Would you like to run hash_md5.py on the provided zip file before altering its contents? (y/n)"
if input(prompt) == 'y':
    os.system(f"python hash_md5.py {zip_file}")
else:
    print("Continuing...")
    pass

# Get the base name of the zip file
new_dir = os.path.basename(zip_file).replace('.zip', '')

# Create a directory for the extracted files, unzip the files into it, and rename the files
print(f"Extracting {zip_file} to {new_dir}...")
os.makedirs(new_dir, exist_ok=True)

with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(path=new_dir)

print(f"Renaming .txt files in {new_dir}...")
for file in os.listdir(new_dir):
    if file.lower().endswith('.txt'):
        os.rename(os.path.join(new_dir, file), os.path.join(new_dir, file.replace('.txt', '_renamed.txt')))
zip_ref.close()

# Create a new zip file with the renamed .txt files directly in the root of the archive
print(f"Zipping {new_dir} into {new_dir}.zip...")
with zipfile.ZipFile(f'{new_dir}.zip', 'w') as zip_ref:
    for file in os.listdir(new_dir):
        zip_ref.write(os.path.join(new_dir, file), os.path.basename(file))
zip_ref.close()

print(f"Deleting {new_dir}...")
# delete the new directory and its contents
for file in os.listdir(new_dir):
    os.remove(os.path.join(new_dir, file))
os.rmdir(new_dir)

print(f"Done! {new_dir}.zip created.")

prompt = "Would you like to run hash_md5.py on the new zip file? (y/n)"
if input(prompt) == 'y':
    os.system(f"python hash_md5.py {new_dir}.zip")
else:
    print("Exiting...")
    exit(0)
