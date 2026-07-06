# AI-Powered Interview Prep Coach

A lightweight Streamlit app that generates tailored mock-interview questions
from your resume + a job description, lets you answer by voice, transcribes
and analyzes your answers, and builds a skill-gap learning roadmap.

## Features

- Resume (PDF) + Job Description + Target Company input
- Interview type selector: Behavioral / Technical / HR
- Difficulty level: Beginner / Intermediate / Advanced
- Company-flavored question generation (uses the AI's general knowledge)
- Voice answer recording → Whisper transcription (via Groq)
- Per-answer AI feedback: relevance score, STAR structure check, filler-word
  flag, pacing note, strengths, improvement suggestion
- Resume-to-Roadmap tab: skill gap analysis with a study plan per missing skill

## Tech Stack

| Layer | Tool |
|---|---|
| UI | Streamlit |
| LLM | Groq API — `llama-3.3-70b-versatile` |
| Speech-to-text | Groq API — `whisper-large-v3-turbo` |
| PDF parsing | pdfplumber |
| Mic input | streamlit-mic-recorder |
| Config | python-dotenv |

## Project Structure

```
interview_coach/
├── app.py              # Streamlit UI - all screens/tabs/session state
├── ai_engine.py         # All Groq LLM/Whisper calls + prompts (core AI logic)
├── resume_parser.py     # PDF -> plain text extraction
├── setup_check.py       # Run this first - verifies installs & .env
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## SETUP - Run These Steps In Order

### Step 1: Get the code on your machine
If you already have this folder locally, skip to Step 2.

### Step 2: Create a virtual environment (recommended, keeps installs isolated)
```bash
python -m venv venv
```
Activate it:
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```
You'll know it worked because your terminal prompt now shows `(venv)` at the start.

### Step 3: Install all dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Get a free Groq API key
1. Go to https://console.groq.com
2. Sign up (free, no credit card)
3. Go to **API Keys** -> **Create API Key**
4. Copy the key (starts with `gsk_...`)

### Step 5: Create your `.env` file
```bash
# Mac/Linux
cp .env.example .env

# Windows
copy .env.example .env
```
Open `.env` in any text editor and paste your real key:
```
GROQ_API_KEY=gsk_your_actual_key_here
```
Save the file.

### Step 6: Verify everything is set up correctly
```bash
python setup_check.py
```
This checks your Python version, confirms every package installed correctly,
and confirms your `.env` key is in place. Fix anything it flags before moving on.

### Step 7: Run the app
```bash
streamlit run app.py
```
It opens automatically at `http://localhost:8501` in your browser.

---

## Using the App

1. **Sidebar**: upload your resume PDF, paste the job description, optionally
   type a target company.
2. **Mock Interview tab**: pick interview type + difficulty -> "Generate
   Interview Questions" -> record your answer with the mic button -> get
   instant AI feedback per question.
3. **Skill Roadmap tab**: click "Analyze Skill Gaps" -> see matched skills
   and a study plan for missing ones.

---

## Pushing This to GitHub

```bash
# Inside the project folder
git init
git add .
git commit -m "Initial commit: AI Interview Prep Coach"

# Create a new repo on github.com first (don't initialize it with a README there),
# then copy its URL and run:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

**Important:** `.env` is already listed in `.gitignore`, so your real API key
will NOT be pushed to GitHub. Only `.env.example` (with a placeholder) gets
committed. When others clone your repo, they create their own `.env` using
Step 5 above.

---

## Notes for Report / Limitations

- Company-specific flavoring relies on the LLM's training knowledge, not a
  live web lookup - stronger for large, well-known companies, more generic
  for small/recent ones.
- Speech-to-text and feedback both depend on Groq's free-tier rate limits;
  expect brief delays under heavy use.
- Feedback parsing has a fallback path if the LLM doesn't return valid JSON
  on a given call, so the app won't hard-crash mid-demo.

## Possible Future Extensions (not built, for scope discussion)

- Adaptive follow-up questions based on answer quality
- Final aggregate "report card" across all answers in a session
- ATS keyword-matching between spoken answers and JD
- Tone/pitch audio analysis (e.g. via `librosa`) beyond just transcribed text
- Cross-session progress tracking (SQLite)
