
import random
to_guess_no = random.randint(1,100)

print("what is your name?")
name=input()
count = 0

print("Guess a number between 1 and 100, "+ name)
guessed_number=int(input())
count += 1

while guessed_number != to_guess_no:
        count += 1
        if guessed_number < to_guess_no:
            print("Go higher")
            guessed_number=int(input())
                  
        elif guessed_number > to_guess_no:
            print("Go lower")
            guessed_number=int(input())
            
        if guessed_number==to_guess_no:
            print("You guessed the correct number "+name+" which is " + str(to_guess_no)+ ' in '+str(count)+" guesses")


          
