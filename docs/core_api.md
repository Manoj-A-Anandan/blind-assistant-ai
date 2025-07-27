# 🧠 Blind Assistant – Core Engine API Documentation

This document describes the core functions of the assistant's intelligence layer: visual captioning and text-to-speech.

---

## 📷 get_caption(image)

### Purpose:
Generate a scene description from an image using a vision-language model (BLIP).

### File:
`core/vision_captioning.py`

### Signature:
```python
get_caption(image: PIL.Image.Image) -> str




Arguments:
image: A PIL.Image.Image object (already opened image)

Returns:
A string caption that describes the scene

Example:
python
Copy
Edit
from core.vision_captioning import get_caption
from PIL import Image

img = Image.open("demo/test_images/street.jpg")
caption = get_caption(img)
print(caption)  # e.g., "A man crossing a street with a traffic light"
🔊 speak(text)
Purpose:
Convert a string of text into natural spoken audio using Coqui TTS (offline).

File:
core/text_to_speech.py

Signature:
python
Copy
Edit
speak(text: str, output_path: str = "core/output.wav") -> str
Arguments:
text: A string containing the message to be spoken

output_path: File path where the generated WAV file will be saved (optional)

Returns:
Path to the audio file that was generated

Example:
python
Copy
Edit
from core.text_to_speech import speak

audio_path = speak("There is a bench to your right.")
print(f"Audio saved at: {audio_path}")
🔁 Combined Flow Example
python
Copy
Edit
from core.vision_captioning import get_caption
from core.text_to_speech import speak
from PIL import Image

img = Image.open("demo/test_images/park.jpg")
caption = get_caption(img)
speak(caption)