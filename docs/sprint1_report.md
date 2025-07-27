### ✅ Sprint 1 Report – Blind Assistant Project

**Sprint Goal:** Set up the project foundation and test core AI components for vision captioning and text-to-speech (TTS).
**Sprint Status:** ✅ Successfully Completed

---

## 🧭 Sprint Objective

Lay the groundwork for the Blind Assistant project by:

* Setting up the folder structure and GitHub repository
* Integrating and testing core AI components (BLIP and TTS)
* Documenting API functions for future integrations

---

## ✅ Completed Tasks
|  # | Task                                       | Description                                                                               | Status |
| -: | ------------------------------------------ | ----------------------------------------------------------------------------------------- | ------ |
|  1 | **Setup Local Project in VS Code**         | Initialized a Python virtual environment, organized folder structure                      | ✅ Done |
|  2 | **Install and Test TTS Engines**           | Tested `pyttsx3`, `Coqui TTS`, and `Piper`. Finalized **Piper** as TTS engine             | ✅ Done |
|  3 | **Install and Test Vision-Language Model** | Installed BLIP (`transformers`, `torch`, `PIL`) and generated captions from static images | ✅ Done |
|  4 | **Integrate TTS + Captioning**             | Combined both modules to read captions aloud from an image                                | ✅ Done |
|  5 | **Setup GitHub Repo + Folder Structure**   | Created GitHub repository and set up clean folder structure                               | ✅ Done |
|  6 | **Document Core Engine API**               | Wrote `core_api.md` with full docstring-style usage for both core functions               | ✅ Done |

---

## 📁 Project Folder Structure (Post-Sprint 1)

```
blind-assistant/
├── core/
│   ├── vision_captioning.py      # Image captioning with BLIP
│   ├── text_to_speech.py         # Piper TTS integration
│   └── tts_testing/              # Manual test scripts
├── demo/
│   └── test_images/              # Sample images for testing
├── docs/
│   ├── core_api.md               # Core module API documentation
│   └── sprint1_report.md         # This sprint report
├── README.md
└── requirements.txt              # Dependencies list
```

---

## 🔬 Key Learnings

* ***Piper*** TTS did not perform as expected due to slow response time and model invocation issues on your system. It will be revisited or replaced in future sprints if performance doesn't improve.
* `transformers` BLIP model can effectively caption real-world images, making it ideal for blind assistant applications.
* A consistent modular design (e.g., `core/` vs `demo/`) helped maintain a clean codebase for upcoming features.

---

## 🚫 Issues Faced & Resolutions

| Issue                                  | Resolution                                                       |
| -------------------------------------- | ---------------------------------------------------------------- |
| `pyttsx3` module circular import error | Avoided naming script as `pyttsx3.py` to fix circular import     |
| Piper `output.wav` not generated       | Replaced with shorter text input, verified `--output_file` path  |
| Slow TTS on low-end systems            | Verified model size and reduced latency with lighter voice model |
| BLIP image captioning runtime errors   | Ensured correct device usage and image size preprocessing        |

---

## 🛠️ Tools & Tech Used

* **Python 3.10+**
* **BLIP via HuggingFace Transformers**
* **Pillow** for image loading
* **VS Code** (Development Platform)
* **Git + GitHub** for version control

---

## 📚 Documentation Added

* [`core_api.md`](./core_api.md) – Full API-level documentation for `get_caption()` and `speak()`

---

## ✅ Sprint Goal Achieved

All tasks of Sprint 1 were completed successfully. Core AI modules are ready and tested, documentation is in place, and project structure is established for scaling.

---

## 🔜 Next Sprint – Sprint 2 Preview

> **Goal:** Build a CLI prototype that lets users input an image and receive spoken feedback describing it.

Key tasks:

* Implement CLI interface to accept image input
* Integrate `get_caption` and `speak` inside a CLI runner script
* Handle image load, error messages, and audio playback

---
