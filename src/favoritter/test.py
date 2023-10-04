import sys
sys.path.append('src')

#from userdata import bruker_def
import userdata.bruker_def as bruker_def



#bruker_def.lag_brukerkonto("DWADSDWDAWADA","DWDWADA","DWDWADAW",0)
bruker_def.lag_brukerkonto("TEST","DWDWADA","DWDWADAW",1)

bruker_def.passord_endre("DWADSDWDAWADA","TEST")

print(bruker_def.is_admin("TEST"))
print(bruker_def.is_admin("DWADSDWDAWADA"))
print(bruker_def.brukernavn_endre("TEST","DWADSDWDAWADA"))
print(bruker_def.passord_get("TEST"))