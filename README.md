# 🕌 Quranic Flashcards

> A simple, lightweight desktop application built in Python for learning and memorizing words from the Quran.

![Placeholder for App Screenshot](https://via.placeholder.com/800x526?text=App+Screenshot)

## 💡 Motivation

Learning a new language, especially a classical one like Quranic Arabic, requires consistent practice and repetition. I built this flashcard app to create a focused, distraction-free environment to memorize vocabulary. Instead of relying on heavy web applications or ad-filled mobile apps, this tool runs locally, tracks your progress in simple text files, and provides a clean, responsive UI built with `tkinter` and `Pillow`.

## 🚀 Quick Start

Follow these steps to get the application running on your local machine.

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/flash_card.git
cd flash_card
```

### 2. Set up a virtual environment (Optional but recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app!
```bash
python main.py
```

## 📖 Usage

Once you launch the app, you will be presented with a flashcard showing an Arabic word from the Quran. 

- **Flipping the Card**: The card will automatically flip after a few seconds to reveal the English translation and the part of speech.
- **Marking as Known**: Click the **✅ (Right)** button if you knew the word. It will be saved to `data/learned_words.txt` so you aren't tested on it again.
- **Marking as Unknown**: Click the **❌ (Wrong)** button if you didn't know the word. The word will be logged in `data/need_to_learn.txt` for your review, and you will be tested on it again in the future.
- **Completion**: Once you have learned all the words in the provided CSV dataset, a "Reset" button will appear, allowing you to clear your progress and start over.

### Adding Custom Words
The application reads vocabulary from `data/arabic_words.csv`. You can easily add your own words by editing this file. Ensure your CSV has the following columns:
- `ID`: A unique identifier for the word.
- `Arabic`: The Arabic word.
- `English`: The English translation.
- `Is a _`: The part of speech (e.g., Noun, Verb, Preposition).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! 

### Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/flash_card.git
cd flash_card

# Install dependencies
pip install -r requirements.txt

# Run linting
ruff check .

# Run the application
python main.py
```

If you'd like to contribute, please fork the repository and open a pull request to the `main` branch.
