players = input("1 or 2 players?")
if players == "1":
    p1 = input("chose rock, paper, scissors:")
    import random
    com = random.randint(1, 3)
    if p1 == "rock":
        if com == 1:
            print("draw")
        if com == 2:
            print("you lose")
        if com == 3:
            print("you win")
    elif p1 == "paper":
        if com == 1:
            print("you win")
        if com == 2:
            print("draw")
        if com == 3:
            print("you lose")
    elif p1 == "scissors":
        if com == 1:
            print("you lose")
        if com == 2:
            print("you win")
        if com == 3:
            print("draw")
    else:
        print("check spelling")
if players == "2":
    p2 = input("rock, paper, scissors")
    for i in range (20):
        print(" ")
    p3 = input("rock, paper, scissors")
    for i in range (20):
        print(" ")
    if p2 == "rock":
        if p3 == "rock":
            print("tie")
        elif p3 == "paper":
            print("player 2 won")
        elif p3 == "scissors":
            print("player 1 won")
        else:
            print("check spelling")
    elif p2 == "paper":
        if p3 == "rock":
            print("player 1 won")
        elif p3 == "paper":
            print("tie")
        elif p3 == "scissors":
            print("player 2 won")
        else:
            print("check spelling")
    elif p2 == "scissors":
        if p3 == "rock":
            print("player 2 won")
        elif p3 == "paper":
            print("player 1 won")
        elif p3 == "scissors":
            print("tie")
        else:
            print("check spelling")
    else:
        print("check spelling")