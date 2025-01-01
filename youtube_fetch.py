from googleapiclient.discovery import build
import query_builder as qb
import logging
import db_ops as db
import cfg

# Logging Def Settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def authenticate_youtube(api_key):
    """Auth for YouTube data api"""
    return build("youtube", "v3", developerKey=api_key)

def search_videos(youtube, published_before, max_results=50):
    """Search for videos published before a specific date."""
    search_query = qb.get_query()
    if cfg.USE_DATABASE == 'True':
        db.process_json_data()
    # Decide if publish_before attr gets pushed or not
    include_pub_date = qb.get_random_int(fortype="pub_date_chance")
    if include_pub_date > 100:
        try:
            request = youtube.search().list(
                part="id,snippet",
                q=search_query,
                type="video",
                publishedBefore=published_before,
                maxResults=max_results
            )
            response = request.execute()
            return response.get("items", [])
        except Exception as e:
            logging.error(f"Error during video search: {e}")
            return []
    else:
        try:
            request = youtube.search().list(
                part="id,snippet",
                q=search_query,
                type="video",
                maxResults=max_results
            )
            response = request.execute()
            return response.get("items", [])
        except Exception as e:
            logging.error(f"Error during video search: {e}")
            return []

def get_video_details(youtube, video_ids):
    """Retrieve details of videos by their IDs."""
    try:
        request = youtube.videos().list(
            part="snippet,statistics",
            id=','.join(video_ids)
        )
        response = request.execute()
        return response.get("items", [])
    except Exception as e:
        logging.error(f"Error fetching video details: {e}")
        return []

def filter_videos(videos, max_views):
    """Filter videos based on view count."""
    filtered = []
    for video in videos:
        try:
            view_count = int(video["statistics"].get("viewCount", 0))
            min_views = 1
            if view_count < max_views and view_count > min_views:
                filtered.append(video)
        except KeyError:
            logging.warning("Missing or invalid statistics for video:", video.get('id', {}).get('videoId', 'unknown'))
    return filtered