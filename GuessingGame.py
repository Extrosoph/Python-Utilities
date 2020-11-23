import random

def guess():
    x = random.randint(1, 101)
    count = 0
    while count < 5:
        y = int(input("Enter a number: "))
        if y > x:
            print("Try a smaller number")
        elif y < x:
            print("Try a larger number")
        elif y == x:
            print ("you are correct, you have guessed ",count," times.")
        count += 1
    print("Out of guesses")
guess()
    

