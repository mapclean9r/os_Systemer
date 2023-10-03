from login import *

if __name__ == '__main__':
    x = "brukernavn"
    y = "passord"

    brukercheckUN = brukernavn_get(x)
    brukercheckPW = passord_get(y)

    start_login(brukercheckUN, brukercheckPW)
