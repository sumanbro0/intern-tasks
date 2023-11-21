import random
guessing_number=random.randint(1,100)
print("Welcome to the Number guessing game")
attempt=3
while(attempt>0):
    guessed_number=int(input("Enter Your Guess: "))
    if guessed_number==guessing_number:
        print("Congratulations You got it right")
        break
    elif guessed_number>guessing_number:
        print("Your guess is higher than the guessing number")
        guessed_number=int(input("Enter Your Guess: "))
    elif guessed_number<guessing_number:
        print("Your guess is lower than the guessing number")
        guessed_number=int(input("Enter Your Guess: "))
    else:
        print("Invalid input")

    attempt=attempt-1
    print(f'{attempt} chances remaining')