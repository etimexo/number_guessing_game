# import random as r
# def easy():
#     lower = 1
#     upper = 100
#     rand = r.randint(lower, upper)
#     guesses = 0
    
#     while True:
#         guess = int(input("Guess the number! ")) 
#         guesses += 1
#         if guess > rand:
#             print("That's high. Bring it down a little.")
#         elif guess < rand:
#             print("You're close. Go a bit higher.'")
#         else:
#             print("You got it in {} guesses!!".format(guesses))
#             play = input("would you like to play again? (y/n) ")
#             if play.lower() != 'y':
#                 break
#             # else:
#             #     guessing()
# def medium():
#     lower = 100
#     upper = 1000
#     rand = r.randint(lower, upper)
#     guesses = 0
    
#     while True:
#         guess = int(input("Guess the number! ")) 
#         guesses += 1
#         if guess > rand:
#             print("That's high. Bring it down a little.")
#         elif guess < rand:
#             print("You're close. Go a bit higher.'")
#         else:
#             print("You got it in {} guesses!!".format(guesses))
#             play = input("would you like to play again? (y/n) ")
#             if play.lower() != 'y':
#                 break
#             # else:
#             #     guessing()
# def hard():
#     lower = 1000
#     upper = 10000
#     rand = r.randint(lower, upper)
#     guesses = 0
    
#     while True:
#         guess = int(input("Guess the number! ")) 
#         guesses += 1
#         if guess > rand:
#             print("That's high. Bring it down a little.")
#         elif guess < rand:
#             print("You're close. Go a bit higher.'")
#         else:
#             print("You got it in {} guesses!!".format(guesses))
#             play = input("Would you like to play again? (y/n) ")
#             if play.lower() != 'y':
#                 break
#             # else:
#             #     guessing()
# def guessing():
#     play_again = True
#     while play_again:
#         print("Welcome to the number guessing game!")

#         answer = input("Do you want to play? (y/n) ")
#         if answer != "y":
#             break
        
#         mode = input("Enter difficulty. (easy/medium/hard) ").lower()
#         if mode == "easy":
#             easy()
#         elif mode == "medium":  
#             medium()
#         elif mode == "hard":
#             hard()
#         else:
#             print("Enter a valid option")
#             continue
#         play_again = input("Would you like to play again? (y/n) ").lower() == 'y'
        
# guessing()
import random as r

def play_game(lower, upper):
    rand = r.randint(lower, upper)
    guesses = 0
    
    while True:
        guess = int(input("Guess the number! ")) 
        guesses += 1
        if guess > rand:
            print("That's high. Bring it down a little.")
        elif guess < rand:
            print("You're close. Go a bit higher.")
        else:
            print("You got it in {} guesses!!".format(guesses))
            play = input("Would you like to play again? (y/n) ")
            if play.lower() != 'y':
                return
            else:
                rand = r.randint(lower, upper)
                guesses = 0

def guessing():
    play_again = True
    while play_again:
        print("Welcome to the number guessing game!")

        answer = input("Do you want to play? (y/n) ")
        if answer.lower() != "y":
            break
        
        while True:
            mode = input("Enter difficulty. (easy/medium/hard) ").lower()

            if mode == "easy":
                play_game(1, 100)
            elif mode == "medium":  
                play_game(100, 1000)
            elif mode == "hard":
                play_game(1000, 10000)
            else:
                print("Enter a valid option")
                continue
            
    play_again = input("Would you like to play again? (y/n) ").lower() == 'y'

guessing()
