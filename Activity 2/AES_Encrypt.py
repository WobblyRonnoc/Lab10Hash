# prompt user for username and password then prompt to encrypt or decrypt
import sys
import pycryptodome as crypto

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
def main():
    username, password = get_login()
    choice = get_choice()
    if choice == 'e':
        print("Encrypting...")
        pass
    elif choice == 'd':
        print("Decrypting...")
        pass
    else:
        print("Please enter a valid choice.")
        get_choice()
    sys.exit(0)


# generate 256 bit key 
def generate_key():
    
    pass

# generate cipher
def generate_cipher():
    pass

# define the encrypt function
def encrypt():
    pass

# define the decrypt function
def decrypt():
    pass

# call the main function
if __name__ == '__main__':
    main()
