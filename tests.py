import Database
# test if the database is working
meteorite = Database.find_meteros_in_db('21', 'e',0,'','')
for thing in meteorite:
    print(thing)