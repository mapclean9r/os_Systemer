import json


class DataLaster:
    def __init__(self, data_file):
        self.data_file = data_file
        self.load_json()

    # Reads The json file // creates one
    def load_json(self):
        try:
            with open(self.data_file, "r") as file:
                self.user_data = json.load(file)
        except FileNotFoundError:
            self.user_data = {}

    # Saves to json file
    def save_json(self):
        with open(self.data_file, "w") as file:
            json.dump(self.user_data, file, indent=4)


class StartRegistration(DataLaster):
    def register(self, name, password):
        if name in self.user_data:
            print("Username already taken")
        else:
            self.user_data[name] = {"username": name, "password": password, "access_level": 0}
            self.save_json()
            print("Registration complete")


class StartLogin(DataLaster):
    def login(self, name, password):
        if name in self.user_data and self.user_data[name]["password"] == password:
            print("Login Complete")
        else:
            print("Login failed")


class GetUserData(DataLaster):

    # Get all stored user data
    def store_user_data(self, name):
        stored_data = [self.user_data[name]]
        return stored_data

    # Get name fix?
    def user_data_name(self, username):
        for name in self.user_data:
            if name == username:
                return name

    # Get verification level
    def user_verification(self, username):
        for name in self.user_data:
            if name == username:
                return self.user_data[name]['access_level']