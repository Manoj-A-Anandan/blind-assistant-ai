# 🧠 Blind Assistant – Core Engine API Documentation

This document describes the core functions of the assistant's intelligence layer: visual captioning and text-to-speech.

---

## 📷 `get_caption(image)`

### Purpose:
Generate a scene description from an image using a vision-language model (BLIP).

### File:
`core/vision_captioning.py`

### Signature:
```python
get_caption(image: PIL.Image.Image) -> str
