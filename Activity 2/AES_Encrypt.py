# prompt user for username and password then prompt to encrypt or decrypt
import sys

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad




key = b'12345678abcdefgh'  # This is your key

# takes in a key and plain text and returns the cipher text

# plain text -> encoded -> padded to block size (16 bytes) -> encrypted -> encoded -> cipher text

def encrypt(key, plain_text):
    cipher = AES.new(key, AES.MODE_CBC)                             # create a cipher object using the key
    
    padded_plain_text = pad(plain_text.encode(), AES.block_size)    # pad the encoded plain text to be a multiple of 16 bytes
    
    cipher_bytes = cipher.encrypt(padded_plain_text)                # encrypt the padded plain text bytes
    
    return cipher_bytes.decode()                                    # return the cipher text as a string


# code golf version of encrypt
def encrypt_concise(key, plain_text):
    return AES.new(key, AES.MODE_CBC).encrypt(pad(plain_text.encode(), AES.block_size)).decode()


# takes in a key and cipher text and returns the plain text
def decrypt(key, cipher_text):
    cipher = AES.new(key, AES.MODE_CBC) # create a cipher object using the key
    
    padded_bytes = cipher.decrypt(cipher_text.encode()) # decrypt the encoded cipher text 
    
    unpadded_bytes = unpad(padded_bytes, AES.block_size) # unpad the decrypted bytes
    
    plain_text = unpadded_bytes.decode() # convert plain text to string
    
    return plain_text

def decrypt_concise(key, cipher_text):
    return AES.new(key, AES.MODE_CBC).decrypt(cipher_text).decode()

def get_login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return username, password

def get_choice():
    try:
        choice = input("Would you like to encrypt or decrypt? (e/d): ")
        if choice == 'e' or choice == 'd':
            return choice
    except ValueError:
        print("Please enter a valid choice.")
        get_choice()

# define the main function
def main(key):
    username, password = get_login()
    choice = get_choice()
    if choice == 'e':
        print("Encrypting...")
        encrypted_username = encrypt(key, username)
        encrypted_password = encrypt(key, password)
        print("Encrypted username: " + encrypted_username)
        print("Encrypted password: " + encrypted_password)
        
    elif choice == 'd':
        print("Decrypting...")
        decrypted_username = decrypt(key, username)
        decrypted_password = decrypt(key, password)
        print("Decrypted username: " + decrypted_username)
        print("Decrypted password: " + decrypted_password)
        
    else:
        print("Please enter a valid choice.")
        get_choice()
    sys.exit(0)


# call the main function
if __name__ == '__main__':
    main(key)
