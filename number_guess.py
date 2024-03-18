import random as r
def guessing():
    print("Welcome to the number guessing game!")
    answer = input("Do you want to play? (y/n) ")
    if answer != 'y':
        quit()
    lower = int(input("Enter your lower limit: "))
    upper = int(input("Enter your upper limit: "))
    rand = r.randint(lower, upper)
    
    while True:
        guess = int(input("Guess the number! ")) 
        if guess > rand:
            print("You guessed too high!")
        elif guess < rand:
            print("You guessed too low!")
        else:
            print("You got it!!")
            play = input("would you like to play again? (y/n) ")
            if play != 'y':
                break
guessing()