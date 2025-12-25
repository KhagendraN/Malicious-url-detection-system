FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy only requirements first for Docker layer caching
COPY requirements.txt .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set Python to unbuffered mode 
ENV PYTHONUNBUFFERED=1

# Run the app with Gunicorn, listening on the port Render provides
CMD gunicorn run:app --bind 0.0.0.0:$PORT
