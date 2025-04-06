from googleapiclient.discovery import build
import pandas as pd
from typing import List, Dict, Any
import time

# Initialize the YouTube API client
api_key = "#"
youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_categories() -> Dict[str, str]:
    """
    Fetches a dictionary mapping category IDs to category names.

    Returns:
        Dict[str, str]: A mapping of category ID to category name.
    """
    categories = {}
    request = youtube.videoCategories().list(part="snippet", regionCode="US")
    # We are using "US" as region code to get standardized categories.
    response = request.execute()

    for item in response["items"]:
        categories[item["id"]] = item["snippet"]["title"]

    return categories

def get_channel_id(username: str) -> str:
    """
    This function returns channel id of the channel whose name is input as str.
    Basic request made from API.
    """
    request = youtube.search().list(
        part="snippet",
        q=username,
        type="channel",
        maxResults=1
    )
    response = request.execute()
    return response["items"][0]["id"]["channelId"]

def get_pewdiepie_uploads_playlist(channel_id: str) -> str:
    """
    I make another request in here that returns me the all videos the channel uploaded in its history.
    """
    request = youtube.channels().list(
        part="contentDetails",
        id=channel_id
    )
    response = request.execute()
    return response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

def get_pewdiepie_all_video_ids(playlist_id: str) -> List[Dict[str, Any]]:
    """
    In this function I access to the API and start pulling all video ids from the playlist.
    I store all video ids in a list and return it. Since API is maximum 50 for a page,
    I continue to make requests and append it to the list until all video ids are requested.
    """
    video_ids = []
    next_page_token = None

    while True:
        request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,  # Maximum allowed per request
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response["items"]:
            video_ids.append(item["contentDetails"]["videoId"])

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

        time.sleep(1)  # Avoid hitting rate limits

    return video_ids

def get_pewdiepie_all_video_details(video_ids: List) -> List[dict]:
    """
    I take all video ids as a list, then return a list of dictionaries with all videos' details in them.
    In the final part where I run main, this list of discionaries is used to create a csv file.
    """
    videos_data = []

    # I used ChatGPT for this loop.
    for i in range(0, len(video_ids), 50):  # Process in batches of 50 (API limit)
        request = youtube.videos().list(
            part="snippet,statistics,contentDetails,status",
            id=",".join(video_ids[i:i+50])
        )
        response = request.execute()

        # In the response of my request, I get all video details and append it to the list.
        for item in response["items"]:
            videos_data.append({
                "video_id": item["id"],
                "title": item["snippet"]["title"],
                "published_at": item["snippet"]["publishedAt"],
                "category_id": item["snippet"]["categoryId"],
                "duration": item["contentDetails"]["duration"],
                "views": item["statistics"].get("viewCount", 0),
                "likes": item["statistics"].get("likeCount", 0),
                "comments": item["statistics"].get("commentCount", 0)
            })

        time.sleep(1)  # Avoid hitting rate limits

    return videos_data

if __name__ == "__main__":
    """
    I execute all the functions that I written to request all videos of PewDiePie,
    with its categeories matched in a proper manner.
    """
    channel_id = get_channel_id("PewDiePie")
    uploads_playlist_id = get_pewdiepie_uploads_playlist(channel_id)
    pewdiepie_video_ids = get_pewdiepie_all_video_ids(uploads_playlist_id)
    pewdiepie_all_videos_details = get_pewdiepie_all_video_details(pewdiepie_video_ids)
    df_all_videos_pewdiepie = pd.DataFrame(pewdiepie_all_videos_details)

    # Get the category mapping
    category_mapping = get_video_categories()
    # Convert 'category_id' column to string (as API returns it as string)
    df_all_videos_pewdiepie["category_id"] = df_all_videos_pewdiepie["category_id"].astype(str)
    # Map category_id to category_name
    df_all_videos_pewdiepie["category_name"] = df_all_videos_pewdiepie["category_id"].map(category_mapping)
    print(df_all_videos_pewdiepie.head())
    df_all_videos_pewdiepie.to_csv('pewdiepie_videos.csv', index=False, encoding="utf-8")