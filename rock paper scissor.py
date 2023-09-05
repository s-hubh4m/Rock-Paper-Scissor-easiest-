import random


def play():
    user=input(" 'r' is rock \n 'p' is paper \n 's' is scissor \n Choose: ")
    computer=random.choice(['r','p','s'])

    if (user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p' and computer=='r'):
        print("Congratulations! You won!")
    else:
        print("You lost")

x=input("Would you like a game of rock, paper, scissor? Y/N : ")

if (x=='Y'):
    play()
if (x=='y'):
    play()
if (x=='N'):
    print("CLICK 'OK' TO CLOSE THE GAME !")
    exit()
if (x=='n'):
    print("CLICK 'OK' TO CLOSE THE GAME !")
    exit()
    
t=input("Do you want to play again? Y/N : ")


while t=='Y':
    play()
    t=input("Do you want to play again? Y/N : ")
while t=='y':
    play()
    t=input("Do you want to play again? Y/N : ")   
if (t=='N'):
    print("Thanks for playing!")
    print("CLICK 'OK' TO CLOSE THE GAME !")
    exit()
if (t=='n'):
    print("Thanks for playing!")
    print("CLICK 'OK' TO CLOSE THE GAME !")
    exit()


