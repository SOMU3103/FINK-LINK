<div align="center">

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Iron_Man_Tony_Stark.jpg/220px-Iron_Man_Tony_Stark.jpg" width="0" height="0"/>

<img src="https://img.icons8.com/color/200/000000/iron-man.png" alt="FINKLINK JARVIS" width="140"/>

<br/>
<h1 align="center">𝙵𝙸𝙽𝙺𝙻𝙸𝙽𝙺</h1>
<br/>

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Gemini AI](https://img.shields.io/badge/Google_Gemini_AI-4285F4?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev)
[![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-00C853?style=flat-square&logo=python&logoColor=white)]()
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)](https://opencv.org)
[![pyttsx3](https://img.shields.io/badge/pyttsx3-TTS_Engine-FF6D00?style=flat-square)]()
[![Status](https://img.shields.io/badge/Status-Active-00C853?style=flat-square)]()

<br/>

![Stars](https://img.shields.io/github/stars/SOMU3103/FINKLINK?style=flat-square&color=4fc3f7&labelColor=0a0a0a)
![Forks](https://img.shields.io/github/forks/SOMU3103/FINKLINK?style=flat-square&color=4fc3f7&labelColor=0a0a0a)
![Last Commit](https://img.shields.io/github/last-commit/SOMU3103/FINKLINK?style=flat-square&color=4fc3f7&labelColor=0a0a0a)
![Repo Size](https://img.shields.io/github/repo-size/SOMU3103/FINKLINK?style=flat-square&color=4fc3f7&labelColor=0a0a0a)
![License](https://img.shields.io/badge/license-MIT-4fc3f7?style=flat-square&labelColor=0a0a0a)

<br/>

[![GitHub Repo](https://img.shields.io/badge/⚙️_View_Repository-SOMU3103/FINKLINK-0a0a0a?style=for-the-badge&logo=github&logoColor=white)](https://github.com/SOMU3103/FINKLINK)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-somnath312006-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/somnath312006)

</div>

---

<div align="center">

```
  JARVIS   »  "Good morning, Sir. All systems are online."
  FINKLINK »  Awaiting your command...
```

</div>

---

## 〉 SYSTEM OVERVIEW

**FINK LINK** is your personal **J.A.R.V.I.S** — an AI-powered voice assistant that gives you complete, hands-free control over your laptop using nothing but your voice.

Just like Tony Stark spoke to JARVIS and the suit responded — **you speak, FINK LINK acts.**

Built with a purpose: designed especially for **people with disabilities** so that **every human being** can use a computer freely, without barriers.

> *"The most powerful input device ever created isn't a keyboard.*
> *It's the human voice."*

---

## 〉 COMMAND DIRECTORY

```
  ┌─────────────────────────────────────────────────────────┐
  │  SYSTEM MODULE                                          │
  ├─────────────────────────────────────────────────────────┤
  │  "wake up"               →  Greet + time & date         │
  │  "take screenshot"       →  Capture screen → save PNG   │
  │  "open settings"         →  Launch Windows Settings     │
  │  "camera"                →  Open live webcam preview    │
  │  "go to sleep"           →  Shut down assistant         │
  ├─────────────────────────────────────────────────────────┤
  │  APPS & MEDIA MODULE                                    │
  ├─────────────────────────────────────────────────────────┤
  │  "notepad"               →  Launch Notepad              │
  │  "youtube"               →  Open YouTube in browser     │
  │  "music"                 →  Play random local song      │
  │  "open gpt"              →  Start Gemini AI chatbot     │
  ├─────────────────────────────────────────────────────────┤
  │  KNOWLEDGE MODULE                                       │
  ├─────────────────────────────────────────────────────────┤
  │  "search <topic>"        →  Wikipedia search + speak    │
  ├─────────────────────────────────────────────────────────┤
  │  COMMUNICATION MODULE                                   │
  ├─────────────────────────────────────────────────────────┤
  │  "send whatsapp message" →  Prompt number → send msg    │
  │  "instagram"             →  Send Instagram DM           │
  ├─────────────────────────────────────────────────────────┤
  │  PRODUCTIVITY MODULE                                    │
  ├─────────────────────────────────────────────────────────┤
  │  "set alarm"             →  Voice-guided alarm setter   │
  └─────────────────────────────────────────────────────────┘
```

---

## 〉 HOW IT WORKS

```
        🎙️  You speak a command
                  │
                  ▼
        SpeechRecognition captures audio
                  │
                  ▼
        Google Speech API → text conversion
                  │
                  ▼
        Python keyword matching engine
                  │
          ┌───────┴────────┐
          ▼                ▼
    Simple Command     AI Command
    (app, alarm,       (Gemini chatbot,
     screenshot...)    Wikipedia...)
          │                │
          ▼                ▼
    Execute directly   API response
          │                │
          └───────┬────────┘
                  ▼
        pyttsx3 speaks result back to you
                  │
                  ▼
        🔊  "Done, Sir."
```

---

## 〉 TECH STACK

```yaml
Language        : Python 3.x
AI Engine       : Google Gemini Pro (generativeai)
Speech Input    : SpeechRecognition + Google Speech API
Voice Output    : pyttsx3 (Text-to-Speech Engine)
Computer Vision : OpenCV (webcam & photo capture)
Screenshot      : Pillow / ImageGrab
Wikipedia       : wikipedia-python
WhatsApp        : pywhatkit
Instagram DM    : instagrapi
Date & Time     : datetime (built-in)
IoT Ready       : Expandable via GPIO / MQTT
```

---

## 〉 WHY FINK LINK?

```
  THE PROBLEM
  ───────────────────────────────────────────────────────
  ✗  People with physical disabilities struggle with
     keyboards and mice
  ✗  Traditional computers require full motor function
  ✗  Existing voice tools are limited & expensive

  THE SOLUTION — FINK LINK
  ───────────────────────────────────────────────────────
  ✓  Full laptop control via natural voice commands
  ✓  AI-backed responses — not just keywords
  ✓  Free, open-source, customizable
  ✓  30% of e-commerce already runs on voice search
  ✓  Connects with IoT to control entire systems

  THE IMPACT
  ───────────────────────────────────────────────────────
  ♿  Accessibility   →  Technology for every human being
  ⚡  Efficiency      →  Voice is 3× faster than typing
  🎯  Convenience     →  Hands-free multitasking
  🤖  AI-Powered      →  Understands natural language
```

---

## 〉 INSTALLATION

**Step 1 — Clone the repository**
```bash
git clone https://github.com/SOMU3103/FINKLINK.git
cd FINKLINK
```

**Step 2 — Install dependencies**
```bash
pip install pyttsx3 SpeechRecognition google-generativeai \
            Pillow wikipedia pywhatkit opencv-python instagrapi
```

**Step 3 — Set your Gemini API key**
```python
# In main.py, replace:
genai.configure(api_key="# insert the End point key #")

# With your key from → https://ai.google.dev
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

**Step 4 — Set your music folder path**
```python
# In the music() function, update:
music = "C:\\Users\\YOUR_USERNAME\\Downloads\\Music"
```

**Step 5 — Launch FINK LINK**
```bash
python main.py
```

```
  JARVIS  »  "Welcome back, Sir. FINK LINK is ready."
```

---

## 〉 PROJECT STRUCTURE

```
FINKLINK/
│
├── 🤖  main.py             # Core assistant — all commands & logic
├── 📋  requirements.txt    # Python dependencies
└── 📖  README.md
```

---

## 〉 ROADMAP

```
  COMPLETED ✅
  ─────────────────────────────────────
  [✓]  Voice-controlled app launcher
  [✓]  Google Gemini AI chatbot
  [✓]  WhatsApp messaging via voice
  [✓]  Instagram DM automation
  [✓]  Alarm, camera, screenshot

  UPCOMING 🚀
  ─────────────────────────────────────
  [ ]  Multi-language voice support
  [ ]  GUI dashboard — command history
  [ ]  IoT device control (lights, fans)
  [ ]  Custom wake word  ("Hey JARVIS")
  [ ]  Mobile companion app
  [ ]  Face recognition login
```

---

## 〉 CONTRIBUTING

```bash
git checkout -b feature/new-command
git commit -m "feat: add new voice command"
git push origin feature/new-command
# → Open a Pull Request
```

---

## 〉 SECURITY NOTICE

> ⚠️ Never push your API keys or Instagram credentials to a public repo.
> Use a `.env` file and `python-dotenv` to keep secrets safe.

```bash
pip install python-dotenv
```

```python
from dotenv import load_dotenv
import os
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
```

---

## 〉 LICENSE

```
MIT License — Copyright (c) 2026 Somnath (SOMU3103)
Free to use, modify, and distribute with attribution.
```

---

<div align="center">

```
  ╔══════════════════════════════════════════════════════╗
  ║   Built by SOMU3103  ·  Team TECH MARVEL             ║
  ║   "Powered by AI. Driven by Voice. Built for All."   ║
  ╚══════════════════════════════════════════════════════╝
```

[![LinkedIn](https://img.shields.io/badge/LinkedIn-somnath312006-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/somnath312006)
&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-SOMU3103-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SOMU3103)

<br/>

*⭐ Star this repo if FINK LINK inspired you — it means the world!*

`🤖 — "Your voice is the new keyboard." — 🎙️`

</div>
