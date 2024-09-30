from colorama import Fore, Style
from getpass import getpass

auth_users = [
    {"gstreet": "gstr71"},
    {"pooh": "kissez"},        
    {"boogie": "2008"},        
    {"admin": "admin"},        
    ]
    
def login():    
    while True:
        username = input(Fore.YELLOW + "Enter your username: ").lower()
        if not is_valid(username):
            continue
        get_password(username)
        return username

def get_password(username):
    password = getpass("Enter your password: ").lower()
    if not is_passValid(username, password):
        login()
    else:
        greeting(username)
        return username

def is_valid(username):
    for user in auth_users:
        if username in user:
            return True
        
    print(Fore.RED + "Username cannot be found" + Style.RESET_ALL)
    return False

def is_passValid(username, password):
    for user in auth_users:
        if username in user and user[username] == password:
            return True
        
    print(Fore.RED + "Password is invalid" + Style.RESET_ALL)
    return False   

def greeting(username):
    name = username.capitalize()
    print(Fore.GREEN + "\nYou have successfully logged in as" + Fore.BLUE + f" {name}\n" + Style.RESET_ALL)    

print(Fore.YELLOW + "LOGIN SYSTEM\n")
login()