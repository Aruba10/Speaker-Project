# 🎙️ AI-Driven Speaker Identification and Captioning

A Python-based AI project that identifies multiple speakers from an audio file and generates speaker-wise captions using Speaker Diarization and Automatic Speech Recognition (ASR).

---

## 📋 Project Description

This project demonstrates how artificial intelligence techniques can be used to analyze audio conversations. It integrates **Speaker Diarization** and **Speech-to-Text (ASR)** to generate meaningful captions with speaker identification.

### Key Features:

* 🔹 **Speaker Identification:** Detects different speakers in audio
* 🔹 **Speaker Diarization:** Segments audio into speaker-wise parts
* 🔹 **Automatic Speech Recognition:** Converts speech into text
* 🔹 **Caption Generation:** Produces speaker-wise captions
* 🔹 **Modular Design:** Separate files for each functionality
* 🔹 **Simple & Lightweight:** Beginner-friendly implementation

---

## 🛠️ Technology Stack

### Core Technology

* **Python 3.x** – Programming language

### Concepts Used

* **Speaker Diarization** – Identifying “who spoke when”
* **ASR (Automatic Speech Recognition)** – Converting speech to text

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or higher
* Any code editor (VS Code recommended)

---

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/AI-Driven-Speaker-Identification.git
cd AI-Driven-Speaker-Identification
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

### ▶️ Run the Project

```bash
python main.py
```

---

## 📁 Project Structure

```
AI-Driven-Speaker-Identification/
│
├── audio/
│   └── sample.wav
│
├── diarization.py        # Speaker segmentation
├── asr.py                # Speech-to-text conversion
├── captioning.py         # Caption formatting
├── main.py               # Main integration file
├── requirements.txt
└── README.md
```

---

## ⚙️ System Workflow

1. Audio file is provided as input
2. Speaker diarization divides audio into segments
3. Each segment is passed to ASR
4. Text is generated for each speaker
5. Final output shows speaker-wise captions

---

## 🎯 Sample Output

```
AI-Driven Speaker Identification and Captioning

Speaker 1: Good morning everyone.
Speaker 2: Today we will discuss our project.
Speaker 1: Thank you for listening.
```

---

## 📌 Applications

* 🗣️ Meeting transcription
* 🎤 Interview analysis
* 🎓 Online lecture captioning
* 🤖 Voice-based AI systems

---

## 🔧 Future Improvements

* Integrate real ASR models (e.g., Whisper)
* Add real-time audio processing
* Improve speaker accuracy using ML models
* Web-based UI for better interaction

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

---

## 📄 License

This project is for educational purposes.

---

## 👩‍💻 Author

ARUBA BAIG

---

## 🙏 Acknowledgments

* Inspiration from AI-based speech processing systems
* Open-source community for learning resources

---

✨ Built with Python and basic AI concepts
