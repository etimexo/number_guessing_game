import random as r
def guessing():
    print("Welcome to the number guessing game!")
    answer = input("Do you want to play? (y/n) ")
    if answer != 'y':
        quit()
    lower = int(input("Enter your lower limit: "))
    upper = int(input("Enter your upper limit: "))
    rand = r.randint(lower, upper)
    guesses = 0
    
    while True:
        guess = int(input("Guess the number! ")) 
        guesses += 1
        if guess > rand:
            print("That's high. Bring it down a little.")
        elif guess < rand:
            print("You're close. Go a bit higher.'")
        else:
            print("You got it in {} guesses!!".format(guesses))
            play = input("would you like to play again? (y/n) ")
            if play.lower() != 'y':
                break
guessing()