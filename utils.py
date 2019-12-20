from os import system, name

def clear(): 
    """Clear Screen. Works for both Windows and Bash"""
    # Windows 
    if name == 'nt': 
        system('cls') 
    # Bash
    else: 
        system('clear') 

def enter_to_continue():
    """Usually to stop the screen from clearing"""
    input("\nPress Enter to continue... ")
