#Universal Game Launcher
#RobotCookie
#15.12.18

import tkinter, time, sys, os, csv, winshell
from win32com.client import Dispatch
os.chdir("Games")

def add():
    pathed = str(input("Input The Game's Locations Ex: C:\Program Files\GameFun\gun.exe: "))
    nameInput = str(input("What is the name of the game? "))
    writefile = open("games.csv","a")
    writefile.write(nameInput+","+pathed+","+"\n")
    writefile.close
    default()
def default():
    print("===========================GAME LIST==============================")
    file = open("games.csv","r")
    games = list()
    for line in file:
        value = line.split(",")
        print(value[0])
    print("==================================================================")
    file.close
    noError = True
    while noError:
        awaitAction()
def awaitAction():
    command = str(input(">>> "))
    if command.lower() == ("add"):
        add()
    elif command.lower() == ("remove"):
        try:
            file = str(input("What Game Do You Want To Remove? "))
            program = (file+".lnk")
            os.remove(program)
            default()
        except:
            print("Invalid Game Name")
            awaitAction()
    elif command.lower() == ("help"):
        print("<Add - Adds A Game To The List> <Remove - Removes A Game From The List> <GameName - Launches That Game>:")
        awaitAction()
    else:
        csv_reader = csv.reader(open('games.csv', 'r'), delimiter=",")
        for line in csv_reader:
            if command == line[0]:
                program = line[1]
                os.system("start"+" "+program)
default()
