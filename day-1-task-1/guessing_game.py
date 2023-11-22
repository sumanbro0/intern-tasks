import random
print("Welcome to the Number guessing game")
guessing_number=random.randint(1,100)
attempt=3

while(attempt>0):
    guessed_number=int(input("Enter Your Guess: "))
    if guessed_number==guessing_number:
        print("Congratulations You got it right")
        break
    elif guessed_number>guessing_number:
        print("Your guess is higher than the guessing number")
    elif guessed_number<guessing_number:
        print("Your guess is lower than the guessing number")
    else:
        print("Invalid input")
    
    attempt=attempt-1

    if attempt==0:
        print("You Lost, Do you want to play again?  ")
        play_again=str(input("Enter (yes/no): "))
        if play_again.lower()=="yes":
            attempt=3
        else:
            print("Bye...")