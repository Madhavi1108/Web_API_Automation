import re
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
import google.generativeai as genai

# ==== CONFIGURE YOUR GEMINI API KEY HERE ====
API_KEY = "AIzaSyDHUWc3Xp9-llca9m6hrzYFmZH6h-2NvAc"

st.title("🎥 YouTube Transcript Summarizer")
url = st.text_input("Enter YouTube URL:")

if st.button("Generate Summary"):
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", url)

    if match:
        video_id = match.group(1)
        print("Video ID:", video_id)

        try:
            yta = YouTubeTranscriptApi()
            transcript = yta.fetch(video_id)

            # Join all text
            full_text = " ".join([line.text for line in transcript])

            # Remove brackets like [Silly Dog: Mm.] or (Laughs)
            cleaned_text = re.sub(r"\)", "", full_text)

            # Remove musical notes
            cleaned_text = re.sub(r"[♪♫]", "", cleaned_text)

            # Remove multiple spaces
            cleaned_text = re.sub(r"\s{2,}", " ", cleaned_text)

            print("\n--- Cleaned Transcript ---\n")
            print(cleaned_text)  # Preview

            # Summarize using Gemini API
            genai.configure(api_key=API_KEY)
            model = genai.GenerativeModel("models/gemini-2.5-pro")

            response = model.generate_content(f"Summarize this transcript: {cleaned_text}")

            st.subheader("Summary")
            st.write(response.text)

        except TranscriptsDisabled:
            st.error("❌ Transcripts are disabled for this video.")
        except NoTranscriptFound:
            st.error("❌ No transcript found.")
        except VideoUnavailable:
            st.error("❌ Video is unavailable.")
        except Exception as e:
            st.error(f"❌ Unexpected error: {str(e)}")

    else:
        st.error("❌ No match found for Video ID.")
