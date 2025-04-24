# Use an official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirement list and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your script
COPY . .

# Run the consumer script
CMD ["python", "tweet_sentiment_consumer.py"]
