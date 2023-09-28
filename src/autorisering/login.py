from src.userdata.Database.bruker_def import *


class Username:

    def __init__(self, brukernavn):
        self.brukernavn = brukernavn

    def start_login(self, brukernavn, passord):
        x = "hest"
        if brukernavn in x and self.brukernavn:
            print(brukernavn)

