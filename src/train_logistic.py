from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os
from src.config import MODEL_PATH, RANDOM_SEED

def train_logistic_regression(X_train, X_test, y_train, y_test):
    """
    Train and evaluate Logistic Regression model.
    """
    print("Training Logistic Regression...")
    model = LogisticRegression(random_state=RANDOM_SEED, max_iter=1000)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    print("Logistic Regression Results:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print(classification_report(y_test, y_pred))
    
    # Save model
    os.makedirs(MODEL_PATH, exist_ok=True)
    joblib.dump(model, os.path.join(MODEL_PATH, "logistic_regression.pkl"))
    print(f"Model saved to {os.path.join(MODEL_PATH, 'logistic_regression.pkl')}")
    
    return model
