import sys
sys.path.append('src')


from userdata import bruker_def as db


def start_login(brukernavn, passord):
    if brukernavn == None:
        print("Wrong unput")
        return brukernavn, passord
    else:
        print(brukernavn, passord)
        print("XDDDDDD")


def start_registrering(brukernavn, passord, mail):
    db.lag_brukerkonto(brukernavn, passord, mail, False)
        


if __name__ == '__main__':

    x = "brukernavn"
    y = "passord"

    create_acc = db.lag_brukerkonto(x, y, "xD@LOL", False)

    print(":DDD")

    brukercheckUN = db.brukernavn_get(x)
    brukercheckPW = db.passord_get(y)

    start_login(brukercheckUN, brukercheckPW)

    print("")
    print("Start")
    print(start_login(brukercheckUN, brukercheckPW))
    print("Done")
