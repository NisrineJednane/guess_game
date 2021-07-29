import random

answer = random.randrange(1,100)
difficulty = input("Hard or easy mode?\n").lower()
user_guess = int(input("Guess a number:\n"))

if difficulty == "easy":
  tries = 10
if difficulty == "hard":
  tries = 5 

while user_guess != answer:
  if tries == 1:
    print("you ran out of guesses, game over")
    break
  if user_guess < answer:
    print("you guessed too low")
    tries -= 1
    print(f"you have {tries} guesses left ")
    user_guess = int(input("Guess a number:\n"))
  if user_guess > answer:
    print("you guessed too high")
    tries -= 1
    print(f"you have {tries} guesses left ")
    user_guess = int(input("Guess a number:\n"))
else:
  print("congratulations, you guessed it right")
