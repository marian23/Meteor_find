from Model import *
from peewee import *
from tabulate import tabulate



# to save in the database meteorite
def insert_meteor(meteor):
    try:
        new_meteor = meteorite_sighting_model.create(
            name = meteor['name'],
            mass =meteor ['mass'],
            year = meteor['year'],
            latitude = meteor['latitude'],
            longitude =meteor['longitude'])
        new_meteor.save()
    except IntegrityError:
        print("meteor is in database")
 #takes single record userfull
def compile_record(record):
    small_list = [record.mass, record.name, record.year, record.latitude, record.longitude]
    return small_list
#this take all record pass by find_meteor_in_db
def record_compiler(all_record):
    all_meteor = []
    for record in all_record:
        all_meteor.append(compile_record(record))
    return all_meteor
# to find meteor in database use when google in google map
def find_meteros_in_db(mass, name, year, latitude, longitude):
    meteors=[]
    list_version = []
    if mass == '':
        for meteor in meteorite_sighting_model:
            if name in meteor.name and int(year) >= int(meteor.year)-5 and int(year) <= int(meteor.year) +5:
                meteors.append(meteor)

    # if name == '':

    #     meteor = meteorite_sighting_model.get(
    #         meteorite_sighting_model.mass.startswith(mass)).where(meteorite_sighting_model.year.startswith(year))
    #
    if year == 0:
        for meteor in meteorite_sighting_model:
            if name in meteor.name and float(mass) >= float(meteor.mass)-15 and float(mass) <= float(meteor.mass)+15:
                meteors.append(meteor)

        # meteor = meteorite_sighting_model.select(
        #     meteorite_sighting_model.name.startswith(name)).where(meteorite_sighting_model.mass.startswith(mass))
        list_version = record_compiler(meteors)
    # if latitude == '':
    #     meteor = meteorite_sighting_model.select(
    #          meteorite_sighting_model.name.startswith(name)).where(meteorite_sighting_model.year.startswith(year)).where(meteorite_sighting_model.mass.startswith(mass))
    # if longitude == '':
    #      meteor = meteorite_sighting_model.select(
    #          meteorite_sighting_model.name.startswith(name)).where(
    #              meteorite_sighting_model.year.startswith(year)).where(meteorite_sighting_model.mass.startswith(mass)).where(meteorite_sighting_model.latitude.startswith(latitude))
    #
    # if mass or name or year or latitude or longitude == '':
    #     meteor = meteorite_sighting_model.select(
    #         meteorite_sighting_model.name.startswith(name)).where(
    #             meteorite_sighting_model.year.startswith(year)).where(
    #                 meteorite_sighting_model.mass.startswith(mass)).where(
    #                     meteorite_sighting_model.latitude.startswith(latitude)).where(meteorite_sighting_model.longitude.startswith(longitude))

    return list_version



