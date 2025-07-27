# 🧠 Blind Assistant – Core Engine API Documentation

This document outlines the core reusable functions powering the system.

---

## 📷 get_caption(image)

### Purpose:
Extract a descriptive caption from a given image using BLIP.

### Usage:
```python
caption = get_caption("demo/test_images/park.jpg")


---

## 🔊 speak(text)

### Purpose:
Convert a string of text into natural spoken audio using `pyttsx3` (offline and reliable).

### File:
`core/text_to_speech.py`

### Signature:
```python
speak(text: str, output_path: str = "core/output.wav") -> str
