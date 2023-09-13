from VerificationSystem import StartRegistration
from VerificationSystem import StartLogin
from VerificationSystem import GetUserData


def main():
    registration = StartRegistration("user_data.json")
    innlogging = StartLogin("user_data.json")
    data_storage = GetUserData("user_data.json")

    while True:
        print("\n   ///// Menu //////")
        print("  / 1   Register //")
        print(" / 2   Login    //")
        print("/////////////////")

        option = input("\nPress 1/2 : \n")

        if option == '1':
            name = input("Enter Your Username: ")
            password = input("Enter Your Password: ")
            registration.register(name, password)
        elif option == '2':
            name = input("Enter Your Username: ")
            password = input("Enter Your Password: ")
            innlogging.login(name, password)
            data_storage.store_user_data(name)
            break
        else:
            print("invalid number")


if __name__ == "__main__":
    main()
    print("")
    print("")

    # Fix // F책 tak i brukernavnet uten 책 skrive det inn manuelt /////
    userdata = GetUserData("user_data.json")
    print("Get Userdata:", userdata.store_user_data("CoolDuck"))

    user_username = GetUserData("user_data.json")
    print("Username:", user_username.user_data_name("CoolDuck"))

    verify_status = GetUserData("user_data.json")
    print("Verification level:", verify_status.user_verification("CoolDuck"))

    # Fix // F책 tak i brukernavnet uten 책 skrive det inn manuelt /////