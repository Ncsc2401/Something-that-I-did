import random

e = ""
b = "|"
f = "---+---+---"
c = "\n"
x = " X "
y = " O "
ValidValues = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
Yes = ["Yes", "YES", "yes", "Y", "y", ""]
No = ["NO", "no", "No", "n", "N"]

def Reiniciar():
    global gametype
    global partidas
    global check
    global O
    global X
    global Casas
    global ia
    partidas = 0
    check = 0
    ia = -1
    O = -1
    X = -1
    Casas = [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 "]


#Set standart values
def Atualizar():
    global txt
    txt = Casas[0] + b + Casas[1] + b  + Casas[2] + c + f + c + Casas[3] + b + Casas[4] + b + Casas[5] + c + f + c + Casas[6]  + b + Casas[7] + b + Casas[8]

#Winning conditions
def Vitoria():
    global check
    if Casas[0] == x and Casas[1] == x and Casas[2] == x:
        check = 1
    elif Casas[3] == x and Casas[4] == x and Casas[5] == x:
        check = 1
    elif Casas[6] == x and Casas[7] == x and Casas[8] == x:
        check = 1
    elif Casas[0] == x and Casas[3] == x and Casas[6] == x:
        check = 1
    elif Casas[1] == x and Casas[4] == x and Casas[7] == x:
        check = 1
    elif Casas[2] == x and Casas[5] == x and Casas[8] == x:
        check = 1
    elif Casas[0] == x and Casas[4] == x and Casas[8] == x:
        check = 1
    elif Casas[2] == x and Casas[4] == x and Casas[6] == x:
        check = 1
    elif Casas[0] == y and Casas[1] == y and Casas[2] == y:
        check = 2
    elif Casas[3] == y and Casas[4] == y and Casas[5] == y:
        check = 2
    elif Casas[6] == y and Casas[7] == y and Casas[8] == y:
        check = 2
    elif Casas[0] == y and Casas[3] == y and Casas[6] == y:
        check = 2
    elif Casas[1] == y and Casas[4] == y and Casas[7] == y:
        check = 2
    elif Casas[2] == y and Casas[5] == y and Casas[8] == y:
        check = 2
    elif Casas[0] == y and Casas[4] == y and Casas[8] == y:
        check = 2
    elif Casas[2] == y and Casas[4] == y and Casas[6] == y:
        check = 2

def Gameselect():
    global gametype
    global restart
    gametypetemp = input("[1] Player Vs Player" + c + "[2] Player Vs IA" + c + "[3] Exit" + c)
    if gametypetemp == "1":
        gametype = 1
        Reiniciar()
        Atualizar()
        restart = 1
        print(txt)
    elif gametypetemp == "2":
        gametype = 2
        restart = 1
        Reiniciar()
        Atualizar()
        print(txt)
    elif gametypetemp == "3":
        gametype = 3
    else:
        print("Invalid Value")
        Gameselect()


#Player 1, X
def player1():
    global Xtemp
    global partidas
    global restart
    global gametype
    if check == 0:
        Xtemp = input("Choose a square (X):  ")
        if Xtemp in ValidValues:
            X = int(Xtemp)
            if Casas[X - 1] == y or Casas[X - 1] == x:
                print("Square occupied" + c)
                player1()
            else:
                Casas[X - 1] = x
                restart = 0
                Atualizar()
                if gametype == 1:
                    print(txt)
                partidas += 1
                Vitoria()
                Draw()
        elif Xtemp == "":
            Confirm = input("Restart?" + c)
            if Confirm in Yes:
                Gameselect()
                Reiniciar()
            if Confirm in No:
                player1()
        else:
            print("Invalid Value")
            player1()

#Player 2, O
def player2():
    global partidas
    global Otemp
    if check == 0:
        Otemp = input("Choose a square (O):  ")
        if Otemp in ValidValues:
            O = int(Otemp)
            if Casas[O - 1] == x or Casas[O - 1] == y:
                print("Square occupied" + c)
                player2()
            else:
                Casas[O - 1] = y
                Atualizar()
                print(txt)
                partidas += 1 
                Vitoria()
                Draw()
        elif Otemp == "":
            Confirm = input("Restart?" + c)
            if Confirm in Yes:
                Gameselect()
                Reiniciar()
            if Confirm in No:
                print(txt)
                player2()
        else:
            print("Invalid Value")
            player2()

def IA():
    global ia
    global partidas
    if check == 0:
        ia = random.randrange(0, 9)
        if Casas[ia] == x or Casas[ia] == y:
            IA()
        else:
            Casas[ia] = y
            Atualizar()
            print(txt)
            partidas += 1 
            Vitoria()
            Draw()
            
        

def Draw():
    global restart
    if partidas == 9 and check == 0:
        print("Draw")
        Reiniciar()
        Atualizar()
        restart = 1
        print(txt)

#Set the values
Reiniciar()
Gameselect()


while check == 0:
    if gametype != 3:
        player1()
        if gametype == 1 and check == 0 and restart == 0:
            player2()
        elif gametype == 2 and check == 0 and restart == 0:
            IA()
        elif restart == 1:
            pass
        if check == 2 and gametype == 2:
            print("IA Won")
            Reiniciar()
            Atualizar()
            print(txt)
        if check == 1 and gametype == 2:
            print("Player Won")
            Reiniciar()
            Atualizar()
            print(txt)
        if check == 1 and gametype == 1:
            print("Player 1 Won")
            Reiniciar()
            Atualizar()
            print(txt)
        if check == 2 and gametype == 1:
            print("Player 2 Won")
            Reiniciar()
            Atualizar()
            print(txt)
    else:
        break

