import getpass

#users = []


# Registrer ny bruker
def register_user():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")


    with open("users.txt", "a") as file:
        file.write(f"{username} : {password} \n")
    print("User registered successfully!")


# Validere login
def login():
    username_valid = input("Enter your username: ")
    password_valid = getpass.getpass("Enter your password: ")


    with open("users.txt", "r") as file:
        for line in file:
            stored_username, store_password = line.strip().split(": ")
            if username_valid == stored_username and password_valid == store_password:
                return True
    return False


while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")


    choice = input("Select an option: ")


    if choice == "1":
        register_user()
    elif choice == "2":
        if login():
            print("Login successful!")
        else:
            print("Invalid username or password. Please try again.")
    elif choice == "3":
        break
    else:
        print("Invalid option. Please try again.")


"""
def add_user():
    user = input("Add user: ")
    users.append([user])
    print(users)


#def add_passord_to_user():



add_user()
"""