import json
from googleapiclient.discovery import build

# YouTube API Details
API_KEY = "AIzaSyCI0mgf6EXWR5qqNe_7WWlLr_bbtQayI68"
VIDEO_ID = "cOdynPv8cok"

def get_youtube_comments(video_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    comments_data = []
    next_page_token = None

    while True:
        request = youtube.commentThreads().list(
            part="snippet,replies",  # Fetch replies too
            videoId=video_id,
            maxResults=100,  # API allows max 100 per request
            textFormat="plainText",
            pageToken=next_page_token
        )

        response = request.execute()

        # Extract comment details
        for item in response.get("items", []):
            snippet = item["snippet"]["topLevelComment"]["snippet"]

            comment_details = {
                "author": snippet.get("authorDisplayName"),
                "comment": snippet.get("textDisplay"),
                "likes": snippet.get("likeCount"),
                "published_at": snippet.get("publishedAt"),
                "total_replies": item["snippet"].get("totalReplyCount", 0),
                "replies": []
            }

            # Check if the comment has replies
            if "replies" in item:
                for reply in item["replies"]["comments"]:
                    reply_snippet = reply["snippet"]
                    comment_details["replies"].append({
                        "author": reply_snippet.get("authorDisplayName"),
                        "comment": reply_snippet.get("textDisplay"),
                        "likes": reply_snippet.get("likeCount"),
                        "published_at": reply_snippet.get("publishedAt")
                    })

            comments_data.append(comment_details)

        # Check if there's another page
        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break  # Exit loop if no more pages

    return comments_data

try:
    # Fetch all comment details
    comments = get_youtube_comments(VIDEO_ID, API_KEY)

    # Save to JSON file
    with open("data/raw/youtube_comments.json", "w", encoding="utf-8") as f:
        json.dump(comments, f, indent=4, ensure_ascii=False)

    print(f"✅ Fetched {len(comments)} comments successfully!")

except Exception as e:
    print(f"❌ Error fetching data: {e}")
