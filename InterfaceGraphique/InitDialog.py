# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 23:52:42 2015

@author: antoinemarechal
"""

from Tkinter import *

class InitDialog :

    def __init__(self, master):

        self.mainFrame = Frame(master)
        self.mainFrame.pack()
        
        self.entries = []
        self.values = []
        self.isChecked = IntVar()
        
        label = Label(self.mainFrame, text="Choisissez les dimensions (entières) de la map")
        label.pack(side=TOP)
        
        self.addEntry("Largeur : ")
        self.addEntry("Hauteur : ")
        
        check = Checkbutton(self.mainFrame, text="Contour rempli", variable=self.isChecked)
        check.pack(side=TOP)
        
        button = Button(self.mainFrame, text="Valider", command=self.validate)
        button.pack(side=BOTTOM)
    
    def addEntry(self, lblText) :
        frame = Frame(self.mainFrame)
        
        label = Label(frame, text=lblText)
        label.pack(side=LEFT)
        
        var = StringVar()
        var.set("10")
        self.entries.append(var)
        
        entry = Entry(frame, textvariable=var)
        entry.pack(side=RIGHT)
        
        frame.pack(side=TOP)
    
    def validate(self) :
        for var in self.entries :
            val = int(float(var.get()))
            self.values.append(val)
            print val
        
        self.mainFrame.quit()

