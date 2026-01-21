import random

random_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        user_guess = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue
    attempts += 1 
        
    if user_guess < 1 or user_guess > 100:
        print("Your guess is out of bounds. Please try again.")
    elif user_guess < random_number:
        print("Too low! Try again.")
    elif user_guess > random_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")
        break
