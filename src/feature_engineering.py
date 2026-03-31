"""
Feature Engineering Module

This module contains functions for creating new features from existing data.
"""

import pandas as pd
import numpy as np


def create_age_bands(data, age_column='age'):
    """
    Create age bands from age values.
    
    Age bands:
    - 3-5: Preschool
    - 6-9: Early childhood
    - 10-13: Pre-teen
    - 14-17: Teen
    
    Args:
        data (pd.DataFrame): Data containing age column
        age_column (str): Name of the age column
        
    Returns:
        pd.DataFrame: Data with new 'age_band' column
    """
    df = data.copy()
    
    # Define age band bins and labels
    bins = [0, 5, 9, 13, 17, 100]
    labels = ['3-5', '6-9', '10-13', '14-17', '18+']
    
    df['age_band'] = pd.cut(df[age_column], bins=bins, labels=labels, right=True)
    
    return df


def create_weekday_weekend_flag(data, date_column='date'):
    """
    Create a flag indicating whether a date is a weekday or weekend.
    
    Logic:
    - Weekday: Monday-Friday (0-4)
    - Weekend: Saturday-Sunday (5-6)
    
    Args:
        data (pd.DataFrame): Data containing date column
        date_column (str): Name of the date column
        
    Returns:
        pd.DataFrame: Data with new 'day_type' column
    """
    df = data.copy()
    
    # Ensure date column is datetime
    if not pd.api.types.is_datetime64_any_dtype(df[date_column]):
        df[date_column] = pd.to_datetime(df[date_column])
    
    # Get day of week (0=Monday, 6=Sunday)
    df['day_of_week'] = df[date_column].dt.dayofweek
    
    # Create weekday/weekend flag
    df['day_type'] = df['day_of_week'].apply(
        lambda x: 'Weekday' if x < 5 else 'Weekend'
    )
    
    return df


def create_screentime_buckets(data, screentime_column='screentime_minutes', 
                              low_threshold=120, high_threshold=240):
    """
    Create screentime buckets based on usage patterns.
    
    Logic:
    - Low: < 120 minutes (2 hours)
    - Medium: 120-240 minutes (2-4 hours)
    - High: > 240 minutes (4+ hours)
    
    Note: Thresholds can be adjusted based on domain knowledge
    
    Args:
        data (pd.DataFrame): Data containing screentime column
        screentime_column (str): Name of the screentime column
        low_threshold (int): Upper bound for 'Low' category (minutes)
        high_threshold (int): Lower bound for 'High' category (minutes)
        
    Returns:
        pd.DataFrame: Data with new 'screentime_bucket' column
    """
    df = data.copy()
    
    def categorize_screentime(minutes):
        if minutes < low_threshold:
            return 'Low'
        elif minutes < high_threshold:
            return 'Medium'
        else:
            return 'High'
    
    df['screentime_bucket'] = df[screentime_column].apply(categorize_screentime)
    
    return df


def apply_all_features(data, age_column='age', date_column='date', 
                      screentime_column='screentime_minutes',
                      include_optional=True):
    """
    Apply all feature engineering transformations.
    
    Args:
        data (pd.DataFrame): Raw data
        age_column (str): Name of the age column
        date_column (str): Name of the date column
        screentime_column (str): Name of the screentime column
        include_optional (bool): Whether to include optional features
        
    Returns:
        pd.DataFrame: Data with all engineered features
    """
    df = data.copy()
    
    # Apply required features
    if age_column in df.columns:
        df = create_age_bands(df, age_column)
    
    if date_column in df.columns:
        df = create_weekday_weekend_flag(df, date_column)
    
    # Apply optional features
    if include_optional and screentime_column in df.columns:
        df = create_screentime_buckets(df, screentime_column)
    
    return df
