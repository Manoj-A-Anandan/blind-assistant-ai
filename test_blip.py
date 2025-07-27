# test_blip.py

from core.vision_captioning import get_caption
import os

image_dir = "demo/test_images"

for file in os.listdir(image_dir):
    if file.lower().endswith(("jpg", "jpeg", "png")):
        path = os.path.join(image_dir, file)
        caption = get_caption(path)
        print(f"{file} ➜ {caption}")
