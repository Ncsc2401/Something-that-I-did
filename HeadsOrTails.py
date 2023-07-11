import random

def game():

    #input
    aposta = input("Heads or Tails?" + "\n")
    if aposta == "Heads" or aposta == "heads":
        a = 0
    elif aposta == "Tails" or aposta == "tails":
        a = 1
    else:
        a = 2
        print("Wrong Input")
    b = random.randrange(0, 2)

    #output
    if a == b and b == 0:
        print("Heads" + "\n" + "Player Won" + "\n")
    elif a == b and b == 1:
        print("Tails" + "\n" + "Player Won" + "\n")
    elif a != b and b == 0:
        print("Heads" + "\n" + "Player Lost" + "\n")
    elif a != b and b == 1:
        print("Tails" + "\n" + "Player Lost" + "\n")
    elif a == 2:
        pass
    else:
        print("Something gone wrong")
    game()
        
game()





