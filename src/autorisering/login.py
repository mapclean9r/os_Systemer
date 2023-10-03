from src.userdata.bruker_def import brukernavn_get, passord_get


def start_login(brukernavn, passord):
    if brukernavn in brukernavn_get(brukernavn) and passord_get(passord) == passord:
        print(brukernavn, passord)
    else:
        print("Wrong input")

