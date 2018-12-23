pathed = str(input("Input The Game's Locations Ex: C:\Program Files\GameFun\gun.exe: "))
nameInput = str(input("What is the name of the game? "))
writefile = open("games.csv","a+")
writefile.write(nameInput+","+pathed+"\n")
writefile.close
