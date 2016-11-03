#!/usr/bin/env python
'''
Example of using GooMPy with Tkinter

Copyright (C) 2015 Alec Singer and Simon D. Levy

This code is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as 
published by the Free Software Foundation, either version 3 of the 
License, or (at your option) any later version.
This code is distributed in the hope that it will be useful,     
but WITHOUT ANY WARRANTY without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU Lesser General Public License 
along with this code.  If not, see <http://www.gnu.org/licenses/>.
'''

from Tkinter import Tk, Canvas, Label, Frame, IntVar, Radiobutton, Button, Entry,StringVar
import Tkinter
from PIL import ImageTk
import Database as db

from goompy import GooMPy

WIDTH = 1000
HEIGHT = 500

LATITUDE  =  37.7913838
LONGITUDE = -79.44398934
ZOOM = 10
MAPTYPE = 'roadmap'
find_meteor = 'meteor'

class UI(Tk):

    def __init__(self):

        Tk.__init__(self)

        self.geometry('%dx%d+500+500' % (WIDTH,HEIGHT))
        self.title('Google maps to find Meteorite ')

        self.canvas = Canvas(self, width=WIDTH, height=HEIGHT)

        self.canvas.pack()

        self.bind("<Key>", self.check_quit)
        self.bind('<B1-Motion>', self.drag)
        self.bind('<Button-1>', self.click)

        self.label = Label(self.canvas)

        self.radiogroup = Frame(self.canvas)
        self.radiovar = IntVar()
        self.maptypes = ['roadmap', 'terrain', 'satellite', 'hybrid']
        self.add_radio_button('Road Map',  0)
        self.add_radio_button('Terrain',   1)
        self.add_radio_button('Satellite', 2)
        self.add_radio_button('Hybrid',    3)
  # list the textbox in google maps to find meteor
        self.massentry = Entry()
        self.massentry.grid_location(400,400)
        self.massentry.pack()
        self.massvalue = StringVar()
        self.massvalue.set('4')
        #self.massentry["textvariable"] = self.massvalue
#list the textbox in google maps to find meteor
        self.nameentry = Entry()
        self.nameentry.grid_location(500,500)
        self.nameValue = StringVar()
        self.nameValue.set('fall')
#list the textbox in google maps to find meteor
        self.year = Entry()
        self.year.grid_location(500,500)
        self.yearValue = StringVar()
        self.yearValue.set('0000')
#list the textbox in google maps to find meteor
        self.latitude = Entry()
        self.latitude.grid_location(500,500)
        self.latitudeValue = StringVar()
        self.latitudeValue.set('6.897')
#list the textbox in google maps to find meteor
        self.longitude = Entry()
        self.longitude.grid_location(500,500)
        self.longitudeValue = StringVar()
        self.longitudeValue.set('5.678')
# to search button to clik when try to find meteor
        self.search = Button(command=self.retrieve_entry)
        self.search["command"]= self.retrieve_entry
        self.search.grid_location(600,600)
        self.search_value = StringVar()
        self.search_value.set('search meteorite')
        self.search["textvariable"] = self.search_value
        self.meteors = []

# to label the textbox
        masstext = StringVar()
        self.mass_label = Label(master=None, textvariable= masstext)
        masstext.set('Mass:')
# to label the textbox for the meteor
        name_text = StringVar()
        self.name_lable = Label(master=None, textvariable= name_text)
        name_text.set('Name:')

        year_number = StringVar()
        self.year_label = Label(master=None, textvariable=year_number)
        year_number.set('Year:')

        latitude_number = StringVar()
        self.latitude_label = Label(master=None, textvariable=latitude_number)
        latitude_number.set('Latitude:')

        longitude_text = StringVar()
        self.longitude_label = Label(master=None, textvariable=longitude_text)
        longitude_text.set('Longitude:')

        search_meteor = StringVar()
        self.search_label = Label(master=None, textvariable=search_meteor)
        search_meteor.set('search meteor:')






        self.zoom_in_button  = self.add_zoom_button('+', +1)
        self.zoom_out_button = self.add_zoom_button('-', -1)
        # self.zoom_nowhere_button = self.add_zoom_button('no',+0)

        self.zoomlevel = ZOOM

        maptype_index = 0
        self.radiovar.set(maptype_index)

        self.goompy = GooMPy(WIDTH, HEIGHT, LATITUDE, LONGITUDE, ZOOM, MAPTYPE)


        self.restart()
# clik the button to find metor
    def retrieve_entry(self):
        print('Button Clicked')
        if self.massentry.get()=='':
            mass = '0'
        else:
            mass = self.massentry.get()
        name = self.nameentry.get()
        if self.year.get()=='':
            a_year = 0
        else:
            a_year = int(self.year.get())

        if self.latitude.get()=='':
            latitude = 0.00
        else:
            latitude = float(self.latitude.get())
        if self.longitude.get()=='':
            longitude = 0.00
        else:
            longitude = float(self.longitude.get())
        # params = [mass, name, year, latitude, longitude]
        self.meteors = db.find_meteros_in_db(mass,name,a_year,latitude,longitude)
        self.redraw()

    def add_zoom_button(self, text, sign):

        button = Button(self.canvas, text=text, width=1, command=lambda:self.zoom(sign))
        return button

    def reload(self):

        self.coords = None
        self.redraw()



        self['cursor']  = ''


    def restart(self):

        # A little trick to get a watch cursor along with loading
        self['cursor']  = 'watch'
        self.after(1, self.reload)

    def add_radio_button(self, text, index):

        maptype = self.maptypes[index]
        Radiobutton(self.radiogroup, text=maptype, variable=self.radiovar, value=index, 
                command=lambda:self.usemap(maptype)).grid(row=0, column=index)



        print()

    def click(self, event):

        self.coords = event.x, event.y

    def drag(self, event):

        self.goompy.move(self.coords[0]-event.x, self.coords[1]-event.y)
        self.image = self.goompy.getImage(self.meteors)
        self.redraw()
        self.coords = event.x, event.y

    def redraw(self):

        self.image = self.goompy.getImage(self.meteors)
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.label['image'] = self.image_tk

        self.label.place(x=0, y=0, width=WIDTH, height=HEIGHT)

        self.radiogroup.place(x=0,y=0)

        x = int(self.canvas['width']) - 50
        y = int(self.canvas['height']) - 80

# to label where the textbox and label go the google map
        self.massentry.place(x=900,y=50)
        self.mass_label.place(x=840, y=50)
        self.nameentry.place(x=900, y=80)
        self.name_lable.place(x=840, y=80)
        self.year.place(x=900,y=103)
        self.year_label.place(x=840, y=100)
        self.latitude.place(x=900, y= 130)
        self.latitude_label.place(x=830, y=130)
        self.longitude.place(x=900, y=160)
        self.longitude_label.place(x=830, y=160)

        self.search.place(x=900,y=190)
        #self.search_label(x=870, y=170)


        self.zoom_in_button.place(x= x, y=y)
        self.zoom_out_button.place(x= x, y=y+30)

    def usemap(self, maptype):

        self.goompy.useMaptype(maptype)
        self.restart()

    def zoom(self, sign):

        newlevel = self.zoomlevel + sign
        if newlevel > 0 and newlevel < 22:
            self.zoomlevel = newlevel
            self.goompy.useZoom(newlevel)
            self.restart()

    def check_quit(self, event):

        if ord(event.char) == 27: # ESC
            exit(0)
        else:
            print('That\'s fine')

UI().mainloop()
