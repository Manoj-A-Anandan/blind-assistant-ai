# File: core/text_to_speech.py

from TTS.api import TTS

# Initialize once during import
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

def speak(text: str, output_path: str = "core/output.wav") -> str:
    """
    Generate speech audio from text using Coqui TTS.
    
    Args:
        text (str): Text to convert to speech.
        output_path (str): Path to save the generated WAV file.

    Returns:
        str: Path to the saved audio file.
    """
    tts.tts_to_file(text=text, file_path=output_path)
    return output_path

# Sample test
if __name__ == "__main__":
    test_text = "This is your blind assistant speaking. Let's explore the world around you."
    path = speak(test_text)
    print(f"✅ Audio generated at: {path}")
