import random
import os

# Step 1: Pick a random number
secret = random.randint(1, 100)

# Step 2: Read previous high score (if file exists)
highscore_file = "highscore.txt"
if os.path.exists(highscore_file):
    with open(highscore_file, "r") as file:
        content = file.read().strip()
        highscore = int(content) if content.isdigit() else None
else:
    highscore = None

# Step 3: Set difficulty
difficulty = input("Enter difficulty level (Easy/Hard): ").strip().lower()
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("❌ Invalid input. Please restart and choose Easy or Hard.")
    exit()

print("\n🎯 I'm thinking of a number between 1 and 100...")
if highscore:
    print(f"🏆 Current High Score: {highscore} attempts")

# Step 4: Game loop
initial_attempts = attempts
while attempts > 0:
    print(f"\nAttempts left: {attempts}")
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("⚠️ Please enter a valid number.")
        continue

    attempts -= 1

    if guess < secret:
        print("📉 Too low!")
    elif guess > secret:
        print("📈 Too high!")
    else:
        used = initial_attempts - attempts
        print(f"\n🎉 You got it! The number was {secret}.")
        print(f"You used {used} attempts.")

        # Step 5: Update high score if needed
        if highscore is None or used < highscore:
            with open(highscore_file, "w") as file:
                file.write(str(used))
            print("🏅 New High Score! 🎊")
        break
else:
    print(f"\n💀 Out of attempts! The number was {secret}. Better luck next time!")
