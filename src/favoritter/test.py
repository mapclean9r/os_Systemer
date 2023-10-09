from userdata import bruker_def
import sys
sys.path.append('src')


# TODO vi må få dette til å fungere
bruker_def.lag_brukerkonto("DWADSDWDAWADA","DWDWADA","DWDWADAW",0)

#bruker_def.lag_brukerkonto("DWADSDWDAWADA","DWDWADA","DWDWADAW",0)
bruker_def.lag_brukerkonto("TEST","DWDWADA","DWDWADAW",1)

bruker_def.passord_endre("DWADSDWDAWADA","TEST")

print(bruker_def.is_admin("TEST"))
print(bruker_def.is_admin("DWADSDWDAWADA"))
print(bruker_def.brukernavn_endre("TEST","DWADSDWDAWADA"))
print(bruker_def.passord_get("TEST"))