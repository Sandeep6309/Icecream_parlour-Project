# Base Python image
FROM python:3.8-slim

# Install system dependencies required for tkinter
RUN apt-get update && \
    apt-get install -y python3-tk && \
    rm -rf /var/lib/apt/lists/*

# Set working directory in the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the application
CMD ["python", "main.py"]
