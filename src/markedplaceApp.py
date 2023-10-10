from src.userdata import database_creation
from src.gui.markedplace_operations import tour_management
from src.gui.login import user_logout, create_userprofile, login_details
import tkinter as tk


class MarketplaceApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Guided Tour Marketplace')
        self.geometry('900x650')
        self.resizable(False, False)

        self.username = None
        self.show_login()

    def show_login(self):
        login_details.display_login(self)

    def login(self):
        login_details.login_checker(self)

    def register(self):
        create_userprofile.making_a_user(self)

    def logout(self):
        user_logout.logout_a_user(self)

    def show_marketplace(self):
        tour_management.display_marketplace(self)

    def offer_tour(self):
        tour_management.offering_a_tour(self)

    def delete_tour(self):
        tour_management.deleting_a_tour(self)


if __name__ == '__main__':
    database_creation.create_database()
    app = MarketplaceApp()
    app.mainloop()
