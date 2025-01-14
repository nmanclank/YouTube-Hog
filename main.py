import time
from datetime import datetime, timedelta, timezone
import logging
import random
import json
import query_builder as qb
import youtube_fetch as ytf
import cfg

google_cloud_key = cfg.GOOGLE_CLOUD_API

# Logging Def Settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def randomize_date_range():
    """Generate a random date from 2 to 18 years ago."""
    days_ago = random.randint(365 * 2, 365 * 18)  # Randomly select a day between 2 and 18 years ago
    date = datetime.now(timezone.utc) - timedelta(days=days_ago)
    return date.strftime("%Y-%m-%dT%H:%M:%SZ")  # Ensure correct RFC 3339 UTC format

def main():
    google_cloud_key: str = cfg.GOOGLE_CLOUD_API

    # Initialize YouTube API client
    youtube = ytf.authenticate_youtube(google_cloud_key)
    # Endless loop for continuous search
    while True:


        # Randomize the published date range for randomness
        PAST_DATE = randomize_date_range()
        logging.info(f"Searching for videos published before {PAST_DATE}...")

        # Search for videos older than the randomized date
        videos = ytf.search_videos(youtube, published_before=PAST_DATE)
        if not videos:
            logging.info("No videos found. Retrying...")
            time.sleep(10)
            continue

        # Extract video IDs
        video_ids = [video['id']['videoId'] for video in videos if 'videoId' in video['id']]

        # Get video details
        details = ytf.get_video_details(youtube, video_ids)

        # Determine randomized max views
        max_viewcount = qb.get_random_int(fortype="maxviewcount")

        # Filter videos based on view count
        low_view_videos = ytf.filter_videos(details, max_viewcount)

        # Log results including channel name
        date = datetime.fromisoformat(datetime.now().isoformat()).strftime("%Y-%m-%d")
        time_now = datetime.fromisoformat(datetime.now().isoformat()).strftime("%H_%M_%S")
        for video in low_view_videos:
            title = video['snippet']['title']
            views = video['statistics'].get('viewCount', 'N/A')
            channel = video['snippet']['channelTitle']
            logging.info(f"Found video: {title} by {channel} with {views} views")
        with open(f"json_data/Found_on_{date}_{time_now}_.json", "w", encoding="utf-8") as f:
            json.dump(low_view_videos, f, indent=2, ensure_ascii=False)

        # Pause to respect API limits
        logging.info("Waiting before the next search...")
        time.sleep(30)

if __name__ == "__main__":
    main()
