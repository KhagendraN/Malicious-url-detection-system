# Malicious Detection System

This project is designed to detect malicious URLs using machine learning models. It features two different classification models, Logistic Regression and MLP (Multilayer Perceptron) Classifier, trained to identify whether a URL is safe or malicious.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Training the Models](#training-the-models)
- [Flask Web Application](#flask-web-application)
- [Evaluation and Reports](#evaluation-and-reports)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Introduction

The **Malicious Detection System** uses machine learning to classify URLs into "malicious" or "safe" categories. This is a critical task in cybersecurity to protect users from phishing and other malicious online threats.

The system includes:
- **Two Machine Learning Models:** Logistic Regression and MLP Classifier.
- **Data Preprocessing and Feature Engineering:** Includes TF-IDF vectorization for URL feature extraction.
- **Flask Web Application:** A simple user interface for testing URLs in real-time.
- **Model Evaluation:** Detailed reports comparing model performance.

This project is a great starting point for anyone interested in machine learning applications in cybersecurity.

## Project Structure

The project follows a clean and scalable structure:

````
malicious-detection-system/
│
├── data/                     # Datasets (raw and processed)
│   ├── raw/                  # Original data
│   ├── processed/            # Processed and serialized data
│
├── models/                   # Trained machine learning models
│   ├── logistic_model.pkl    # Logistic Regression model
│   ├── mlp_model.pkl         # MLP Classifier model
│   └── vectorizer.pkl        # TF-IDF Vectorizer
│
├── notebooks/                # Jupyter Notebooks for exploratory data analysis
│   └── eda.ipynb             # Exploratory Data Analysis notebook
│
├── src/                      # Core ML and utility logic
│   ├── **init**.py
│   ├── config.py             # Configuration settings
│   ├── data_loader.py        # Data loading and preparation
│   ├── preprocessing.py      # Data preprocessing (train-test split)
│   ├── feature_engineering.py # Feature engineering (TF-IDF vectorization)
│   ├── train_logistic.py     # Logistic Regression training script
│   ├── train_mlp.py          # MLP Classifier training script
│   ├── evaluate.py           # Model evaluation and reporting
│   └── predict.py            # URL prediction for Flask app
│
├── app/                      # Flask web application
│   ├── **init**.py
│   ├── app.py                # Main Flask app file
│   ├── templates/            # HTML templates
│   │   └── index.html        # Main UI template
│   └── static/               # Static assets (CSS, JS)
│       └── style.css         # Stylesheet
│
├── reports/                  # Model evaluation reports
│   ├── logistic_report.txt   # Logistic Regression evaluation report
│   └── mlp_report.txt        # MLP Classifier evaluation report
│
├── main.py                   # Main script for training both models
├── requirements.txt          # Python dependencies
└── README.md                 # Project overview and documentation
````

## Requirements

To run this project, you need the following libraries:
- Flask
- scikit-learn
- pandas
- numpy
- joblib
- matplotlib (optional, for visualization)
- seaborn (optional, for visualization)

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
````

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/malicious-detection-system.git
   cd malicious-detection-system
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the system, run the Flask web application with:

```bash
python app/app.py
```

Visit `http://127.0.0.1:5000/` in your web browser to test URLs using the two classification models: Logistic Regression or MLP Classifier.

### Example of Using the Web Application

1. Enter a URL in the input field (e.g., `http://example.com`).
2. Select the model you want to use: Logistic Regression or MLP Classifier.
3. Click **Detect** to see if the URL is **Malicious** or **Safe**.

## Training the Models

To train both models, run the `main.py` script:

```bash
python main.py
```

This will:

1. Load the raw dataset (`malicious_urls.csv`).
2. Preprocess the data (splitting and vectorizing).
3. Train both the Logistic Regression and MLP Classifier models.
4. Save the trained models and vectorizer for future predictions.

## Flask Web Application

The **Flask Web Application** provides an interface where you can input URLs and use the trained models to classify them as **Malicious** or **Safe**.

* **app.py**: Main Flask application file that routes requests to the appropriate functions.
* **index.html**: Simple HTML form to input URLs and select a model.
* **style.css**: Basic styles for the web interface.

## Evaluation and Reports

After training the models, evaluation is done using **classification reports**. These reports summarize key metrics like precision, recall, and F1-score for both models.

* **logistic_report.txt**: Evaluation report for Logistic Regression.
* **mlp_report.txt**: Evaluation report for MLP Classifier.

## Future Enhancements

Here are some possible enhancements for the project:

* **Model Comparison Visualization**: Add graphs to compare the performance of Logistic Regression and MLP models.
* **Confidence Scores**: Display the confidence score (probability) for each prediction.
* **Dockerization**: Dockerize the entire project for easier deployment.
* **API Deployment**: Expose the model as an API for use in other applications.
* **Cloud Deployment**: Deploy the system on platforms like AWS or Heroku.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

