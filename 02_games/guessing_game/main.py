import random
import os

# ---------- Helper functions ----------

def load_scores(filename):
    """Load high scores from file into a dictionary."""
    scores = {}
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                if ":" in line:
                    name, score = line.strip().split(":")
                    scores[name] = int(score)
    return scores


def save_scores(filename, scores):
    """Save all scores back to the file."""
    with open(filename, "w") as file:
        for name, score in sorted(scores.items(), key=lambda x: x[1]):
            file.write(f"{name}:{score}\n")


def clear_leaderboard(filename):
    """Delete leaderboard file if user chooses."""
    ask = input("Do you want to clear the leaderboard? (yes/no): ").strip().lower()
    if ask == "yes" and os.path.exists(filename):
        os.remove(filename)
        print("🧹 Leaderboard cleared!\n")


def show_leaderboard(scores):
    """Display leaderboard neatly."""
    if not scores:
        print("🎮 No high scores yet — be the first to set one!\n")
        return
    print("\n🏆 Leaderboard:")
    for rank, (name, score) in enumerate(sorted(scores.items(), key=lambda x: x[1]), start=1):
        print(f" {rank}. {name} — {score} attempts")
    print()


# ---------- Main game function ----------

def play_game():
    highscore_file = "highscore.txt"

    # Ask if user wants to clear leaderboard
    clear_leaderboard(highscore_file)

    # Load leaderboard data
    scores = load_scores(highscore_file)

    print("🎯 I'm thinking of a number between 1 and 100...")
    show_leaderboard(scores)

    # Player setup
    player_name = input("Enter your name: ").strip().capitalize()

    # Set difficulty
    difficulty = input("Enter difficulty level (Easy/Hard): ").strip().lower()
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("❌ Invalid input. Please restart and choose Easy or Hard.")
        return

    # Generate random secret number
    secret = random.randint(1, 100)
    initial_attempts = attempts

    # Game loop
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

            # Update leaderboard
            if player_name not in scores or used < scores[player_name]:
                scores[player_name] = used
                print(f"🏅 New personal best! Congrats, {player_name}!")
                save_scores(highscore_file, scores)
            else:
                print(f"🙌 You didn’t beat your best of {scores[player_name]} attempts.")

            show_leaderboard(scores)
            break
    else:
        print(f"\n💀 Out of attempts! The number was {secret}. Better luck next time!")

    # Replay option
    again = input("\nPlay again? (yes/no): ").strip().lower()
    if again == "yes":
        print("\n🔁 Restarting the game...\n")
        play_game()
    else:
        print("\n👋 Thanks for playing!")


# ---------- Run the game ----------
if __name__ == "__main__":
    play_game()