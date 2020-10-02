import random

auto_generate = random.randint(1, 100)  # generates random no. automatically

name = input("what is your name?  ")  # user guesses the no.
counter = 0

print("Guess a number between 1 and 100 ")  # Guessing the number
guessed_number = int(input())
counter += 1
# checking user guesses
while guessed_number != int(auto_generate):
    counter += 1
    if guessed_number < int(auto_generate):
        print("Go higher")
        guessed_number = int(input())

    elif guessed_number > int(auto_generate):
        print("Go lower")
        guessed_number = int(input())

    if guessed_number ==int(auto_generate):
        print("You guessed the correct number " + name + " which is " + str(auto_generate) + ' in ' + str(
            counter) + " guesses")
