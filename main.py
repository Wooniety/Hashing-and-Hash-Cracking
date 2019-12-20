# Import libraries
import hashlib
import re
# Minor stuff
from utils import *


def pick_option(question, *options):
    """General Menu"""
    option_dict = {"0": 0}
    print(question)
    print("0) Exit")
    for i, option in enumerate(options):
        option_dict[str(i+1)] = option
        print(f"{i+1}) {option}")
    choose = input(">> ").strip()
    while choose not in option_dict.keys():
        print("Invalid option!")
        choose = input(">> ").strip()
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

# Main Loop
while True:
    clear()
    choose = pick_option("Do you want to hash or crack?", "Hash", "Crack")
    if choose == 0:
        print("Bye!")
        break
    elif choose == "Hash":
        clear()
        choose_hash = pick_option("What kind of hashing?", "md5", "sha1", "sha224", "sha256", "sha384", "sha512")
        to_hash = input("Enter string to hash: ")
        print(f"\033[1;33;40m{to_hash}\033[0;37;40m in \033[1;33;40m{choose_hash}\033[0;37;40m = {hashing(choose_hash, to_hash)}") 
    elif choose == "Crack":
        hash_input = pick_option("Enter hash or read from file?", "Enter hash", "Read from file")
        if hash_input == "Enter hash":
            hash_input = [input("Enter hash: ").strip()]
        else:
            hash_filename = input("Enter name of password list e.g \"password.txt\"\nFormat is seperated by newline\nFilename: ").strip()
            hash_file = open(hash_filename, "r")
            hash_input = hash_file.read().split('\n')
            hash_file.close()
        hash_type = pick_option("Enter name of hash", "md5", "sha1", "sha224", "sha256", "sha384", "sha512")
        hashed_file = open(f"dictionary/{hash_type}.csv", "r")
        stored_hashes = hashed_file.read().split('\n')
        for i, line in enumerate(stored_hashes):
            stored_hashes[i] = line.split(',')
        for hashed_string in hash_input:
            for word in stored_hashes:
                if word[1] == hashed_string:
                    print(f"Match found!\n{hashed_string} = {word[0]}")
                    break
    enter_to_continue()
