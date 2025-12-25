# Malicious URL Detection System

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-FF6F00?logo=xgboost&logoColor=white)](https://xgboost.readthedocs.io/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Live Demo](https://img.shields.io/badge/Live_Demo-Visit-blue?logo=render&logoColor=white)](https://malicious-url-detection-system.onrender.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


A comprehensive machine learning-based system for detecting malicious URLs (Phishing, Defacement, Malware) with a premium Flask-based web interface.

## 🚀 Features

- **Multi-Model Support**: Utilizes various ML algorithms including XGBoost, Random Forest, Decision Trees, and more.
- **Advanced Feature Engineering**: Extracts lexical and host-based features from URLs.
- **Premium Web UI**: A modern, responsive, and interactive web interface built with Flask.
- **Real-time Prediction**: Instant analysis of URLs.
- **Deployment Ready**: Dockerized and configured for easy deployment on Render.

## 🛠️ Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/KhagendraN/Malicious-url-detection-system.git
    cd Malicious-url-detection-system
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Usage

### Web Interface (Recommended)

1.  **Run the Flask application:**
    ```bash
    python run.py
    # OR for production-like environment
    gunicorn --bind 0.0.0.0:5000 run:app
    ```

2.  **Access the UI:**
    Open your browser and navigate to `http://127.0.0.1:5000`.

3.  **Analyze a URL:**
    - Enter a URL in the input field.
    - Select a model (optional, defaults to XGBoost).
    - Click "Analyze URL".

### Model Training

To retrain the models with new data:

1.  Place your raw data in `data/raw/`.
2.  Run the main pipeline:
    ```bash
    python main.py
    ```
    This will load data, extract features, preprocess, train all models, and save artifacts to `models/`.


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 👾 Models
Find trained models at [hugging face](https://huggingface.co/khagu/malicious-url-detection-models)

## ⚖️ License

This project is licensed under the MIT License — see the [LICENSE](https://github.com/KhagendraN/Malicious-url-detection-system/blob/main/LICENSE) file for details.

