# AI Agent Instructions

This repository contains a simple Python desktop application built with `tkinter` and `Pillow` for learning Quranic Arabic vocabulary.

## 🏗️ Architecture & Entrypoints
- **Entrypoint**: `python main.py` is the main executable for the application.
- **Image Generation**: `text_to_png.py` is used to render text to images. This is likely how Arabic text is handled to bypass `tkinter` font rendering issues.
- **Data Source**: Vocabulary is read from `data/arabic_words.csv`.
- **State/Progress**: User progress is saved to simple text files (`data/learned_words.txt` and `data/need_to_learn.txt`). Avoid modifying these files directly during development unless specifically testing state resets.

## 🛠️ Setup & Commands
- **Dependencies**: Managed via `requirements.txt`. Always run within the virtual environment (`.venv`).
- **Linting**: Run `ruff check .` before committing changes. The configuration is in `ruff.toml` (which selectively ignores certain rules and uses preview features). 

## ⚠️ Quirks & Conventions
- **GUI Limitations**: Being a `tkinter` application, testing requires an active display (e.g., X11/Wayland). Avoid running GUI-dependent tests in headless environments without something like `xvfb`.
- **State management**: The app relies heavily on `global` variables (like `curr_record`, `curr_ar_image`, `flip_timer`) for tracking state across `tkinter` callbacks. Be careful when refactoring these to ensure event loops and callbacks don't break.
- **File I/O**: The application creates the `data/learned_words.txt` file automatically if it doesn't exist. Keep file paths relative to the project root (e.g., `"data/..."`).
