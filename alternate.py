#Universal Game Launcher
#RobotCookie
#15.12.18

import time, sys, os

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
    else:
        file2 = open("games.csv","r")
        for line in file2:
            if command == line.split(",")[0]:
                program = line.split(",")[1]
                todoPath = line.split(",")[2]
                os.system("start"+" "+program)
                try:
                    list = open(todoPath, "r+")
                    print("Task | Checked")
                    for item in list:
                        check = item.split(",")
                        print(check[0],"|",check[1])
                    list.close
                except:
                    with open(todoPath,"w") as create:
                        list = open(todoPath, "r+")
                        print("Task | Checked")
                        for item in list:
                            check = item.split(",")
                            print(check[0],"|",check[1])
                        list.close
                        create.close
        file2.close
default()
