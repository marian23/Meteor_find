Finding meteor in the Google map
I find meteorite API in the data.gov I am using to find in the Google maps. 

API1: Nasa Meteorite Tracker API

API2: Google Maps Static Images
Purpose: To show where meteorites have fallen, and put google maps markers on those locations

Successes: Api Connection to Meteorite data, parsing the JSON given by it, Database for meteors and calls for data from it, modification of Tkinter GUI.

Bugs/Features: Problems with the way the static files are rendered, resulting in not grabbing new ones instead using the old ones, or crashing after not finding the right file.

I am using python 2.7  and a package for using googlemaps static images that comes with a basic GUI for modifying: https://github.com/simondlevy/GooMPy
