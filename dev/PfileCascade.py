# Player file cascade functions

from tkinter import *
from GURPSCharacter import *

def Pnew(root, app):
    app.player = GURPSCharacter()
    app.player.loadCharacter(name = "BASE")

def Popen(root, app):
    return

def Psave(root, app):
    return

def clientExit(window):
    window.destroy()
    #exit()
