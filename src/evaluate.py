import joblib
import os
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from config import RAW_DATA_PATH, MODEL_PATH, REPORT_PATH
from data_loader import load_data
from feature_engineering import extract_features
from preprocessing import preprocess_data

def evaluate_models():
    # 1. Load and Preprocess Data (to get X_test and y_test)
    print("Loading and preprocessing data for evaluation...")
    try:
        df = load_data(RAW_DATA_PATH)
    except FileNotFoundError as e:
        print(e)
        return

    df = extract_features(df)
    _, X_test, _, y_test, le, _ = preprocess_data(df)
    
    # 2. Load Models
    model_files = [f for f in os.listdir(MODEL_PATH) if f.endswith('.pkl') and f not in ['scaler.pkl', 'label_encoder.pkl']]
    
    results = {}
    
    for model_file in model_files:
        model_name = model_file.replace('.pkl', '').replace('_', ' ').title()
        print(f"\nEvaluating {model_name}...")
        
        model_path = os.path.join(MODEL_PATH, model_file)
        model = joblib.load(model_path)
        
        y_pred = model.predict(X_test)
        
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, target_names=le.classes_)

        # saving accuracy and report to reports folder
        os.makedirs(REPORT_PATH, exist_ok=True)
        with open(os.path.join(REPORT_PATH, f"{model_name}_report.txt"), 'w') as f:
            f.write(accuracy)
            f.write(report)
        
        print(f"Accuracy: {accuracy}")
        print("Classification Report:")
        print(report)
        
        results[model_name] = {
            'accuracy': accuracy,
            'report': report,
            'confusion_matrix': confusion_matrix(y_test, y_pred)
        }
        
    return results

if __name__ == "__main__":
    evaluate_models()
