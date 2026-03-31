"""
Preprocessing Module

This module contains functions for data preprocessing and cleaning.
"""

import pandas as pd
import numpy as np


def preprocess_data(data):
    """
    Perform basic preprocessing on the dataset.
    
    Args:
        data (pd.DataFrame): Raw data
        
    Returns:
        pd.DataFrame: Preprocessed data
    """
    # Make a copy to avoid modifying original data
    df = data.copy()
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    df = handle_missing_values(df)
    
    return df


def handle_missing_values(data):
    """
    Handle missing values in the dataset.
    
    Args:
        data (pd.DataFrame): Data with potential missing values
        
    Returns:
        pd.DataFrame: Data with handled missing values
    """
    df = data.copy()
    
    # Fill numeric columns with median
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    
    # Fill categorical columns with mode
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else 'Unknown')
    
    return df


def normalize_data(data, columns=None):
    """
    Normalize numerical columns in the dataset.
    
    Args:
        data (pd.DataFrame): Data to normalize
        columns (list): List of columns to normalize. If None, normalize all numeric columns.
        
    Returns:
        pd.DataFrame: Normalized data
    """
    df = data.copy()
    
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns
    
    for col in columns:
        if col in df.columns:
            df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    
    return df
