from Tkinter import Tk, Canvas, Label, Frame, IntVar, Radiobutton, Button
from PIL import ImageTk
#import tkinter as tk


from goompy import *

width = 1000
height = 900
latitude = 37.7913838
longitude = -79.44398934
zoom = 20
maptype = 'roadmap'


class UI(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.geometry = ('%dx%d+600+600' % (width, height))
        self.canvas = Canvas(self, width=width, height=height)
        self.title=('meteor_finder')

        #self.canvas.pack()



        self.bind('<Key>', self.check_quit)
        self.bind('<B1-Motion>', self.drag)
        self.bind('<Button-1>', self.click)

        self.label = Label(self.canvas)
        self.radiogroup = Frame(self.canvas)
        self.radiovar = IntVar()
        self.maptypes = ['roadmap', 'Terrain', 'Satellite', 'Hybrid']
        self.add_radio_button('Road map', 0)
        self.add_radio_button('Terrain', 1)
        self.add_radio_button('Satellite', 2)
        self.add_radio_button('Hybrid', 3)

        self.zoom_in_button = self.add_zoom_button('+', +1)
        self.zoom_out_button = self.add_zoom_button('-', -1)

        self.zoomlevel = zoom
        map_type_index = 0
        self.radiovar.set(map_type_index)

        self.goompy = GooMPy(width,height,latitude, longitude, zoom, maptype)
        self.restart()

    def add_zoom_button(self, text, sign):

        button = Button(self.canvas, text=text, width=1, command=lambda:self.zoom(sign))
        return button
    def reload(self):
        self.coords = None
        self.redraw()

        self['cursor'] = ''

    def restart(self):
        self['cursor'] = 'watch'
        self.after(1, self.reload)

    def add_radio_button(self, text, index):

        typemap = self.maptypes[index]
        Radiobutton(self.radiogroup, text=maptype, variable=self.radiovar, value=index,
                    command=lambda: self.usemap(maptype)).grid(row=0, column=index)

    def click(self, event):

        self.coords = event.x, event.y

    def drag(self, event):

        self.goompy.move(self.coords[0] - event.x, self.coords[1] - event.y)
        self.image = self.goompy.getImage()
        self.redraw()
        self.coords = event.x, event.y

    def redraw(self):

        self.image = self.goompy.getImage()
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.label['image'] = self.image_tk

        self.label.place(x=0, y=0, width=width, height=height)

        self.radiogroup.place(x=0, y=0)

        x = int(self.canvas['width']) - 50
        y = int(self.canvas['height']) - 80

        self.zoom_in_button.place(x=x, y=y)
        self.zoom_out_button.place(x=x, y=y + 30)

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

        if ord(event.char) == 27:  # ESC
            exit(0)

UI().mainloop()



