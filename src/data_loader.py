import pandas as pd
import os

def load_data(path):
    """
    Load data from a CSV file.
    
    Args:
        path (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Loaded dataframe.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"The file {path} does not exist.")
    return pd.read_csv(path)
