import hashlib
import getpass
passwords={}
def create_account():
    username=input("enter the username:")
    password=getpass.getpass("enter the password:")
    hashed_pass=hashlib.sha256(password.encode()).hexdigest()
    passwords[username]=hashed_pass
    print("account created succesfully!!")
def login():
    username=input("enter the user name:")
    password=getpass.getpass("enter the password:")
    hash_pass=hashlib.sha256(password.encode()).hexdigest()
    if username in passwords.keys() and passwords[username]==hash_pass:
        print("login successful")
    else:
        print("invalid credintials")
def main():
    while True:
        l=input("enter 1 to login or enter 2 to sign up or 0 to break")
        if l=="1":
            login()
        elif l=="2":
            create_account()
        elif l=="0":
            break
        else:
            print("invalid choice")
main()    
