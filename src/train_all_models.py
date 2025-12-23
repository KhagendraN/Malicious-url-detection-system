from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, ExtraTreesClassifier, GradientBoostingClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os
from src.config import MODEL_PATH, RANDOM_SEED

def train_and_evaluate(model, model_name, X_train, X_test, y_train, y_test):
    """
    Train, evaluate and save a model.
    """
    print(f"\nTraining {model_name}...")
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    print(f"{model_name} Results:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print(classification_report(y_test, y_pred))
    
    # Save model
    os.makedirs(MODEL_PATH, exist_ok=True)
    filename = model_name.lower().replace(" ", "_") + ".pkl"
    joblib.dump(model, os.path.join(MODEL_PATH, filename))
    print(f"Model saved to {os.path.join(MODEL_PATH, filename)}")
    
    return model

def train_all_models(X_train, X_test, y_train, y_test):
    """
    Train all requested models.
    """
    models = [
        (DecisionTreeClassifier(random_state=RANDOM_SEED), "Decision Tree"),
        (RandomForestClassifier(random_state=RANDOM_SEED), "Random Forest"),
        (AdaBoostClassifier(random_state=RANDOM_SEED), "AdaBoost"),
        (SGDClassifier(random_state=RANDOM_SEED), "SGD Classifier"),
        (ExtraTreesClassifier(random_state=RANDOM_SEED), "Extra Trees Classifier"),
        (GaussianNB(), "Gaussian Naive Bayes"),
        (GradientBoostingClassifier(random_state=RANDOM_SEED), "Gradient Boosting Classifier"),
        (XGBClassifier(random_state=RANDOM_SEED, eval_metric='mlogloss'), "XGBoost")
    ]
    
    trained_models = {}
    for model, name in models:
        trained_models[name] = train_and_evaluate(model, name, X_train, X_test, y_train, y_test)
        
    return trained_models
