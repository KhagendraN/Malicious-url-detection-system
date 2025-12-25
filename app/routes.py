from flask import Blueprint, render_template, request, jsonify
import os
from src.predict import predict_url
from src.config import MODEL_PATH

main = Blueprint('main', __name__)

from src.hf_utils import list_hf_models

MODEL_EFFICIENCIES = {
    'adaboost': '85%',
    'decision tree': '96%',
    'extra trees classifier': '97%',
    'gaussian naive bayes': '80%',
    'gradient boosting classifier': '94%',
    'logistic regression': '87%',
    'mlp classifier': '96%',
    'random forest': '97%',
    'sgd classifier': '87%',
    'xgboost': '96%'
}

@main.route('/')
def index():
    # Get list of available models from local storage
    local_models = {f.replace('.pkl', '').replace('_', ' ').title() 
                    for f in os.listdir(MODEL_PATH) 
                    if f.endswith('.pkl') and f not in ['scaler.pkl', 'label_encoder.pkl']}
    
    # Get list of available models from Hugging Face
    hf_models = {f.replace('.pkl', '').replace('_', ' ').title() 
                 for f in list_hf_models()}
    
    # Combine and sort
    model_names = list(local_models.union(hf_models))
    model_names.sort()
    
    # Create list of dicts for template
    models = []
    for name in model_names:
        models.append({
            'name': name,
            'accuracy': MODEL_EFFICIENCIES.get(name.lower(), 'N/A')
        })
    
    return render_template('index.html', models=models)

@main.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data.get('url')
    model_name = data.get('model')
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    if not model_name:
        model_name = "Xgboost" # Default
        
    try:
        # Convert model name back to filename format if needed, 
        # but predict_url handles "Xgboost" -> "xgboost.pkl" logic mostly.
        # However, predict_url expects "xgboost" or "random_forest" etc.
        # The UI sends "Xgboost", "Random Forest".
        # We need to normalize it.
        normalized_model_name = model_name.lower().replace(' ', '_')
        
        prediction = predict_url(url, model_name=normalized_model_name)
        return jsonify({'prediction': prediction, 'url': url, 'model': model_name})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
