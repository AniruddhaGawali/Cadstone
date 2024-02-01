import random

x = "n"

#Generate a random number between 1 and 6 (inclusive)

x = input("Press y to roll again and n to exit: ")
while x=="y":
    no = random.randint(0,6)

    if no == 1:
        print("[-----]")
        print("[-----]")
        print("[--0--]")
        print("[-----]")
        print("[-----]")
        
    if no == 2:
        print("[-----]")
        print("[--0--]")
        print("[-----]")
        print("[--0--]")
        print("[-----]")
        break
    if no == 3:
        print("[-----]")
        print("[--0--]")
        print("[--0--]")
        print("[--0--]")
        print("[-----]")
    if no == 4:
        print("[-----]")
        print("[0---0]")
        print("[-----]")
        print("[0---0]")
        print("[-----]")
    if no ==5:
        print("[-----]")
        print("[0---0]")
        print("[--0--]")
        print("[0---0]")
        print("[-----]")
    if no == 6:
        print("[-----]")
        print("[0---0]")
        print("[0---0]")
        print("[0---0]")
        print("[-----]")

    x = input("Press y to roll again and n to exit: ")


        