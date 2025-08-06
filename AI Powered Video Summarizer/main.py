import re

url = ""
pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
match = re.search(pattern, url)

if match:
    print("Video ID:", match.group(1))
else:
    print("No match found")
