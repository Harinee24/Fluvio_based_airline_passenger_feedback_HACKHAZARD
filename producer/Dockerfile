# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files into the container
COPY producer/tweet_producer.py ./
COPY dataset/airline-review.csv ./dataset/airline-review.csv  
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the producer
CMD ["python", "tweet_producer.py"]
