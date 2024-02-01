import random

x = "y"

#Generate a random number between 1 and 6 (inclusive)

x = input("Press y to roll again and n to exit: ")
while x=="y":
    no = random.randint(1,6)

    if no == 1:
        for i in range(5):
            if i == 2:
                print("[--0--]")
            else:
                print("[-----]")


        
    if no == 2:
        for i in range(5):
            if i==1 or i==3:
                print("[--0--]")
            else:
                print("[-----]")


    if no == 3:
        for i in range(5):
            if i==1 or i==2 or i==3:
                print("[--0--]")
            else:
                print("[-----]")
                
    if no == 4:
        for i in range(5):
            if i==1 or i==3:
                print("[0---0]")
            else:
                print("[-----]")
                

    if no ==5:
        for i in range(5):
            if i==1 or i==3:
                print("[0---0]")
            elif i==2:
                print("[--0--]")
            else:
                print("[-----]")

    if no == 6:
        for i in range(5):
            if i==1 or i==3 or i==2:
                print("[0---0]")
            else:
                print("[-----]")
                
    x = input("Press y to roll again and n to exit: ")


        