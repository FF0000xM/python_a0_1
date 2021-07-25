from cryptography.fernet import Fernet
import time
run = True
file =""
keyname=""
keyfile=""

def write_key(key_name):
    #generates a new key
    ts = time.time()
    key = Fernet.generate_key()
    file_name = key_name + ".key"
    #writes key to current directory as key.key !DO!NOT!LOSE!
    with open(file_name,"wb") as key_file:
        key_file.write(key)

def read_key(key_file):
    key_file = key_file + ".key"
    #loads the key from current directory name 'key.key'
    return open(key_file, "rb").read()

def encrypt(filename, key):
    f = Fernet(key)

    with open(filename, "rb") as file:
        #read all file data
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)

    with open(filename,"wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    f = Fernet(key)

    with open(filename, "rb") as file:
        #read all file data
        encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)

    with open(filename,"wb") as file:
        file.write(decrypted_data)

if __name__ == "__main__":

    run = True

    while run == True:
        checklist = input('Would you like to Encrypt or Decrypt? (E/D): ').lower()
        if checklist == 'e':
            file = input('Enter file name: ')
            keyname = input('Name your key file !DO!NOT!LOSE!THIS!: ')
            write_key(keyname)
            key = read_key(keyname)
            encrypt(file, key)
        elif checklist == 'd':
            file = input('Enter file name: ')
            key_file = input('Enter Keyfile name, no .key at the end: ')
            key = read_key(key_file)
            decrypt(file, key)
        elif checklist == 'q':
            run = Fe
            alse
        else: print("Please enter E or D or e or d or Q to (q)uit")
