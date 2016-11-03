import requests
import json
from Database import insert_meteor
from Model import *


# to call meteorite api
class meteor_api():
 def __init__(self):
     self.url = 'https://data.nasa.gov/resource/gh4g-9sfh.json'
     self.response = []


 def get_data(self):
     self.response = requests.get(self.url).json()

 # to list names, masss, years, latitudes and longitudes in database
     for meteor in self.response:
         single_meteor = {'name': '', 'mass':0.0, 'year':0, 'latitude':0.00, 'longitude':0.00}
         try:
             if meteor['name']:
                single_meteor['name']=meteor['name'][0:]
             if meteor['mass']:
                single_meteor['mass']=meteor['mass']
             if meteor['year']:
                single_meteor['year'] = meteor['year'][:4]
             if meteor['geolocation']:
                single_meteor['latitude'] = meteor['geolocation']['latitude']
             if meteor['geolocation']:
                single_meteor['longitude'] = meteor['geolocation']['longitude']


         except KeyError as e:
             print(e)
         insert_meteor(single_meteor)
         print(single_meteor)




         # print(meteor)
#


