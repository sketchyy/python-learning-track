import random

# Step 1: Pick a random number
secret = random.randint(1, 100)
attempts = 0

print("I'm thinking of a number between 1 and 100...")

# Step 2: Keep looping until the guess is correct
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    # Step 3: Check the guess
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"🎉 You got it! The number was {secret}.")
        print(f"Attempts: {attempts}")
        break
