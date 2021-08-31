import random
player_score = 0
com_score = 0 

while True:
    print("\n")
    print("It's your turn, player!")
    player_turn = 0
    while True:
        p_roll = random.randint(1,6)
        print("A " + str(p_roll) + " was rolled!")
        player_turn += p_roll
        if p_roll == 1:
            print("Bummer! Your turn is over.")
            break
        kg = int(input("Would you like to (1) Hold or (2) Keep rolling? "))
        if kg == 1:
            print("Nice! You earned " + str(player_turn) + " points.")
            print("You have " + str(player_score + player_turn) + " points!")
            player_score += player_turn
            break
    if player_score >= 100:
        print("You Won!")
        break
    
    print("\n")
    print("It's computer turn!")
    com_turn = 0
    while True:
        c_roll = random.randint(1,6)
        print("A " + str(c_roll) + " was rolled!")
        com_turn += c_roll
        if c_roll == 1:
            print("Bummer! Computer turn over.")
            break
        cg = random.randint(1,2)
        if cg == 1:
            print("Nice! Computer earn " + str(com_turn) + " points.")
            print("Computer have " + str(com_score + com_turn) + " points!")
            com_score += com_turn
            break
    if com_score >= 100:
        print("Computer Win!")
        break
