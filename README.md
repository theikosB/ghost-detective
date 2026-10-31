# 👻 The Ghost Detective

*A mystery at Blackthorn Manor.*

**The Ghost Detective** is an interactive, AI-powered detective game built with [Streamlit](https://streamlit.io/) and Google’s Gemma model. Investigate a suspicious theft, examine evidence, question suspects, and decide whether the strange occurrences at Blackthorn Manor have a rational explanation.

> Trust the evidence. Question everything.

## 🕯️ The Case: The Clockmaker’s Last Hour

The Nocturne Prototype, the most valuable invention of clockmaker Elias Voss, has vanished from his locked study.

The windows are latched. The study door was locked. And several people claim to have witnessed something unusual in the halls of Blackthorn Manor.

You play as **Detective Rowan Hale**—a methodical investigator who does not believe in ghosts.

Your task is to reconstruct the events of the night, identify the thief, and decide what to make of the manor’s unexplained incidents.

## ✨ Features

- **Interactive investigation** — examine physical evidence and documents found around the manor.
- **Suspect profiles** — explore the motives, statements, and personalities of the people connected to the case.
- **Unexplained incidents** — investigate strange occurrences while keeping witness reports separate from established facts.
- **AI-powered interrogation** — question suspects, test theories, and explore the case through a Gemma-powered detective assistant.
- **Progressive hints** — receive increasingly specific guidance when you need a nudge.
- **Detective’s notebook** — keep track of observations and deductions throughout the investigation.
- **Case verdict** — name your suspect when you’re ready to submit your conclusion.
- **Atmospheric interface** — a vintage, dark casebook-inspired UI designed for the mystery.

## 🛠️ Built With

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Google Gemma](https://ai.google.dev/gemma)
- HTML and CSS for interface styling

The game uses hosted model inference rather than running a local language model.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/theikosB/ghost-detective.git
cd ghost-detective
```

### 2. Create and activate a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API credentials

Create a file at:

```text
.streamlit/secrets.toml
```

Add your credentials and model configuration:

```toml
GEMINI_API_KEY = "your-api-key"
GEMMA_MODEL = "your-supported-gemma-model"
```

Use a valid API key and model name supported by your configured Google GenAI access.

**Keep your API key private.** Do not commit `.streamlit/secrets.toml` or expose your credentials in screenshots, logs, or public code.

### 5. Run the game

```bash
streamlit run app.py
```

Streamlit will provide a local URL in your terminal. Open it in your browser to begin the investigation.

## 📁 Project Structure

```text
ghost-detective/
├── .streamlit/
│   └── secrets.toml       # Local API credentials (not committed)
├── app.py                 # Streamlit interface and game flow
├── case_data.py           # Case narrative, clues, suspects, and solution
├── detective.py           # Gemma-powered detective assistant
├── styles.css             # Custom interface styling
├── requirements.txt        # Python dependencies
└── README.md
```

## 🎮 How to Play

1. Read the case introduction and review the suspects.
2. Examine the available evidence.
3. Investigate the reported incidents around the manor.
4. Use the notebook to record observations and connect clues.
5. Ask the detective assistant questions to test your theories.
6. Use hints if you get stuck.
7. Submit your verdict when you believe you have solved the case.

The investigation is designed to encourage careful reasoning. A witness’s certainty is not the same as proof, and an unexplained event does not automatically establish a supernatural cause.

## 🧩 About the Project

The Ghost Detective was created as a small interactive mystery project exploring how generative AI can support narrative gameplay.

The goal is to combine a structured mystery—with evidence, suspects, and a defined intended solution—with an AI assistant that makes the investigation feel more conversational and exploratory.

---

*The house has its stories. The evidence has its limits.*

**Can you solve the case?**