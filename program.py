import time, os, sys, random

class func:
    def clear():
        os.system('cls')
    def wait(t):
        time.sleep(t)
    def autotype(s, t):
        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(t)

class game:
    n=0
    def easy():
        n = random.randint(1, 10)
        i=0

        func.clear()
        print("WARNING: Only type in NATURAL (COUNTING) NUMBERS!")
        while True:
            i+=1
            print("Think of a number between 1 and 10")
            usrInput = input("Guess: ")
            if int(usrInput) == n:
                print()
                print("Well done! You did this in %s attempts!" % i)
                func.autotype("Do you want to play again?", 0.1)
                print()
                global rptInput
                rptInput = input("(y/n): ")
                if rptInput == "y":
                    break
                if rptInput == "n":
                    func.autotype("Thanks for playing!", random.uniform(0.01, 0.25))
                    sys.exit()
                else:
                    sys.exit()
            if int(usrInput) >= n:
                print("The number you guessed is too high.")
                func.wait(1)
            if int(usrInput) <= n:
                print("The number you guessed is too low.")

    def med():
        n = random.randint(1, 100)
        i=0

        func.clear()
        print("WARNING: Only type in NATURAL (COUNTING) NUMBERS!")
        while True:
            i+=1
            print("Think of a number between 1 and 100")
            usrInput = input("Guess: ")
            if int(usrInput) == n:
                print()
                print("Well done! You did this in %s attempts!" % i)
                func.autotype("Do you want to play again?", 0.1)
                print()
                global rptInput
                rptInput = input("(y/n): ")
                if rptInput == "y":
                    break
                if rptInput == "n":
                    func.autotype("Thanks for playing!", random.uniform(0.01, 0.25))
                    sys.exit()
                else:
                    sys.exit()
            if int(usrInput) >= n:
                print("The number you guessed is too high.")
                func.wait(1)
            if int(usrInput) <= n:
                print("The number you guessed is too low.")

    def hard():
        n = random.randint(1, 1000)
        i=0

        func.clear()
        print("WARNING: Only type in NATURAL (COUNTING) NUMBERS!")
        while True:
            i+=1
            print("Think of a number between 1 and 1000")
            usrInput = input("Guess: ")
            if int(usrInput) == n:
                print()
                print("Well done! You did this in %s attempts!" % i)
                func.autotype("Do you want to play again?", 0.1)
                print()
                global rptInput
                rptInput = input("(y/n): ")
                if rptInput == "y":
                    break
                if rptInput == "n":
                    func.autotype("Thanks for playing!", random.uniform(0.01, 0.25))
                    sys.exit()
                else:
                    sys.exit()
            if int(usrInput) >= n:
                print("The number you guessed is too high.")
                func.wait(1)
            if int(usrInput) <= n:
                print("The number you guessed is too low.")


def begin():
    while True:
        func.clear()
        func.autotype("Welcome to Guess and Go!", 0.01)
        func.wait(2)
        print('''
Begin?
y: YES    n: NO
''')
        beginInput = input("(y/n): ")
        if beginInput.lower() == "y":
            break
        if beginInput.lower() == "n":
            sys.exit()
        else:
            print("Invalid Input.")
            func.wait(2)
    while True:
        func.clear()
        func.autotype('''Which difficulty do you choose?
    1) Easy
    2) Medium
    3) Hard
''', 0.01)
        diffInput = input("(1/2/3): ")
        if diffInput == "1":
            game.easy()
        elif diffInput == "2":
            game.med()
        elif diffInput == "3":
            game.hard()
        else:
            print("Invalid Input.")
            func.wait(2)