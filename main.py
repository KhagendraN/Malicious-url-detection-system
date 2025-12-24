from src.config import RAW_DATA_PATH
from src.data_loader import load_data
from src.feature_engineering import extract_features
from src.preprocessing import preprocess_data
from src.train_all_models import train_all_models
import joblib
import os
from src.config import MODEL_PATH

def main():
    # 1. Load Data
    print("Loading data...")
    try:
        df = load_data(RAW_DATA_PATH)
    except FileNotFoundError as e:
        print(e)
        return

    # 2. Feature Engineering
    print("Extracting features...")
    df = extract_features(df)
    
    # 3. Preprocessing
    print("Preprocessing data...")
    X_train, X_test, y_train, y_test, le, scaler = preprocess_data(df)
    
    # Save scaler and label encoder
    os.makedirs(MODEL_PATH, exist_ok=True)
    joblib.dump(scaler, os.path.join(MODEL_PATH, "scaler.pkl"))
    joblib.dump(le, os.path.join(MODEL_PATH, "label_encoder.pkl"))
    print("Scaler and Label Encoder saved.")
    
    # 4. Train Models
    train_all_models(X_train, X_test, y_train, y_test)

if __name__ == "__main__":
    main()
