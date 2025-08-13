TODO: create requirements.txt, backup chat history file, OBS websockets implementation

# GPT Character Chat
App that allows you to talk to characters using OpenAI.

Created for jengy13 at https://www.twitch.tv/jengy13.
Credit to DougDoug for idea and inspiration! (most of the code is his...)

## Things you will need :
1) Python (this app was written in Python 3.8, but 3.9 will also do) - https://www.python.org/downloads/

2) Microsoft Azure Account (for speech to text))

3) ElevenLabs Account (for character voicing)

4) OpenAI Account (for generated text using GPT-4o)


## Setup :
1) Install Python 3.8 or 3.9.

2) Run 'pip install -r requirements.txt' to install needed packages.

3) You will need to have accounts for Microsoft Azure, ElevenLabs, and OpenAI to use their services. Create accounts for these platforms and generate API keys. For Microsoft Azure, you will need to create a Speech service and use either of the provided API keys.
    - Note: Azure Speech services are free if you do not exceed a certain amount of characters a month (you need a TON of characters to exceed this). ElevenLabs has tiered pricing at $5/month for 30k characters/month, $22/month for 100k characters/month, and $99/month for 500k characters/month. GPT-4o is $5 for 1 million input tokens.

4) Add API keys for each of the services as environment variables named AZURE_TTS_KEY, ELEVENLABS_API_KEY, and OPENAI_API_KEY.

5) After creating an ElevenLabs account, create an AI voice and create an input in voice_config.yaml with that voice's voice ID and character personality. You may also modify the menu in chatgpt_character.py with characters that you have created.


### How to use : 
1) Run 'chatgpt_character.py'

2) Once it's running, press F4 to say something to your character.

3) Once you're done talking, the AI will generate a response and respond accordingly. It may take a couple seconds for the response to be played back.

4) After the AI has responded, press F4 to respond to the AI and keep the conversation going.
