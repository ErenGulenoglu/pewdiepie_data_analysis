import pandas as pd
from typing import List, Dict, Any
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def category_views_gpt(dataframe: pd.DataFrame):
    """Plots the monthly total views for each category."""
    df = dataframe.copy()
    df['published_at'] = pd.to_datetime(df['published_at'])  # Ensure datetime format
    plt.figure(figsize=(12, 6))
    # Group by category and resample to sum views per month
    for category, category_df in df.groupby("category_name_gpt"):
        monthly_category_views = category_df.resample('ME', on='published_at')['views'].sum()
        # Remove months with zero views
        monthly_category_views = monthly_category_views[monthly_category_views > 0]
        plt.plot(monthly_category_views, label=f'{category} Views', marker='o')
    # Improve readability
    plt.xlabel('Date')
    plt.ylabel('Total Views')
    plt.title('Monthly Views Per Category')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()

def monthly_video_upload_count_category_gpt(dataframe: pd.DataFrame):
    """Plots the number of videos uploaded per month for each category."""
    df = dataframe.copy()
    df['published_at'] = pd.to_datetime(df['published_at'])  # Ensure datetime format
    plt.figure(figsize=(12, 6))  
    # Group by category and resample to count videos per month
    for category, category_df in df.groupby("category_name_gpt"): # seperates each video to subset of dataframes (Categories)
        # Step 1: Resample the data by the end of each month ('ME')
        # - 'ME' stands for "Month-End," meaning we group data by the last day of each month.
        # - 'on="published_at"' tells resample() to use the 'published_at' column for time-based grouping.
        # - This ensures that videos are counted for the month they were published in.
        monthly_video_count = category_df.resample('ME', on='published_at')['video_id'].count()
        # Step 2: Count the number of videos per month
        # - 'video_id' is used because each video has a unique ID.
        # - .count() counts how many 'video_id' entries exist for each month.
        # - This effectively gives us the total number of videos uploaded in each category per month.
        # Remove months with zero uploads
        monthly_video_count = monthly_video_count[monthly_video_count > 0]
        plt.plot(monthly_video_count, label=f'{category} Videos', marker='o')
    # Improve readability
    plt.xlabel('Date')
    plt.ylabel('Number of Videos')
    plt.title('Monthly Video Uploads Per Category')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()

def monthly_video_length_sum_category_gpt(dataframe: pd.DataFrame):
    """Plots the total video lengths per month for each category."""
    df = dataframe.copy()
    df['published_at'] = pd.to_datetime(df['published_at'])  # Ensure datetime format
    plt.figure(figsize=(12, 6))
    # Group by category and resample to sum video lengths per month
    for category, category_df in df.groupby("category_name_gpt"):  # Separates each video to subset of dataframes (Categories)
        # Step 1: Resample the data by the end of each month ('ME')
        # - 'on="published_at"' groups the data by the publication date of videos.
        # - We sum the 'duration_minutes' for each month to get total video length.
        monthly_video_length = category_df.resample('ME', on='published_at')['duration_minutes'].sum()
        # Step 2: Remove months with zero video lengths (if necessary)
        monthly_video_length = monthly_video_length[monthly_video_length > 0]
        # Find the maximum month based on total video length
        # max_month = monthly_video_length.idxmax()  # This will give you the date of the max value
        # max_length = monthly_video_length.max()    # This will give you the total length for that month
        # # Convert the max month to a string format (e.g., 'May 2023')
        # max_month_str = max_month.strftime('%B %Y')  # e.g., 'May 2023'
        # print(f"Category: {category} - Max Month: {max_month_str}, Max Video Length: {max_length} minutes")
        # Plot the total video length per month for each category
        plt.plot(monthly_video_length, label=f'{category} Total Length (min)', marker='o')
    # Improve readability
    plt.xlabel('Date')
    plt.ylabel('Total Video Length (minutes)')
    plt.title('Monthly Video Length Per Category')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()

def monthly_likes_sum_category_gpt(dataframe: pd.DataFrame):
    """Plots the total likes per month for each category."""
    df = dataframe.copy()
    df['published_at'] = pd.to_datetime(df['published_at'])  # Ensure datetime format
    plt.figure(figsize=(12, 6))
    # Group by category and resample to sum likes per month
    for category, category_df in df.groupby("category_name_gpt"):  # Separates each video to subset of dataframes (Categories)
        # Step 1: Resample the data by the end of each month ('ME')
        # - 'on="published_at"' groups the data by the publication date of videos.
        # - We sum the 'likes' for each month to get total likes.
        monthly_likes = category_df.resample('ME', on='published_at')['likes'].sum()
        # Step 2: Remove months with zero likes (if necessary)
        monthly_likes = monthly_likes[monthly_likes > 0]
        # Plot the total likes per month for each category
        plt.plot(monthly_likes, label=f'{category} Total Likes', marker='o')
    # Improve readability
    plt.xlabel('Date')
    plt.ylabel('Total Likes')
    plt.title('Monthly Likes Per Category')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()

def monthly_comments_sum_category_gpt(dataframe: pd.DataFrame):
    """Plots the total comments per month for each category."""
    df = dataframe.copy()
    df['published_at'] = pd.to_datetime(df['published_at'])  # Ensure datetime format
    plt.figure(figsize=(12, 6))
    # Group by category and resample to sum comments per month
    for category, category_df in df.groupby("category_name_gpt"):  # Separates each video to subset of dataframes (Categories)
        # Step 1: Resample the data by the end of each month ('ME')
        # - 'on="published_at"' groups the data by the publication date of videos.
        # - We sum the 'comments' for each month to get total comments.
        monthly_comments = category_df.resample('ME', on='published_at')['comments'].sum()
        # Step 2: Remove months with zero comments (if necessary)
        monthly_comments = monthly_comments[monthly_comments > 0]
        # Find the maximum month based on total video length
        # max_month = monthly_comments.idxmax()  # This will give you the date of the max value
        # max_comments = monthly_comments.max()    # This will give you the total length for that month
        # Convert the max month to a string format (e.g., 'May 2023')
        # max_month_str = max_month.strftime('%B %Y')  # e.g., 'May 2023'
        # print(f"Category: {category} - Max Month: {max_month_str}, Max Video Comments: {max_comments} comments")
        # Plot the total comments per month for each category
        plt.plot(monthly_comments, label=f'{category} Total Comments', marker='o')
    # Improve readability
    plt.xlabel('Date')
    plt.ylabel('Total Comments')
    plt.title('Monthly Comments Per Category')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()
