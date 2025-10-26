import random

# Step 1: Pick a random number
secret = random.randint(1, 100)

# Step 2: Set difficulty
difficulty = input("Enter difficulty level (Easy/Hard): ").strip().lower()

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("❌ Invalid input. Please restart and choose Easy or Hard.")
    exit()

print("\n🎯 I'm thinking of a number between 1 and 100...")

# Step 3: Keep looping until the guess is correct
while attempts > 0:
    print(f"\nAttempts left: {attempts}")
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("⚠️ Please enter a valid number.")
        continue

    attempts -= 1

    # Step 4: Check the guess
    if guess < secret:
        print("📉 Too low!")
    elif guess > secret:
        print("📈 Too high!")
    else:
        print(f"\n🎉 You got it! The number was {secret}.")
        print(f"You used {10 - attempts if difficulty == 'easy' else 5 - attempts} attempts.")
        break
else:
    print(f"\n💀 You ran out of attempts! The number was {secret}. Better luck next time!")
