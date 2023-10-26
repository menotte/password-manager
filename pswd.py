import random
import string
import os

def generate_random_password(length=24):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def display_banner():
    banner = """
██████╗ ███████╗██╗    ██╗██████╗ 
██╔══██╗██╔════╝██║    ██║██╔══██╗
██████╔╝███████╗██║ █╗ ██║██║  ██║
██╔═══╝ ╚════██║██║███╗██║██║  ██║
██║     ███████║╚███╔███╔╝██████╔╝
╚═╝     ╚══════╝ ╚══╝╚══╝ ╚═════╝
    """
    print(banner)

def generate_new_password():
    account_name = input("Account: ")
    file_name = f"{account_name}_password.txt"
    if os.path.exists(file_name):
        print(f"A file with the name '{file_name}' already exists.")
        print("You cannot create a file with the same name.")
        return

    account_username = input("Username: ")
    account_email = input("Email: ")
    random_password = generate_random_password()
    with open(file_name, "w") as file:
        file.write(f"Account: {account_name}\n")
        file.write(f"Account: {account_username}\n")
        file.write(f"Email: {account_email}\n")
        file.write(f"Password: {random_password}\n")
    print(f"Account information for '{account_name}' has been saved to '{file_name}' file.")
    print("")
    print(f"The password is: {random_password}")

def list_passwords():
    files = [f for f in os.listdir() if f.endswith("_password.txt")]
    if not files:
        print("No password files found.")
    else:
        print("List of generated passwords:")
        print("")
        for file_name in files:
            account_name = file_name.split("_password.txt")[0]
            print(f"Account: {account_name}")

def see_password(account_name):
    file_name = f"{account_name}_password.txt"
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            lines = file.readlines()
            for line in lines:
                if "Password:" in line:
                    password = line.strip().split("Password: ")[1]
                    print("")
                    print(f"Password for {account_name} is: {password}")
                    break
            else:
                print(f"Password not found for {account_name} in the file.")
    else:
        print(f"File '{file_name}' not found.")

def regenerate_password_from_file(account_name):
    file_name = f"{account_name}_password.txt"
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            lines = file.readlines()
            account_username = None
            account_email = None
            for line in lines:
                if "Account:" in line:
                    account_name = line.strip().split("Account: ")[1]
                elif "Account:" in line:
                    account_username = line.strip().split("Account: ")[1]
                elif "Email:" in line:
                    account_email = line.strip().split("Email: ")[1]
            random_password = generate_random_password()
            with open(file_name, "w") as file:
                file.write(f"Account: {account_name}\n")
                file.write(f"Account: {account_username}\n")
                file.write(f"Email: {account_email}\n")
                file.write(f"Password: {random_password}\n")
            print(f"Password for '{account_name}' has been regenerated and saved to '{file_name}'.")
            print("")
            print(f"The new password is: {random_password}")
    else:
        print(f"File '{file_name}' not found for '{account_name}'.")

def main():
    display_banner()
    first_display = True
    while True:
        if first_display:
            print("[1] Generate a new password")
            print("[2] List generated passwords")
            print("[3] See a password from a file")
            print("[4] Regenerate a password from a file")
            print("[5] Quit")
            print("")
            choice = input("Number: ")
            first_display = False
        else:
            print("")
            choice = input("Number: ")
        if choice == "1":
            print("")
            generate_new_password()
        elif choice == "2":
            print("")
            list_passwords()
        elif choice == "3":
            print("")
            account_name = input("Enter the account name: ")
            see_password(account_name)
        elif choice == "4":
            print("")
            account_name = input("Enter the account name: ")
            regenerate_password_from_file(account_name)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
