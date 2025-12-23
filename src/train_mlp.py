from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os
from src.config import MODEL_PATH, RANDOM_SEED

def train_mlp(X_train, X_test, y_train, y_test):
    """
    Train and evaluate MLP Classifier.
    """
    print("Training MLP Classifier...")
    model = MLPClassifier(random_state=RANDOM_SEED, max_iter=300)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    print("MLP Classifier Results:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print(classification_report(y_test, y_pred))
    
    # Save model
    os.makedirs(MODEL_PATH, exist_ok=True)
    joblib.dump(model, os.path.join(MODEL_PATH, "mlp_classifier.pkl"))
    print(f"Model saved to {os.path.join(MODEL_PATH, 'mlp_classifier.pkl')}")
    
    return model
