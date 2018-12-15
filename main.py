#Universal Game Launcher
#RobotCookie
#15.12.18

import tkinter, time, sys, os, csv, winshell
from win32com.client import Dispatch
def add():
    pathed = str(input("Input The Game's Locations Ex: C:\Program Files\GameFun\gun.exe "))
    pathed2 = str(input("Now Input That Again But Without The Exe Ex: C:\Program Files\GameFun "))
    nameInput = str(input("What is the name of the game? "))
    name = (nameInput+".lnk")
    path = os.path.join("Games", name)
    target = (pathed)
    wDir = (pathed2)
    icon = (pathed)

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()
def default():
    os.chdir("Games")
    dir = os.listdir()
        for item in dir:
            print (item)
default()
