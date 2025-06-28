import os
from cryptography.fernet import Fernet
import hashlib
import getpass

# File paths
base_dir = os.path.dirname(os.path.abspath(__file__))
password_file = os.path.join(base_dir, "passwords.txt")
key_file = os.path.join(base_dir, "key.txt")
master_file = os.path.join(base_dir, "master.key")

def create_master_password():
    master = getpass.getpass("Set your master password: ")
    hash_master = hashlib.sha256(master.encode()).hexdigest()
    with open(master_file, "w") as f:
        f.write(hash_master)
    print("Master password set successfully!")
    
def verify_master_password():
    if not os.path.exists(master_file):
        create_master_password()

    while True:
        master = getpass.getpass("Enter master password: ")
        hash_master = hashlib.sha256(master.encode()).hexdigest()

        with open(master_file, "r") as f:
            saved_hash = f.read()

        if hash_master == saved_hash:
            print("Access granted ✅")
            return 
        else:
            print("Wrong master password ❌")

def write_key():
    key = Fernet.generate_key()
    with open(key_file, "wb") as f:
        f.write(key)

def load_key():
    with open(key_file, "rb") as f:
        return f.read()

if not os.path.exists(key_file):
    write_key()
key = load_key()
fer = Fernet(key)

def view():
    if not os.path.exists(password_file):
        print("No passwords found.")
        return

    with open(password_file, "r") as f:
        for line in f:
            data = line.strip()
            if " | Password is " in data:
                try:
                    name, enc_pass = data.split(" | Password is ")
                    name = name.replace("Name is ", "").strip()
                    password = fer.decrypt(enc_pass.encode()).decode()
                    print(f"Name: {name}, Password: {password}")
                except:
                    print("Error decrypting a password.")
            else:
                print("Skipped malformed line:", data)

def add():
    name = input("Enter name: ")
    password = getpass.getpass("Enter your password: ")
    encrypted = fer.encrypt(password.encode()).decode()

    with open(password_file, "a") as f:
        f.write(f"Name is {name} | Password is {encrypted}\n")
    print("Password saved.")

def remove():
    if not os.path.exists(password_file):
        print("No passwords found.")
        return

    name = input("Enter name to remove: ").strip()
    with open(password_file, "r") as f:
        lines = f.readlines()

    with open(password_file, "w") as f:
        removed = False
        for line in lines:
            if not line.startswith(f"Name is {name} |"):
                f.write(line)
            else:
                removed = True

    if removed:
        print(f"Removed password for {name}.")
    else:
        print(f"No entry found for {name}.")

def remove_all():
    if os.path.exists(password_file):
        os.remove(password_file)
        print("All passwords deleted.")
    else:
        print("No passwords found.")
        

verify_master_password()
while True:
    mode = input("Choose mode (add/view/remove/remove_all), or 'q' to quit: ").lower().strip()

    if mode == 'q':
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "remove":
        remove()
    elif mode == "remove_all":
        remove_all()
    else:
        print("Invalid option.")
