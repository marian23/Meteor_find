
from meteor_API import meteor_api
from Model import meteorite_sighting_model
import Model
from Database import insert_meteor as insert
import Database
def main():
    mapi = meteor_api()
    Model.db.connect()
    #Database.drop_table()
    Model.db.create_tables  ([meteorite_sighting_model], safe=True)
    mapi.get_data()






main()

