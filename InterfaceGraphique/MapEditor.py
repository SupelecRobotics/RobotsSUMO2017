# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 23:54:04 2015

@author: antoinemarechal
"""

from Tkinter import *

scale = 20

class MapEditor :
    
    def __init__(self, master, dimensions, fillBorder) :
        
        # scales of colors and values
        self.colorChart = ["#ffffff", "#ffff7f", "#ffff00", "#ff7f00", "#ff0000", "#000000"]
        self.valueChart = [10, -40, -30, -20, -10, 0]
        
        # main window frame
        mainFrame = Frame(master)
        mainFrame.pack()
        
        self.coords = StringVar()
        self.coords.set("0,0")
        coordinates = Label(mainFrame, textvariable=self.coords)
        coordinates.pack(side=TOP)
        
        # values container
        w = dimensions[0]
        h = dimensions[1]
        self.valMap = [ [ 0 for y in xrange(h) ] for x in xrange(w) ]
        
        # drawing area
        self.map = Canvas(mainFrame, width=w*scale+2, height=h*scale+2)
        self.map.pack(side=TOP)
        self.map.config(bg="#888")
        self.reset(w, h, fillBorder==1)
        self.map.bind("<Button-1>", self.mapCallback)
        
        # level selector
        self.slider = Scale(mainFrame, from_=0, to=5, orient=HORIZONTAL)
        self.slider.pack(side=TOP)
        self.slider.set(5)
        
        # reset button
        resetButton = Button(mainFrame, text="Reset", command = lambda: self.reset(w, h, False))
        resetButton.pack(side=LEFT)
        
        # close button
        closeButton = Button(mainFrame, text="Finish", command = mainFrame.quit)
        closeButton.pack(side=RIGHT)
        
        # mouse position
        self.mouseX = 0
        self.mouseY = 0
        self.map.bind("<Motion>", self.mouseCallback)

    def mapCallback(self, event) :
        x = self.mouseX
        y = self.mouseY
        lvl = self.slider.get()
        self.valMap[x][y] = self.valueChart[lvl]
        self.colorRectangle("current", lvl)
    
    def reset(self, w, h, fillBorder) :
        for x in xrange(w) :
            for y in xrange(h) :
                i = self.map.create_rectangle(x*scale +4, y*scale +4, (x+1)*scale +3, (y+1)*scale +3)
                if fillBorder and (x==0 or x==w-1 or y==0 or y==h-1) :
                    self.colorRectangle(i, 5)
                    self.valMap[x][y] = 0
                else :
                    self.colorRectangle(i, 0)
                    self.valMap[x][y] = 1
    
    def colorRectangle(self, item, lvl) :
        self.map.itemconfig(item, fill=self.colorChart[lvl])
        self.map.itemconfig(item, outline=self.colorChart[lvl])
        self.map.itemconfig(item, activeoutline="#ff0000")
    
    def mouseCallback(self, event) :
        self.mouseX = (event.x - 3) / scale
        self.mouseY = (event.y - 3) / scale
        self.coords.set( str(self.mouseX) + "," + str(self.mouseY) )
        
    
    