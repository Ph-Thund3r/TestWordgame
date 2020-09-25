import random
#Coded by Noob-Thund3r
print("""
===========================================
[                                         ]
[    Welcome to number guessing game!     ]
[                                         ]
[                                         ]
===========================================""")
def start():
    def again():
        dec = input("""
1.) Exit
2.) Play again
""")
        if dec == "1":
            exit()
        elif dec == "2":
            start()
        else:
            print("Input error!")
            again()
    dif = input("""
1.) Easy (0-5)
2.) Medium (0-10)
3.) Hard (0-20)
Enter Difficulty level:""")
    if dif == "1":
        num = random.randint(0, 5)
        att = int(input("Input how many attempts:"))
        while True:
            ans = int(input("What number is your guess?:"))
            att -= 1
            if ans == num:
                print("You win!")
                again()
            elif ans < num:
                print("Too Low!")
                print("Try again!")
                print("============")
            elif ans > num:
                print("Too High!")
                print("Try again!")
                print("===========")

            if att == 0:
                print("You Lose!")
                again()
    elif dif == "2":
        num = random.randint(0, 10)
        att = int(input("Input how many attempts:"))
        while True:
            ans = int(input("What number is your guess?:"))
            att -= 1
            if ans == num:
                print("You win!")
                again()
            elif ans < num:
                print("Too Low!")
                print("Try again!")
                print("============")
            elif ans > num:
                print("Too High!")
                print("Try again!")
                print("===========")

            if att == 0:
                print("You Lose!")
                again()
    elif dif == "3":
        num = random.randint(0, 20)
        att = int(input("Input how many attempts:"))
        while True:
            ans = int(input("What number is your guess?:"))
            att -= 1
            if ans == num:
                print("You win!")
                again()
            elif ans < num:
                print("Too Low!")
                print("Try again!")
                print("============")
            elif ans > num:
                print("Too High!")
                print("Try again!")
                print("===========")

            if att == 0:
                print("You Lose!")
                again()
    else:
        print("Error!")
        start()
start()
