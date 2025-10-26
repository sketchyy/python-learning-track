from game import play_number_game
from utils import clear_screen

def main():
    while True:
        clear_screen()
        print("🎮 Python Mini Game Hub")
        print("----------------------")
        print("1️⃣  Play Number Guessing Game")
        print("2️⃣  Exit")
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            play_number_game()
            input("\nPress Enter to return to menu...")
        elif choice == "2":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
