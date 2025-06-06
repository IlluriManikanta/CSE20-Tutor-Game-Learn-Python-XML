import xml.etree.ElementTree as ET
import sys
import os

class AdventureGame:
    def __init__(self, file_path, player_name, lives):
        self.prompts = self.load_prompts(file_path)
        self.player_name = player_name
        self.score = 0
        self.lives = lives
        self.max_lives = lives

    def load_prompts(self, file_path):
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' not found.")
            sys.exit(1)

        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
        except ET.ParseError:
            print("Error: Failed to parse the XML file.")
            sys.exit(1)

        prompts = {}
        for prompt in root.findall('prompt'):
            prompt_id = prompt.get('id')
            text = prompt.find('text').text if prompt.find('text') is not None else ''
            options = []
            for option in prompt.findall('option'):
                option_text = option.text
                next_prompt = option.get('next')
                options.append((option_text, next_prompt))
            prompts[prompt_id] = {'text': text, 'options': options}
        return prompts

    def loseHealth(self, amount=1):
        self.lives -= amount
        print(f"Lives remaining: {self.lives}")
        if self.lives <= 0:
            print("You're out of lives. Game over.")
            sys.exit(0)

    def play(self):
        self.outputIntro()
        current_prompt_id = 'start'
        while current_prompt_id:
            if current_prompt_id not in self.prompts:
                print(f"Error: Prompt ID '{current_prompt_id}' not found.")
                break
            prompt = self.prompts[current_prompt_id]
            print(prompt['text'])
            options = prompt['options']
            if not options:
                print("The adventure ends here.")
                break
            for i, (opt_text, _) in enumerate(options, start=1):
                print(f"{i}. {opt_text}")
            try:
                choice = int(input("Choose an option: "))
                if 1 <= choice <= len(options):
                    _, next_prompt = options[choice - 1]
                    self.score += 1
                    current_prompt_id = next_prompt
                    if "fail" in next_prompt:
                        self.loseHealth()
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        print(f"Thanks for playing, {self.player_name}! Your final score was {self.score}.")

    def outputIntro(self):
        print("\033[96mWelcome to the Adventure Game!\033[0m")
        print(f"Good luck, {self.player_name}. You have {self.lives} lives.")
