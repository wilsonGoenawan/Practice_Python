import utils as ut
import random

counter = 0


randnum = random.randrange(1,10)

while True:
    
    user_guess = input("input your guess: ")
    if user_guess == "exit":
        print(counter)
        break
    user_guess = int(user_guess)
    counter += 1
    if randnum == user_guess:
        print("exactly right!")
    elif randnum < user_guess:
        print("Too high")
    elif randnum > user_guess:
        print("Too low")
    

