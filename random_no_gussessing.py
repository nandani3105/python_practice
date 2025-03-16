import random
print("computer has guess a number you have to find out in between 1to 10")
n = random.randrange(1,10)
guess = int(input("Enter any number: "))
while n!= guess:

    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
        break
print("you guessed it right!!")