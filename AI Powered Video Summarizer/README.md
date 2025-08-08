# 🎥 YouTube Transcript Summarizer

A Python-based automation project to extract transcripts from YouTube videos and summarize them using OpenAI’s language models. Built with a clean modular design and an interactive Streamlit UI.

This project is part of my [Web API Automation](https://github.com/Madhavi1108/Web_API_Automation) collection.

---

## 🚀 Project Timeline & Tasks

| Day | Task                                                   | Status     |
|-----|--------------------------------------------------------|------------|
| 1   | Extract Video ID from YouTube URL                      | ✅ Done     |
| 2   | Fetch YouTube Transcript using `youtube-transcript-api`| ✅ Done     |
| 3   | Clean & Prepare Transcript                             | ✅ Done     |
| 4   | Use OpenAI API to Summarize                            | 🔜 Upcoming |
| 5   | Build Streamlit UI                                     | 🔜          |
| 6   | Enhance UI & Add Features                              | 🔜          |
| 7   | Finalize Code & Upload to GitHub                       | 🔜          |

---

## 🛠️ Technologies Used

- Python 3.x
- youtube-transcript-api
- OpenAI API (coming in Day 4)
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

## 🧼 Day 3 - Transcript Cleaning Details

Once the transcript is fetched, it contains entries like:

```python
FetchedTranscriptSnippet(text="Hello!", start=0.0, duration=1.3)
````

This script:

* Extracts only the `text` from each line
* Joins all lines into a single paragraph
* Cleans the text using regex to remove:

  * Musical notes like `♪` or `♫`
  * Bracketed expressions like `[Silly Dog: Mm.]` or `(Laughs)`
  * Extra whitespace

### 📄 Sample Cleaned Output:

```
A beautiful place full of smiles Where imaginations about you grow wildly The winter sun is like your white teeth ...
```

This cleaned text is now ready to be summarized using the OpenAI API (Day 4).

---

## ✅ How to Run This Step

```python
# Sample Code Snippet
full_text = " ".join([line.text for line in transcript])
cleaned_text = re.sub(r"[\[\(].*?[\]\)]", "", full_text)
cleaned_text = re.sub(r"[♪♫]", "", cleaned_text)
cleaned_text = re.sub(r"\s{2,}", " ", cleaned_text)
```

---

## 🎯 Progress

* [x] Day 1 - Extract Video ID ✅
* [x] Day 2 - Fetch Transcript ✅
* [x] Day 3 - Clean Transcript ✅
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

