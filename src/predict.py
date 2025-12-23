import joblib
import os
import pandas as pd
import numpy as np
from .config import MODEL_PATH
from .feature_engineering import extract_features

def load_artifacts():
    """Load scaler, label encoder, and models."""
    scaler_path = os.path.join(MODEL_PATH, "scaler.pkl")
    le_path = os.path.join(MODEL_PATH, "label_encoder.pkl")
    
    if not os.path.exists(scaler_path) or not os.path.exists(le_path):
        raise FileNotFoundError("Scaler or Label Encoder not found. Run main.py first.")
        
    scaler = joblib.load(scaler_path)
    le = joblib.load(le_path)
    
    return scaler, le

def load_model(model_name="xgboost"):
    """Load a specific model."""
    filename = model_name.lower().replace(" ", "_") + ".pkl"
    model_path = os.path.join(MODEL_PATH, filename)
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model {model_name} not found at {model_path}")
        
    return joblib.load(model_path)

def predict_url(url, model_name="xgboost"):
    """
    Predict the type of a URL.
    
    Args:
        url (str): The URL to predict.
        model_name (str): The name of the model to use.
        
    Returns:
        str: Predicted class (Benign, Defacement, Phishing, Malware).
    """
    # Load artifacts
    scaler, le = load_artifacts()
    model = load_model(model_name)
    
    # Create DataFrame for feature extraction
    df = pd.DataFrame([{'url': url}])
    
    # Extract features
    # Note: extract_features expects a dataframe and returns a dataframe with features
    # We need to suppress prints if possible, or just accept them
    df_features = extract_features(df)
    
    # Drop 'url' column as in preprocessing
    X = df_features.drop(['url'], axis=1)
    
    # Scale features
    X_scaled = scaler.transform(X)
    
    # Predict
    prediction_idx = model.predict(X_scaled)[0]
    prediction_label = le.inverse_transform([prediction_idx])[0]
    
    return prediction_label

if __name__ == "__main__":
    # Example usage
    test_url = "http://google.com"
    print(f"Predicting for {test_url}...")
    result = predict_url(test_url, model_name="mlp_classifier")
    print(f"Prediction: {result}")
    
    test_url_2 = "http://malicious-site.com/login.php"
    print(f"Predicting for {test_url_2}...")
    result = predict_url(test_url_2)
    print(f"Prediction: {result}")
