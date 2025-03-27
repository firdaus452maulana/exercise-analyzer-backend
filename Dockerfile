# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask flask_restful firebase-admin python-dotenv openai

EXPOSE 4025

# Run the application
CMD ["python", "main.py", "--port", "4025"]