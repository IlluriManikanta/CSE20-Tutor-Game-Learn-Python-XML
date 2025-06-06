import sys
import os
import AdventureGame

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <prompt_file>")
        sys.exit(1)

    prompt_file = sys.argv[1]
    if not os.path.isfile(prompt_file):
        print(f"Error: The file '{prompt_file}' does not exist or cannot be opened.")
        sys.exit(1)

    AdventureGame.run(prompt_file)

if __name__ == "__main__":
    main()
