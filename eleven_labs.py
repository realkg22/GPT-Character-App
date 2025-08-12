import os
from elevenlabs.client import ElevenLabs
from elevenlabs import play
import subprocess
import io
from pydub import AudioSegment
import simpleaudio as sa

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

        audio_bytes = b"".join(audio)
        with open("input.mp3", "wb") as f:
            f.write(audio_bytes)

        # Run ffmpeg to speed up with atempo
        subprocess.run([
            "ffmpeg", "-y", "-hide_banner", "-loglevel", "quiet", "-i", "input.mp3", 
            "-filter:a", "atempo=1.2", 
            "-vn", "output.mp3"
        ])

        audio_mp3 = AudioSegment.from_file("output.mp3")
        self.play_audio(audio_mp3)
    
    def play_audio(self, audio):
        play_obj = sa.play_buffer(
            audio.raw_data,
            num_channels=audio.channels,
            bytes_per_sample=audio.sample_width,
            sample_rate=audio.frame_rate
        )
        play_obj.wait_done()
          
if __name__ == "__main__":
    manager = ElevenLabsManager()
    input_text = "Alright, hear me out — we go half-buy, light armor, a couple Sheriffs or Stingers."
    phoenix_voice_id = "GCeXugU9r0ZtwmTbAxQM"
    manager.text_to_speech(input_text, phoenix_voice_id)