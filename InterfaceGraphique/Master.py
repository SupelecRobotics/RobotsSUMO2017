# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 00:09:57 2015

@author: antoinemarechal
"""

from Tkinter import *
from InitDialog import InitDialog
from MapEditor import MapEditor

root1 = Tk()

dialog = InitDialog(root1)

root1.mainloop()
root1.destroy()

root2 = Tk()

editor = MapEditor(root2, dialog.values, dialog.isChecked.get())

#root2.mainloop()
#root2.destroy() # optional; see description below

def writeToFile() :
    mat = editor.valMap
    w = len(mat)
    h = len(mat[0])
    
    f = open("resultmap.txt", "w")
    
    for y in xrange(h) :
        line = ""
        for x in xrange(w) :
            v = mat[x][y]
            if v > 0 :
                line += "."
            else :
                line += str(-v)
        f.write(line + "\n")
    
    f.close()