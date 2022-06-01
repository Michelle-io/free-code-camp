print("You are in a dark room in a mysterious castle")
print("There are three infrount of you, you must choose one")
playerchoice = input("choose 1, 2, 3")
if playerchoice == "1":
    print("You are in a room full of treasure. You are rich")
    print("Game Over,YOU WIN")
elif playerchoice =="2":
    print("the door opens and an angry oger hits you with his club")
    print("you loose, Game Over")
elif playerchoice=="3":
    print("you go into the room and find a sleeping dragon")
    print("the dragon wakes up and eats you. you are delicious")
    print("Game Over. You loose")
else:
    print("sorry, you didnt enter 1, 2, 3")
print("run the game again to have another go")