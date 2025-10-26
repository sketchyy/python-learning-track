import random
from utils import read_highscore, write_highscore, clear_highscore

def play_number_game():
    file_path = "highscore.txt"

    ask = input("Do you want to clear the leaderboard? (yes/no): ").strip().lower()
    if ask == "yes":
        clear_highscore(file_path)

    highscore_name, highscore_value = read_highscore(file_path)

    difficulty = input("Enter difficulty level (Easy/Hard): ").strip().lower()
    attempts = 10 if difficulty == "easy" else 5 if difficulty == "hard" else None

    if attempts is None:
        print("❌ Invalid input. Please restart and choose Easy or Hard.")
        return

    secret = random.randint(1, 100)
    print("\n🎯 I'm thinking of a number between 1 and 100...")

    if highscore_name:
        print(f"🏆 Current High Score — {highscore_name}: {highscore_value} attempts")

    player_name = input("\nEnter your name: ").strip().capitalize()

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

            if highscore_value is None or used < highscore_value:
                write_highscore(file_path, player_name, used)
                print(f"🏅 New High Score! 🎊 Congrats, {player_name}!")
            else:
                print(f"🙌 You didn’t beat {highscore_name}'s score of {highscore_value} attempts.")
            break
    else:
        print(f"\n💀 Out of attempts! The number was {secret}. Better luck next time!")
