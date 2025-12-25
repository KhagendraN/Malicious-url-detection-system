import os
from huggingface_hub import hf_hub_download, list_repo_files
from .config import MODEL_PATH

REPO_ID = "khagu/malicious-url-detection-models"

def download_file(filename):
    """
    Download a file from the Hugging Face repo to the local models directory.
    
    Args:
        filename (str): Name of the file to download.
        
    Returns:
        str: Path to the downloaded file.
    """
    print(f"Downloading {filename} from Hugging Face...")
    try:
        file_path = hf_hub_download(
            repo_id=REPO_ID,
            filename=filename,
            local_dir=MODEL_PATH,
            local_dir_use_symlinks=False
        )
        print(f"Successfully downloaded {filename} to {file_path}")
        return file_path
    except Exception as e:
        print(f"Error downloading {filename}: {e}")
        raise e

def list_hf_models():
    """
    List available .pkl model files in the Hugging Face repo.
    
    Returns:
        list: List of model filenames.
    """
    try:
        files = list_repo_files(repo_id=REPO_ID)
        models = [f for f in files if f.endswith('.pkl') and f not in ['scaler.pkl', 'label_encoder.pkl']]
        return models
    except Exception as e:
        print(f"Error listing files from Hugging Face: {e}")
        return []
