import sys
import os
from AdventureGame import AdventureGame

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <prompt_file>")
        sys.exit(1)

    prompt_file = sys.argv[1]
    if not os.path.isfile(prompt_file):
        print(f"Error: The file '{prompt_file}' does not exist or cannot be opened.")
        sys.exit(1)

    name = input("Enter your name: ")
    total_stages = 4
    lives = min(3, total_stages)

    game = AdventureGame(prompt_file, name, lives)
    game.play()

if __name__ == "__main__":
    main()
