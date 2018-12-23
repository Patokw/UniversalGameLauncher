#Universal Game Launcher
#RobotCookie
#15.12.18

import time, sys, os

def add():
    pathed = str(input("Input The Game's Locations Ex: C:\Program Files\GameFun\gun.exe: "))
    nameInput = str(input("What is the name of the game? "))
    writing(nameInput,pathed)
    default()
def writing(a,b):
    writefile = open("games.csv","a")
    writefile.write(a+","+b+"\n")
    writefile.close
def default():
    print("===========================GAME LIST==============================")
    file = open("games.csv","r")
    games = list()
    for line in file:
        value = line.split(",")
        print(value[0])
    file.close
    print("==================================================================")
    noError = True
    while noError:
        awaitAction()
def awaitAction():
    command = str(input(">>> "))
    if command.lower() == ("add"):
        add()
    elif command.lower() == ("help"):
        print("<Add - Adds A Game To The List> <GameName - Launches That Game>:")
        awaitAction()
    else:
        file2 = open("games.csv","r")
        for line in file2:
            if command == line.split(",")[0]:
                program = line.split(",")[1]
                os.system("start"+" "+program)
        file2.close
default()
