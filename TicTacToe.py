e = ""
b = "|"
f = "---+---+---"
c = "\n"
x = " X "
y = " O "
Vitoria1 = "Player 1 venceu"
Vitoria2 = "Player 2 venceu"

partidas = 0
check = 0
O = -1
X = -1
Casas = [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 "]

def Atualizar():
    global txt
    txt = Casas[0] + b + Casas[1] + b  + Casas[2] + c + f + c + Casas[3] + b + Casas[4] + b + Casas[5] + c + f + c + Casas[6]  + b + Casas[7] + b + Casas[8]
    print(txt)

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


def player1():
    global X
    if check == 0:
        X = int(input("Vez do X, escolha em quadrado: "))
        if Casas[X - 1] == y or Casas[X - 1] == x:
            print("Casa já ocupada" + c)
            player1()
        else:
            Casas[X - 1] = x
            Atualizar()

def player2():
    global O
    if check == 0:
        O = int(input("Vez do O, escolha em quadrado: "))
        if Casas[O - 1] == x or Casas[O - 1] == y:
            print("Casa já ocupada" + c)
            player2()
        else:
            Casas[O - 1] = y
            Atualizar()
    
Atualizar()

while check == 0:
    player1()
    Vitoria()
    if partidas == 8 and check == 0:
        print("Empate")
        break
    partidas += 1
    player2()
    Vitoria()
    partidas += 1
    if check == 1:
        print(Vitoria1)
        break
    if check == 2:
        print(Vitoria2)






    



    


