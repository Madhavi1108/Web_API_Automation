# 🎥 YouTube Transcript Summarizer

A Python + Streamlit application to extract transcripts from YouTube videos, clean them, and summarize them using **Google Gemini 2.5 Pro**.  
Built with the original `.fetch()` method logic — no changes to functionality — now with a fully working interactive Streamlit interface.

This project is part of my [Web API Automation](https://github.com/Madhavi1108/Web_API_Automation) collection.

---

## 🚀 Features

- Extract **Video ID** from any YouTube link (supports `youtube.com` & `youtu.be`)
- Fetch transcripts via `youtube-transcript-api` using `.fetch()` (original method preserved)
- Clean the transcript by removing:
  - Closing parentheses `)`
  - Musical notes `♪` / `♫`
  - Multiple spaces
- Summarize the cleaned transcript using **Google Gemini 2.5 Pro**
- **Streamlit UI** for easy, no-terminal use

---

## 🛠️ Technologies Used

- Python 3.x
- [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/)
- [`google-generativeai`](https://ai.google.dev/)
- [Streamlit](https://streamlit.io)
- Regular Expressions (`re`)

---

## 📂 Folder Structure

```

youtube-summarizer/
├── app\_streamlit.py     # Streamlit UI script
├── core\_script.py       # Original CLI script
├── README.md

````

---

## 💻 How to Run

1. **Install dependencies**
   ```bash
   pip install streamlit youtube-transcript-api google-generativeai
````

2. **Run the app**

   ```bash
   streamlit run app_streamlit.py
   ```

3. **Open in browser**

   * Local: `http://localhost:8501`
   * Or public link if using services like Colab + localtunnel

---

## 📄 Example Summary Output

**Input:** YouTube link
**Output:**

```
• Talks about the importance of creativity.
• Encourages audience to embrace new ideas.
• Concludes with a motivational call to action.
```

---

## 🎯 Project Timeline & Status

| Day | Task                                                    | Status |
| --- | ------------------------------------------------------- | ------ |
| 1   | Extract Video ID from YouTube URL                       | ✅ Done |
| 2   | Fetch YouTube Transcript using `youtube-transcript-api` | ✅ Done |
| 3   | Clean & Prepare Transcript + Summarize with Gemini AI   | ✅ Done |
| 4   | Build Streamlit UI                                      | ✅ Done |
| 5   | Enhance UI & Add Features                               | ✅ Done |
| 6   | Finalize Code & Upload to GitHub                        | ✅ Done |

---

## 📃 License

This project is for educational purposes.
Feel free to fork or contribute under the MIT License.

---

## 🙋‍♀️ Author

* [Madhavi1108](https://github.com/Madhavi1108)

