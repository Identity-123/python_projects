import random

def guess(x):
    low = 1
    high = x
    check = ''
    while check != 'c':
      #If there's a range of numbers (more than one possible number between 1 and 10), the computer randomly picks one.
        if low != high:
            guess_number = random.randint(low, high)
         # If there's only one number left in the range, the computer just uses that number  
        else:
            guess_number = low
   # in above code 
   #Let's say the range is 1 to 10, and initially, low = 1 and high = 10. 
   # Since there's a range of numbers, the computer randomly picks a number, let's say it picks 7.
   #  If, after some guesses, it finds out that the correct number is 7, then low becomes 7, and high also becomes 7. 
   # Now, since there's only one possible number left (7), the computer doesn't need to make a random guess anymore.
   #  It simply uses the remaining number (7) directly.
        check = input(f"Is {guess_number} too high (H), too low (L), or correct (C)? ".lower())
       
        if check == "h":
            high = guess_number - 1
        elif check == 'l':
            low = guess_number + 1

    print(f"Hurray! The computer guessed your number, and it is {guess_number}")

guess(100)
