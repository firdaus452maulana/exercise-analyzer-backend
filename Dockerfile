# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install flask firebase-admin python-dotenv

# Copy all Python files
COPY *.py ./

EXPOSE 4025

# Run the application
CMD ["python", "main.py"]