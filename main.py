import pandas as pd
from typing import List, Dict, Any
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import isodate
from data_analysis_barcharts import number_of_videos_per_category_gpt, number_of_videos_per_year
from data_analysis_time_series import category_views_gpt, monthly_video_upload_count_category_gpt, monthly_video_length_sum_category_gpt, monthly_likes_sum_category_gpt, monthly_comments_sum_category_gpt
from descriptive_analysis import total_descriptive_analysis


def parse_duration_to_minutes(duration: str) -> int:
    """
    Function to parse and convert duration to minutes.
    isodate takes isodate duration format (ex: PT29M9S)
    and turns it into mathmetical number.
    """
    parsed_duration = isodate.parse_duration(duration)
    return int(parsed_duration.total_seconds() // 60)  # Convert seconds to minutes


if __name__ == "__main__":
    """
    You can access to all the functions I have written through these files:
    - data_analysis_time_series.py
    - data_analysis_barcharts.py
    - descriptive_analysis.py
    I did not use all the functions in my analysis. I did not have enough space in my report.
    """
    df = pd.read_csv("pewdiepie_videos_gpt.csv", encoding='utf-8')
    # df = df[pd.to_datetime(df['published_at']).dt.year >= 2022] # Enable this to look at videos just after 2022
    df = df[df['category_name_gpt'].isin(df['category_name_gpt'].value_counts().head(5).index)] # Enable this to see most occuring 5 video categories

    # Possible sampling %40 of data for more accuracy and clean data.
    # df = df.sample(frac=0.4, random_state=42)

    # Making sure quantitative data is numeric (integer).
    df['views'] = pd.to_numeric(df['views'], errors='coerce')
    df['likes'] = pd.to_numeric(df['likes'], errors='coerce')
    df['comments'] = pd.to_numeric(df['comments'], errors='coerce')
    # print(df.info())
    # print(df.head())
    # To see video duration in minutes I created a new column in DataFrame
    df['duration_minutes'] = df['duration'].apply(parse_duration_to_minutes)
    print(df.head())
    
    # Functions ending with "_gpt" means they are using the dataset cleaned by ChatGPT.
    number_of_videos_per_year(df)
    number_of_videos_per_category_gpt(df)
    monthly_video_upload_count_category_gpt(df)
    category_views_gpt(df)
    monthly_video_length_sum_category_gpt(df)
    monthly_likes_sum_category_gpt(df)
    monthly_comments_sum_category_gpt(df)

    # Some videos are premium. That gives 0 views, likes, comments since API does not access views of premium videos.
    # For cleaner data I took edge low cases out out. I guess some videos were not open to commenting before, and this left them in 0 comment.
    df = df[df['views'] > 0]
    df = df[df['likes'] > 0]
    df = df[df['comments'] > 100]
    total_descriptive_analysis(df)
