import pandas as pd
from typing import List, Dict, Any
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def number_of_videos_per_category_gpt(dataframe: pd.DataFrame) -> None:
    """
    Creates a bar plot for each video category and shows how many videos uploaded.
    """
    df = dataframe.copy()
    plt.figure(figsize=(12, 6))
    sns.countplot(
    y=df['category_name_gpt'], 
    order=df['category_name_gpt'].value_counts().index, 
    color="royalblue"  # Single color, still clear and readable
    )
    plt.xlabel("Number of Videos")
    plt.ylabel("Category Name")
    plt.title("Number of Videos per Category")
    plt.show()

def number_of_videos_per_year(dataframe: pd.DataFrame) -> None:
    """
    This function takes a DataFrame containing YouTube video data, extracts the year from 
    the 'published_at' column, and creates a bar chart showing the number of videos uploaded per year.
    """
    # Create a copy of the DataFrame to avoid modifying the original data
    df = dataframe.copy()    
    # Convert the 'published_at' column to datetime format (if it isn't already)
    df['published_at'] = pd.to_datetime(df['published_at'])
    # Extract only the year from the 'published_at' datetime column
    df['year'] = df['published_at'].dt.year
    print(df.info())
    # Set figure size for better visualization
    plt.figure(figsize=(12, 6))
    # Create a count plot showing the number of videos per year
    # sns.countplot() automatically counts how many times each year appears in the column and creates a bar chart. (KEY POINT)
    sns.countplot(
        x=df['year'],  # X-axis: year of video publication
        order=sorted(df['year'].unique(), reverse=False),  # Ensure years are in chronological order
        color="royalblue"  # Set bar color to royal blue for clarity
    )
    # Set axis labels and chart title
    plt.xlabel("Year")  # Label for the X-axis
    plt.ylabel("Number of Videos")  # Label for the Y-axis
    plt.title("Number of Videos per Year")  # Title of the plot
    # Display the plot
    plt.show()