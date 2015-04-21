# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 23:54:04 2015

@author: antoinemarechal
"""

from Tkinter import *

scale = 10
maxWidth = 600
maxHeight = 400

class MapEditor :
    
    def __init__(self, master, dimensions, fillBorder) :
        
        # scales of colors and values
        self.colorChart = ["#fffff0", "#cccccc", "#999999", "#666666", "#333333", "#000000"]
        self.valueChart = [1, -4, -3, -2, -1, 0]
        
        # main window frame
        mainFrame = Frame(master)
        mainFrame.pack()
        
        self.coords = StringVar()
        self.coords.set("1,1")
        coordsLabel = Label(mainFrame, textvariable = self.coords)
        coordsLabel.pack(side = TOP, fill = Y)
        
        self.isDrawing = False
        self.state = StringVar()
        self.state.set("not drawing")
        stateLabel = Label(mainFrame, textvariable = self.state)
        stateLabel.pack(side = TOP, fill = X)
        
        # values container
        w = dimensions[0]
        h = dimensions[1]
        self.valMap = [ [ 0 for y in xrange(h) ] for x in xrange(w) ]
        #self.widgetMap = [ [ None for y in xrange(h) ] for x in xrange(w) ]
        
        # drawing area
        mapFrame = Frame(mainFrame)
        mapFrame.pack(side = TOP)
        
        self.map = Canvas(mapFrame)
        self.map.config(width = min(maxWidth, scale*w))
        self.map.config(height = min(maxHeight, scale*h))
        self.map.config(scrollregion = (0, 0, scale*w, scale*h))
        self.map.config(bg = "#ffff00")
        
        # scrollbars
        xbar = Scrollbar(mapFrame, orient = HORIZONTAL)
        xbar.pack(side = BOTTOM, fill = X)
        xbar.config(command = self.map.xview)
        self.map.config(xscrollcommand = xbar.set)
        
        ybar = Scrollbar(mapFrame, orient = VERTICAL)
        ybar.pack(side = RIGHT, fill = Y)
        ybar.config(command = self.map.yview)
        self.map.config(yscrollcommand = ybar.set)
        
        self.map.pack()
        
        # drawing events
        for x in xrange(w) :
            for y in xrange(h) :
                i = self.map.create_rectangle(x*scale, y*scale, (x+1)*scale -1, (y+1)*scale -1)
                self.map.itemconfig(i, fill=self.colorChart[0])
                self.map.itemconfig(i, outline=self.colorChart[0])
                self.map.itemconfig(i, activeoutline="red")
                self.valMap[x][y] = self.valueChart[0]
        
        self.map.bind("<Button-1>", self.mouseClickCallback)
        self.map.bind("<Motion>", self.mouseMoveCallback)
        
#        self.map = Canvas(mainFrame, width=w*scale+2, height=h*scale+2)
#        self.map.pack(side=TOP)
#        self.map.config(bg="#888")
#        self.reset(w, h, fillBorder==1)
#        self.map.bind("<B1-Motion>", self.mapCallback)
        
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
#        self.mouseX = 0
#        self.mouseY = 0
#        self.map.bind("<Motion>", self.mouseCallback)
    
    def mouseClickCallback(self, event) :
        self.isDrawing = not self.isDrawing
        self.state.set("drawing" if self.isDrawing else "not drawing")
    
    def mouseMoveCallback(self, event) :
        x = int(self.map.canvasx(event.x) / scale)
        y = int(self.map.canvasy(event.y) / scale)
        self.coords.set(str(x+1) + "," + str(y+1))
        if self.isDrawing :
            lvl = self.slider.get()
            self.map.itemconfig("current", fill = self.colorChart[lvl])
            self.map.itemconfig("current", outline = self.colorChart[lvl])
            self.valMap[x][y] = self.valueChart[lvl]

#    def mapCallback(self, event) :
#        x = self.mouseX
#        y = self.mouseY
#        lvl = self.slider.get()
#        self.valMap[x][y] = self.valueChart[lvl]
#        self.colorRectangle("current", lvl)
    
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
    
#    def mouseCallback(self, event) :
#        self.mouseX = (event.x - 3) / scale
#        self.mouseY = (event.y - 3) / scale
#        self.coords.set( str(self.mouseX) + "," + str(self.mouseY) )
#        #self.colorRectangle("current", self.slider.get())
        
    
    