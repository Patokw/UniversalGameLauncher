#Universal Game Launcher
#RobotCookie
#15.12.18

import tkinter, time, sys, os, csv, winshell
from win32com.client import Dispatch
os.chdir("Games")
def add():
    pathed = str(input("Input The Game's Locations Ex: C:\Program Files\GameFun\gun.exe: "))
    nameInput = str(input("What is the name of the game? "))
    name = (nameInput+".lnk")
    path = os.path.join(name)
    target = (pathed)
    icon = (pathed)
    try:
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.IconLocation = icon
        shortcut.save()
        default()
    except:
        print("Invalid Game Location")
        add()
def default():
    print("========================GAME LIST=================================")
    dir = os.listdir()
    dirList = [x.split('.')[0] for x in dir]
    for item in dirList:
        print (item)
    print("==================================================================")
    noError = True
    while noError:
        awaitAction()
def awaitAction():
    command = str(input("Type a game name to launch a game to launch a game, or Add To Add A Game: "))
    if command.lower() == ("add"):
        add()
    else:
        try:
            program = command+".lnk"
            os.system("start"+" "+program)
        except:
            print("Game Not Found [Case Sensitive]")
            awaitAction()
default()
