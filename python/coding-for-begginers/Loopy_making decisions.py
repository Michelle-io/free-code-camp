import random
exitChoice="nothing"
while exitChoice!=exit:


    print("You are in a dark room in a mysterious castle")
    print("There are four infrount of you, you must choose one")
    playerchoice = input("choose 1, 2, 3 or 4")
    if playerchoice == "1":
        print("You are in a room full of treasure. You are rich")
        print("Game Over,YOU WIN")
    elif playerchoice =="2":
        print("the door opens and an angry oger hits you with his club")
        print("you loose, Game Over")
    elif playerchoice=="3":
        print("you go into the room to find a sleeping dragon")
        print("1) to steal some of the dragons gold")
        print("2) try to sneak around the dragon to exit")
        dragonchoice =input("type 1 or 2")
        if dragonchoice == "1":
            print("the dragon wakes up and eats you. You are delicious")
            print("game over. you loose")
        elif dragonchoice == "2":
            print("you sneak around the dragon and escape the castle,blinking in the sunshine")
            print("game over. you win")
        else:
            print("sorry, you didnt answer 1 or 2")
    elif playerchoice == "4":
        print("you enter a room with a sphinx")
        print("it asks you to think of a number between 1 and 10")
        number = int(input("what number do you choose"))
        if number ==random.randint(1,10):
            print("the sphinx hisses in disappointment. you guessed correctly")
            print("she must let you go free")
            print("game over. you win")
        else:
            print("the sphinx tell you that your guess is incorrect")
            print("you are now her prisoner forever")
            print("game over you loose")
    else:
        print("sorry, you didnt enter 1, 2, 3 or 4")
    exitChoice=input('PRESS RETURN TO PLAY AGAIN, OR TYPE EXIT TO LEAVE')