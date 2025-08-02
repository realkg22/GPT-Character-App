import azure.cognitiveservices.speech as speechsdk
import os

class SpeechToTextManager:
    azure_speechconfig = None
    azure_audioconfig = None
    azure_speechrecognizer = None

    def __init__(self):
        # Creates an instance of a speech config with specified subscription key and service region.
        # Replace with your own subscription key and service region (e.g., "westus").
        try:
            self.azure_speechconfig = speechsdk.SpeechConfig(subscription=os.getenv('AZURE_TTS_KEY'), region="westus")
        except TypeError:
            exit("Oops! You forgot to set AZURE_TTS_KEY in your environment!")
        
        self.azure_speechconfig.speech_recognition_language="en-US"

    def get_text_to_speech(self):
        self.azure_speechrecognizer = speechsdk.SpeechRecognizer(speech_config=self.azure_speechconfig)

        # Start recognition (one-shot)
        result = self.azure_speechrecognizer.recognize_once_async().get()
        text_result = result.text

        # Handle result
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(result.text))
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized.")
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation = result.cancellation_details
            print("Canceled: {}".format(cancellation.reason))
            if cancellation.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation.error_details))

        print(f"The following text was the result: {text_result}")
        return text_result

if __name__ == "__main__":
    speech_to_text_manager = SpeechToTextManager()
    speech_to_text_manager.get_text_to_speech()