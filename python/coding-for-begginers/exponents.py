# page28 global defence program

aliens=2
password="shelly"
print("Qickely! Aliens are invading the planet.")
print("You need to activate the global defence platforms")
print("Hope you know the password for earths sake")
print()
print("-----------------------------------------")
print("     WElCOME TO THE GOBAL DEFENCE NETWORK     ")
print("------------------------------------------")
print()
guess=input("please enter password").upper()
while guess!=password:
    print()
    print("incorrect password")
    print()
    aliens=aliens**2
    print("there are",aliens,"aliens now on earth. try again")
    if aliens>7400000000:
        break
    print()
    print("password hint: the things that are attacking us")
    print()
    guess=input("quick!please enter password").upper()
if aliens>7400000000:
    print('noooooo! the aliens have outnumbered us. all is lost')
else:
    print("hooray!we wone the fight! the worls is safe")
