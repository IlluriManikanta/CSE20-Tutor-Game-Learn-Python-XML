import xml.etree.ElementTree as ET
import sys
import os

def load_prompts(file_path):
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
        if prompt_id is None:
            print("Error: A prompt is missing its 'id' attribute.")
            sys.exit(1)
        text = prompt.find('text').text if prompt.find('text') is not None else ''
        options = []
        for option in prompt.findall('option'):
            option_text = option.text
            next_prompt = option.get('next')
            if option_text is None or next_prompt is None:
                print(f"Error: Option in prompt '{prompt_id}' is malformed.")
                sys.exit(1)
            options.append((option_text, next_prompt))
        prompts[prompt_id] = {'text': text, 'options': options}
    return prompts

def play_game(prompts):
    current_prompt_id = 'start'
    while current_prompt_id:
        if current_prompt_id not in prompts:
            print(f"Error: Prompt ID '{current_prompt_id}' not found.")
            break
        prompt = prompts[current_prompt_id]
        print(prompt['text'])
        options = prompt['options']
        if not options:
            break
        for i, (opt_text, _) in enumerate(options, start=1):
            print(f"{i}. {opt_text}")
        try:
            choice = int(input("Choose an option: "))
            if 1 <= choice <= len(options):
                _, next_prompt = options[choice - 1]
                current_prompt_id = next_prompt
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def run(file_path):
    prompts = load_prompts(file_path)
    play_game(prompts)
