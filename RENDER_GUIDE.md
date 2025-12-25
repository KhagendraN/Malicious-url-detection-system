# Deploying to Render

This guide explains how to deploy the Malicious URL Detection System to Render.

## Prerequisites
- A [Render](https://render.com/) account.
- A GitHub repository containing this project code.

## Option 1: Deploy using `render.yaml` (Blueprints)

1.  Push your code to a GitHub repository.
2.  Go to the [Render Dashboard](https://dashboard.render.com/).
3.  Click **New +** and select **Blueprint**.
4.  Connect your GitHub account and select the repository.
5.  Render will automatically detect the `render.yaml` file.
6.  Click **Apply** to start the deployment.

## Option 2: Manual Deployment (Docker)

1.  Push your code to a GitHub repository.
2.  Go to the [Render Dashboard](https://dashboard.render.com/).
3.  Click **New +** and select **Web Service**.
4.  Connect your GitHub repository.
5.  Select **Docker** as the Runtime.
6.  Click **Create Web Service**.

## Option 3: Manual Deployment (Python Native)

If you prefer not to use Docker:
1.  Select **Python 3** as the Runtime.
2.  Set the **Build Command** to:
    ```bash
    pip install -r requirements.txt
    ```
3.  Set the **Start Command** to:
    ```bash
    gunicorn run:app
    ```

## Post-Deployment
- Render will provide a URL (e.g., `https://malicious-url-detector.onrender.com`).
- Visit the URL to access the UI.
