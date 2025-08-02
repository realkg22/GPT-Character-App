import os
from elevenlabs.client import ElevenLabs
from elevenlabs import play


try:
    client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
except TypeError:
    exit("Oops! You forgot to set ELEVENLABS_API_KEY in your environment!")

class ElevenLabsManager:
    def __init__(self):
        pass
    
    def text_to_speech(self, input_text, voice_id):
        audio = client.text_to_speech.convert(
          text=input_text,
          voice_id=voice_id,
          model_id="eleven_multilingual_v2",
          output_format="mp3_44100_128"
        )

        play(audio)

          
if __name__ == "__main__":
    manager = ElevenLabsManager()
    input_text = "Alright, hear me out — we go half-buy, light armor, a couple Sheriffs or Stingers."
    phoenix_voice_id = "GCeXugU9r0ZtwmTbAxQM"
    manager.text_to_speech(input_text, phoenix_voice_id)