import sys
sys.path.append('src')


from userdata.bruker_def import brukernavn_get, passord_get


def start_login(brukernavn, passord):
    if brukernavn in brukernavn_get(brukernavn) and passord_get(passord) == passord:
        print(brukernavn, passord)
    else:
        print("Wrong input")
from login import *

if __name__ == '__main__':
    x = "brukernavn"
    y = "passord"

    brukercheckUN = brukernavn_get(x)
    brukercheckPW = passord_get(y)

    start_login(brukercheckUN, brukercheckPW)

