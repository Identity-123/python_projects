import random
def guess(x):
  random_number = random.randint(1,x)

  guess = 0
  while(guess != random_number):
    guess = int(input(f"enter the random number between between 1 and {x}: "))
    if guess<random_number:
      print("sorry, your guess is too low")
    elif guess > random_number:
      print("Sorry, your guess is too high")
  print(f"Congratulation! , you guessed the number {random_number}")

guess(10)
