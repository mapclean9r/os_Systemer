import sys
sys.path.append('src')


from userdata import bruker_def


bruker_def.test()
bruker_def.lag_brukerkonto("Jame", "Labron", "fake@fake.no", False)
