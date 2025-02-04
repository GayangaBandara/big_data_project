import json
from googleapiclient.discovery import build

# Youtube API Details
API_KEY = "AIzaSyCI0mgf6EXWR5qqNe_7WWlLr_bbtQayI68"
VIDEO_ID = "cOdynPv8cok"

youtube = build('youtube', 'v3', developerKey=API_KEY)

request = youtube.commentThreads().list(
        part="snippet",
        videoId=VIDEO_ID,
        maxResults=1000,
        textFormat="plainText"
)
response = request.execute()

try:
    response = request.execute()  # Execute API request
    with open("data/raw/youtube_comments.json", "w") as f:  # Save to a JSON file
        json.dump(response, f, indent=4)
    print("✅ Data saved successfully!")

except Exception as e:
    print(f"❌ Error fetching data: {e}")

