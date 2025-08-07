import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable

url = "https://www.youtube.com/watch?v=_8DPM_kqKbI&list=PLADbhCPI8Be7aHFv40RVGQv9NabkTBigw"
pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
match = re.search(pattern, url)

if match:
    video_id = match.group(1)
    print("Video ID:", video_id)

    try:
        yta = YouTubeTranscriptApi()
        transcript = yta.fetch(video_id)

        for line in transcript:
            print(line)

    except TranscriptsDisabled:
        print("❌ Transcripts are disabled for this video.")
    except NoTranscriptFound:
        print("❌ No transcript found.")
    except VideoUnavailable:
        print("❌ Video is unavailable.")
    except Exception as e:
        print("❌ Unexpected error:", str(e))

else:
    print("❌ No match found for Video ID.")
