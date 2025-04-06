import pandas as pd
from typing import List, Dict, Any
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def total_descriptive_analysis(dataframe: pd.DataFrame) -> None:
    """
    This function first prints the overall measures of location and measures of spread for all videos.
    Then it prints out measures of location and measures of spread for all categories.
    """
    df = dataframe.copy()
    df['published_at'] = pd.to_datetime(df['published_at'])

    """
    I have taken all these calculation statements and methods from Week 9 exploratory analysis module.
    Functions such as mean, median are self explanatory.
    I used f string to round numbers with fractions.
    """

    mean_views_all = df['views'].mean() 
    print(f"Mean views of all time: {mean_views_all:,.2f}")
    median_view_all = df['views'].median()
    print(f"Median views of all time: {median_view_all:,.2f}")
    mode_view_all = df['views'].mode()[0]
    print(f"Mode views of all time: {mode_view_all:,.2f}")
    print(f"Range of views: {df['views'].max()-df['views'].min():,.2f}")
    print(f"Variance of views: {df['views'].var():,.2f}")
    print(f"Standard Deviation of views: {df['views'].std():,.2f}")
    print(f"IQR of views: {df['views'].quantile(0.75)-df['views'].quantile(0.25):,.2f}")
    print()

    mean_likes_all = df['likes'].mean() 
    print(f"Mean likes of all time: {mean_likes_all:,.2f}")
    median_likes_all = df['likes'].median()
    print(f"Median likes of all time: {median_likes_all:,.2f}")
    mode_likes_all = df['likes'].mode()[0]
    print(f"Mode likes of all time: {mode_likes_all:,.2f}")
    print(f"Range of likes: {df['likes'].max()-df['likes'].min():,.2f}")
    print(f"Variance of likes: {df['likes'].var():,.2f}")
    print(f"Standard Deviation of likes: {df['likes'].std():,.2f}")
    print(f"IQR of likes: {df['likes'].quantile(0.75)-df['likes'].quantile(0.25):,.2f}")
    print()

    mean_comments_all = df['comments'].mean()
    print(f"Mean comments of all time: {mean_comments_all:,.2f}")
    median_comments_all = df['comments'].median()
    print(f"Median comments of all time: {median_comments_all:,.2f}")
    mode_comments_all = df['comments'].mode()[0]
    print(f"Mode comments of all time: {mode_comments_all:,.2f}")
    print(f"Range of comments: {df['comments'].max()-df['comments'].min():,.2f}")
    print(f"Variance of comments: {df['comments'].var():,.2f}")
    print(f"Standard Deviation of comments: {df['comments'].std():,.2f}")
    print(f"IQR of comments: {df['comments'].quantile(0.75)-df['comments'].quantile(0.25):,.2f}")
    print()

    for category, category_df in df.groupby("category_name_gpt"):
        # groupby creates a dictionary key is where the column that dataframe is grouped and values which are grouped dataframes
        # Measures of Location and Measures of Spread

        print(f"{category} category have {len(category_df)} number of videos in it after 2022.")
        print(f"Mean views of {category} after 2022: {category_df['views'].mean():,.2f}")
        print(f"Median views of {category} after 2022: {category_df['views'].median():,.2f}")
        print(f"Mode views of {category} after 2022: {category_df['views'].mode()[0]:,.2f}")
        print(f"Range of views of {category} after 2022: {category_df['views'].max()-category_df['views'].min():,.2f}")
        print(f"Variance of views of {category} after 2022: {category_df['views'].var():,.2f}")
        print(f"Standard Deviation of views of {category} after 2022: {category_df['views'].std():,.2f}")
        print(f"IQR of views of {category} after 2022: {category_df['views'].quantile(0.75)-category_df['views'].quantile(0.25):,.2f}")
        print()

        print(f"Mean likes of {category} after 2022: {category_df['likes'].mean():,.2f}")
        print(f"Median likes of {category} after 2022: {category_df['likes'].median():,.2f}")
        print(f"Mode likes of {category} after 2022: {category_df['likes'].mode()[0]:,.2f}")
        print(f"Range of likes of {category} after 2022: {category_df['likes'].max()-category_df['likes'].min():,.2f}")
        print(f"Variance of likes of {category} after 2022: {category_df['likes'].var():,.2f}")
        print(f"Standard Deviation of likes of {category} after 2022: {category_df['likes'].std():,.2f}")
        print(f"IQR of likes of {category} after 2022: {category_df['likes'].quantile(0.75)-category_df['likes'].quantile(0.25):,.2f}")
        print()

        print(f"Mean comments of {category} after 2022: {category_df['comments'].mean():,.2f}")
        print(f"Median comments of {category} after 2022: {category_df['comments'].median():,.2f}")
        print(f"Mode comments of {category} after 2022: {category_df['comments'].mode()[0]:,.2f}")
        print(f"Range of comments of {category} after 2022: {category_df['comments'].max()-category_df['comments'].min():,.2f}")
        print(f"Variance of comments of {category} after 2022: {category_df['comments'].var():,.2f}")
        print(f"Standard Deviation of comments of {category} after 2022: {category_df['comments'].std():,.2f}")
        print(f"IQR of comments of {category} after 2022: {category_df['comments'].quantile(0.75)-category_df['comments'].quantile(0.25):,.2f}")
        print()

"""
1. **Measures of Location (Central Tendency)**
    - **Mean:** The average value, useful for understanding the general trend.
    - **Median:** The middle value when data is sorted, less affected by outliers.
    - **Mode:** The most frequently occurring value, mainly useful for categorical data.

2. **Measures of Spread (Dispersion)**
    - **Standard Deviation:** Shows how spread out the data is from the mean.
        - **A low standard deviation means the data points are close to the mean.
        - **A high standard deviation means the data points are more spread out.

    - **Variance:** The average of the squared differences from the mean.
        - **Higher variance means the data points are more spread out.

    - **Range:** The difference between the maximum and minimum values. (In this case will not tell us much since there are lots of videos.)
    - **Interquartile Range (IQR):** Measures the spread of the middle 50% of the data.
        - **The IQR focuses on the middle 50% of the data, ignoring extreme values (outliers).

3. **Measures of Shape (Distribution)**
    - **Skewness:** Indicates if the data is skewed to the left or right.
    - **Kurtosis:** Measures the "tailedness" of the distribution, indicating outliers.
      
4. **Correlation (For Relationships Between Variables)**
    - **Correlation Coefficient:** Measures how two numerical variables relate to each other. For example, do more views generally mean more likes?
    Spread 5 different categories. Then compare their view/like scale to see what users engage with most when it comes to categories.
"""