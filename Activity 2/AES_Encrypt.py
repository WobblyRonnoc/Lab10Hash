# prompt user for username and password then prompt to encrypt or decrypt
import sys

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode



key = b'12345678abcdefgh'  # This is your key

# takes in a key and plain text and returns the cipher text

# plain text -> encoded -> padded to block size (16 bytes) -> encrypted -> encoded -> cipher text
# Function to encrypt a string and return the ciphertext
def encrypt(key, plain_text):
    cipher = AES.new(key, AES.MODE_CBC)
    padded_plain_text = pad(plain_text.encode(), AES.block_size)
    cipher_text_bytes = cipher.encrypt(padded_plain_text)
    cipher_text = b64encode(cipher_text_bytes).decode()
    return cipher_text

# Function to decrypt the ciphertext and return the original plaintext
def decrypt(key, cipher_text):
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text_bytes = b64decode(cipher_text)
    padded_plain_text_bytes = cipher.decrypt(cipher_text_bytes)
    plain_text = unpad(padded_plain_text_bytes, AES.block_size).decode()
    return plain_text

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
