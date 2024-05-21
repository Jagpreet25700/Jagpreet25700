play = input("Hello and welcome ato the Tresure hunting game. Please type 'Start' to play the game: ")

if play == "Start":
    crossroad = input("Great!!. Let play the game. You are at a crossroad. Select 'L' to go Left or 'R' to go Right: ")
else:
    print("Game over. this is gibberish")    

if crossroad == "L":
    left = input("You have selected left. You reached near lake with a island in the middle. You can take the boat or swim to the island. Type 'Wait' to ge the Boat or 'Swim'to the swim: ")
    if left == "Wait":
        print("WAIT")
        door = input("the boat has arrived and it took you to the island. Upon reaching the island you see three doors 'Red','Yellow','Blue'. Please type R or Y or B to continue: ")
        if door == "R":
            print("OOPS!! You opened the Red door. There was a fire in the room in which you have burnt yourself. You died! GAME OVER")
        elif door == "B":
            print("OOPS!! You opened the Blue door where you encountered a crocodile. After a fight which was not worth(for obvious reasons) the crocodile eats you.\n GAME OVER.")
        else:
            print('CONGRATULATIONS!! YOU HAVE FOUND THE TRESURE. NOW YOU CAN CALL YOUR SELF "CAPTIAN COOL"')
    else:
        print("You selected to swim. I don't think that you are sane cause when you have a option to wait for some time you selected to SWIM.\n You swimmed to island and in the middle you saw a shark. Shark ate you and you died. GAME OVER")                      
else:
    print("You have selected right. You went in to the forest where you get bit by a snake. You died because of poison. GAME OVER")    