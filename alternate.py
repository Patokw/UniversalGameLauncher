#Universal Game Launcher
#RobotCookie
#15.12.18

import time, sys, os, subprocess

def add():
    pathed = str(input("Input The Game's Locations Ex: C:\Program Files\GameFun\gun.exe: "))
    nameInput = str(input("What is the name of the game? "))
    todo = ("ToDos/"+nameInput+".csv")
    writing(nameInput,pathed,todo)
    default()
def writing(a,b,c):
    writefile = open("games.csv","a")
    writefile.write(a+","+b+","+c+","+"Blank"+"\n")
    writefile.close
def listadd():
    global todoPath
    writefile = open(todoPath,"a")
    addition = str(input("Name The Task To Add: "))
    writefile.write(addition+","+"NO"+"\n")
    writefile.close
def to_do():
    list = open(todoPath, "r+")
    print()
    print("Task")
    print("-----")
    for item in list:
        check = item.split(",")
        print(check[0])
    list.close
    print("======")
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
    global todoPath
    command = str(input(">>> "))
    if command.lower() == ("add"):
        add()
    elif command.lower() == ("help"):
        print("<Add - Adds A Game To The List> <GameName - Launches That Game>:")
        awaitAction()
    elif command.lower() == ("addl"):
        listadd()
    elif command.lower() == ("todo"):
        try:
            to_do()
        except:
            print("No Game Started!")
            awaitAction()
    elif command.lower() == ("clear"):
        list = open(todoPath, "r+")
        wlist = open(todoPath, "w+")
        for item in list:
            wlist.write("Clearing!")
        list.close
    else:
        file2 = open("games.csv","r")
        for line in file2:
            if command == line.split(",")[0]:
                program = str(line.split(",")[1])
                todoPath = line.split(",")[2]
                os.system("start"+" "+program)
                try:
                    list = open(todoPath, "r+")
                    print()
                    print("Task")
                    print("-----")
                    for item in list:
                        check = item.split(",")
                        print(check[0])
                    list.close
                    print("======")
                except:
                    list = open(todoPath, "w")
                    list.close
                    list = open(todoPath, "r+")
                    print()
                    print("Task")
                    print("-----")
                    for item in list:
                        check = item.split(",")
                        print(check[0])
                    list.close
                    create.close
                    print("======")
        file2.close
default()
