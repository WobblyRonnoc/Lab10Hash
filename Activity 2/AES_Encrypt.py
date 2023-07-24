# AES Encryption

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

key = b'12345678abcdefgh'  # This is your key (16 bytes)
cipher = AES.new(key, AES.MODE_CBC)  # Create an AES cipher object with the key using the mode CBC

# get the data to encrypt
print("Enter your username and password to encrypt")
username = input("Username: ")
password = input("Password: ")

print("\n\n")
print("\t* encrypting the data".center(50, "="))

# encode the data to bytes
print("\t* encoding username and password to bytes...")
username = username.encode()
password = password.encode()


# pad the user and password so that it is a multiple of 16 bytes
print("\t* padding username and password...")
username = pad(username, AES.block_size)
password = pad(password, AES.block_size)


# encrypt the data
print("\t* encrypting username and password...")
encrypted_username = cipher.encrypt(username)
encrypted_password = cipher.encrypt(password)

# encode the encrypted data to base64 before decoding to utf-8 to
ct_username = b64encode(encrypted_username).decode('utf-8')
ct_password = b64encode(encrypted_password).decode('utf-8')

# get the initialization vector
iv = b64encode(cipher.iv).decode('utf-8')

# print the encrypted data
print('=' * 50)
print(f"Encrypted Username and Password")
print(f"Username: {ct_username}")
print(f"Password: {ct_password}")

# decrypt the data

print("\n\n")
print("Decrypting the data".center(50, "="))


# decode the base64 encoded initialization vector
print("decoding the base64 encoded initialization vector...")
iv = b64decode(iv)

# decode the base64 encoded encrypted ciphertexts
print("decoding the base64 encoded encrypted ciphertexts...")
ct_username = b64decode(ct_username)
ct_password = b64decode(ct_password)

# using the initialization vector, create a new cipher object
print("using the initialization vector to create a new cipher object...")
cipher = AES.new(key, AES.MODE_CBC, iv)

# unpad and decrypt the ciphertexts to get the plaintext username and password
print("unpadding and decrypting the ciphertexts...")
pt_username = unpad(cipher.decrypt(ct_username), AES.block_size)
pt_password = unpad(cipher.decrypt(ct_password), AES.block_size)

# decode the bytes back into strings
print("decoding the bytes back into strings...")
pt_username = pt_username.decode()
pt_password = pt_password.decode()

# print the plaintext username and password
print('=' * 50)
print(f"Decrypted Username and Password")
print(f"Username: {pt_username}")
print(f"Password: {pt_password}")
