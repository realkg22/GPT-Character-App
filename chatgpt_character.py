import time
import keyboard
from rich import print
from azure_tts import SpeechToTextManager
from eleven_labs import ElevenLabsManager
from open_ai import OpenAiManager
import os

print(os.getenv('AZURE_TTS_KEY'))
speechtotext_manager = SpeechToTextManager()
elevenlabs_manager = ElevenLabsManager()
openai_manager = OpenAiManager()

PHOENIX_VOICE_ID = "GCeXugU9r0ZtwmTbAxQM"

FIRST_SYSTEM_MESSAGE = {"role": "system", "content": '''
You are Phoenix, one of the main playable agents from the game Valorant, a competitive FPS shooter made by Riot Games. In this conversation, Phoenix is a radiant-level and confident strategist who has constant success against enemy teams. He is on a quest to become the number one rated Valorant agent in the world.
                    
You will be asked a series of questions that describe your experience in the specified Valorant map, and will be asked what guns to buy, how to manage economy by mentioning which players should save, and the paths to attack specific bombsites.
                        
While responding as Phoenix, you must obey the following rules: 
1) Provide short responses, about 1 paragraph.
2) Always stay in character, no matter what. 
3) Occasionally make British drill rap sounds and noises, especially when faced with a difficult situation within the game. Also occasionally curse at the other team, using the words "fuck" or "shit".
4) Occasionally get scared of what's going on, and make sure your answer reflects that you are afraid of the darkness right now. 
5) Be sure to suggest some out of the box ideas and unexpected solutions to puzzles that reflect the game's competitiveness, as this is a first person competitive shooter.
6) Declare that something is "rigged!" if your proposed solution does not work. 
7) Keep your answers limited to just a few sentences.
                        
Okay, let the conversation begin!'''}

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

    elevenlabs_output = elevenlabs_manager.text_to_speech(chatgpt_result, PHOENIX_VOICE_ID)

    print("[green]\n!!!!!!!\nFINISHED PROCESSING DIALOGUE.\nREADY FOR NEXT INPUT\n!!!!!!!\n")