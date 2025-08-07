### ✅ AI Powered Youtube Video summarizer

```markdown
# 🎥 YouTube Transcript Summarizer

A Python-based automation project to extract transcripts from YouTube videos and summarize them using OpenAI’s language models. Built with a clean modular design and an interactive Streamlit UI.

This project is part of my [Web API Automation](https://github.com/Madhavi1108/Web_API_Automation) collection.

---

## 🚀 Project Timeline & Tasks

| Day | Task                                                   | Status |
|-----|--------------------------------------------------------|--------|
| 1   | Extract Video ID from YouTube URL                      | ✅ Done |
| 2   | Fetch YouTube Transcript using `youtube-transcript-api`| ✅ Done |
| 3   | Clean & Prepare Transcript                             | 🔜 Upcoming |
| 4   | Use OpenAI API to Summarize                            | 🔜 |
| 5   | Build Streamlit UI                                     | 🔜 |
| 6   | Enhance UI & Add Features                              | 🔜 |
| 7   | Finalize Code & Upload to GitHub                       | 🔜 |

---

## 💡 Features (Planned)

- Input any YouTube URL  
- Automatically extract and clean the transcript  
- Summarize long transcripts using OpenAI  
- User-friendly Streamlit web interface  
- Error handling for missing/disabled transcripts  
- Support for multilingual transcripts (optional)

---

## 🛠️ Technologies Used

- Python 3.x
- youtube-transcript-api
- OpenAI API (upcoming)
- Streamlit
- Regular Expressions (`re`)
- urllib for URL parsing

---

## 📂 Folder Structure

```

youtube-summarizer/
├── day1\_extract\_video\_id.py
├── day2\_fetch\_transcript.py
├── day3\_clean\_transcript.py
├── day4\_openai\_summary.py
├── app\_streamlit.py
├── README.md

````

---

## ✅ How to Run

1. Clone the repo
```bash
git clone https://github.com/Madhavi1108/Web_API_Automation.git
cd Web_API_Automation/youtube-summarizer
````

2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install youtube-transcript-api
```

4. Run current test (example from Day 2)

```python
from youtube_transcript_api import YouTubeTranscriptApi

yta = YouTubeTranscriptApi()
transcript = yta.fetch("dQw4w9WgXcQ")  # replace with your video ID
for line in transcript:
    print(line)
```

---

## 🎯 Progress

* [x] Day 1 - Extract Video ID ✅
* [x] Day 2 - Fetch Transcript ✅
* [ ] Day 3 - Clean Transcript
* [ ] Day 4 - OpenAI Summary
* [ ] Day 5 - Streamlit UI
* [ ] Day 6 - UI Enhancement
* [ ] Day 7 - Final Touches + GitHub

---

## 📃 License

This project is for educational purposes.
Feel free to fork or contribute under the MIT License.

---

## 🙋‍♀️ Author

* [Madhavi1108](https://github.com/Madhavi1108)

````