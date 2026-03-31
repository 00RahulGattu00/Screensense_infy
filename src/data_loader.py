"""
Data Loader Module

This module contains functions for loading data from various sources.
"""

import pandas as pd
import os


def load_raw_data(file_path):
    """
    Load raw data from a file.
    
    Args:
        file_path (str): Path to the data file
        
    Returns:
        pd.DataFrame: Loaded data
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found: {file_path}")
    
    # Determine file type and load accordingly
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.json'):
        return pd.read_json(file_path)
    elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        return pd.read_excel(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")


def save_processed_data(data, file_path):
    """
    Save processed data to a file.
    
    Args:
        data (pd.DataFrame): Data to save
        file_path (str): Output file path
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    data.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")
