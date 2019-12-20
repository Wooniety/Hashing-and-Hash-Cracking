# Import library to hash.
import hashlib

def pick_option(question, *options):
    """General Menu"""
    option_dict = {"0": 0}
    print(question)
    print("0) Exit")
    for i, option in enumerate(options):
        option_dict[str(i+1)] = option
        print(f"{i+1}) {option}")
    choose = input("").strip()
    while choose not in option_dict.keys():
        choose = input("").strip()
    return option_dict[choose]

def hashing(option, string):
    """Hash string in chosen hash"""
    hash_dict = {"md5": hashlib.md5(string.encode()).hexdigest(),
                "sha1": hashlib.sha1(string.encode()).hexdigest(),
                "sha224": hashlib.sha224(string.encode()).hexdigest(),
                "sha256": hashlib.sha256(string.encode()).hexdigest(),
                "sha384": hashlib.sha384(string.encode()).hexdigest(),
                "sha512": hashlib.sha512(string.encode()).hexdigest()
                }
    
    return hash_dict[option]

print(pick_option("What kind of hashing?", "md5", "sha1", "sha224", "sha256", "sha384", "sha512"))

def clear(): 
    """Clear Screen. Works for both Windows and Bash"""
    # Windows 
    if name == 'nt': 
        _ = system('cls') 
    # Bash
    else: 
        _ = system('clear') 

def enter_to_continue():
    """Usually to stop the screen from clearing"""
    input("\nPress Enter to continue... "

# Main Loop
while True:
    choose = pick_option("Do you want to hash or crack?", "Hash", "Crack")
    if choose == 0:
        print("Bye!")
        break
    elif choose == "Hash":
        choose_hash = pick_option("What kind of hashing?", "md5", "sha1", "sha224", "sha256", "sha384", "sha512")
        to_hash = input("Enter string to hash: ")
        print(f"{to_hash} in {choose_hash} = {hashing(choose_hash, to_hash)}") 
    elif choose == "Crack":
        password_file = input("Enter name of password list e.g \"password.txt\"").strip()
    enter_to_continue()


# Hash
# Pick a hash
## 
# Input plaintext
# Output hashed text
## Optional: Append hashed item to file

# Crack Hash
# Enter hash (Optional: Read from file)
