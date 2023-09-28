from src.userdata.Database.bruker_def import brukernavn_get, passord_get


class Username:

    def __init__(self, brukernavn):
        self.brukernavn = brukernavn

    def start_login(self, brukernavn, passord):
        x = "hest"
        if brukernavn in brukernavn_get(brukernavn) and passord in passord_get(passord):
            print(brukernavn, passord)

