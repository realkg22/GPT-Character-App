import time
import keyboard
from rich import print
from azure_tts import SpeechToTextManager
from eleven_labs import ElevenLabsManager
from open_ai import OpenAiManager
import os
import yaml

speechtotext_manager = SpeechToTextManager()
elevenlabs_manager = ElevenLabsManager()
openai_manager = OpenAiManager()

with open("voice_config.yaml", "r") as f:
    voice_config = yaml.safe_load(f)

while True:
    print("[bold yellow]WHICH CHARACTER DO YOU CHOOSE TO BE YOUR IGL???")
    print("1. Phoenix")
    print("2. Chamber")

    user_choice = input("Pick a character!!! ").strip()

    if user_choice == "1":
        character = voice_config["phoenix"]
        voice_id = character["voice_id"]
        personality = character["personality"]
        break
    elif user_choice == "2":
        character = voice_config["chamber"]
        voice_id = character["voice_id"]
        personality = character["personality"]
        break
    else:
        print("Oh no!!! You didn't pick a character!!!")

FIRST_SYSTEM_MESSAGE = {"role": "system", "content": personality}

openai_manager.chat_history.append(FIRST_SYSTEM_MESSAGE)

print("[green]Beginning the program, press F4 to begin!")
while True:
    if keyboard.read_key() != "f4":
        time.sleep(0.1)
        continue

    print("[green]User pressed F4! Now listening to your mic: ")

    mic_output = speechtotext_manager.get_text_to_speech()

    if mic_output == '':
        print("[red]No response was received from your microphone!")
        continue

    chatgpt_result = openai_manager.chat_with_history(mic_output)

    elevenlabs_output = elevenlabs_manager.text_to_speech(chatgpt_result, voice_id)

    print("[green]\n!!!!!!!\nFINISHED PROCESSING DIALOGUE.\nREADY FOR NEXT INPUT\n!!!!!!!\n")