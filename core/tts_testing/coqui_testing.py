from TTS.api import TTS

# Init the TTS engine (this downloads default model)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

# Run
tts.tts_to_file(text="Hello! I'm your blind assistant.", file_path="core/tts_testing/coqui_output.wav")

print("✅ Coqui audio saved: coqui_output.wav")
