#use this code if the Groq AI's API limits exhaust. Groq AI based code is placed below
import json
import time
from fluvio import Fluvio, Offset
import socketio
from transformers import pipeline

fluvio = Fluvio.connect()
consumer = fluvio.partition_consumer("social-tweets", 0)
sio = socketio.Client()

sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

@sio.event
def disconnect():
    print("❌ Disconnected from backend")

def connect_to_backend():
    try:
        sio.connect("http://localhost:8000")
        print("✅ Connected to backend")
        time.sleep(1)
    except Exception as e:
        print("❌ Connection error:", e)
        exit(1)

connect_to_backend()

print("\n🚀 Listening for passenger feedback...\n")

def determine_satisfaction(record):
    score_fields = [
        "Seat comfort", "Departure/Arrival time convenient", "Food and drink",
        "Inflight wifi service", "Inflight entertainment", "Online support",
        "Ease of Online booking", "On-board service", "Leg room service",
        "Baggage handling", "Cleanliness", "Online boarding"
    ]

    positive_count = sum(1 for field in score_fields if int(record.get(field, 0)) >= 3)
    return "satisfied" if positive_count >= 4 else "unsatisfied"

def classify_review_sentiment(text_review):
    if not text_review.strip():
        return "neutral"
    
    try:
        result = sentiment_pipeline(text_review)[0]
        label = result["label"]
        if label == "POSITIVE":
            return "good"
        elif label == "NEGATIVE":
            return "bad"
        else:
            return "neutral"
    except Exception as e:
        print("❌ Sentiment classification failed:", e)
        return "neutral"

# Stream records from Fluvio topic
for record in consumer.stream(Offset.beginning()):
    try:
        msg = json.loads(record.value_string())
        
        text_review = msg.get("Text reviews", "")
        review_sentiment = classify_review_sentiment(text_review)

        satisfaction = determine_satisfaction(msg)

        print(f"👤 Passenger Age: {msg['Age']}, Class: {msg['Class']}, Satisfaction: {satisfaction.upper()}")
        print(f"📝 Review Text: {text_review} (Sentiment: {review_sentiment.upper()})")

        if sio.connected:
            try:
                sio.emit("tweet", {
                    "sentiment": review_sentiment,  
                    "satisfaction": "satisfied" if msg["satisfaction"] == 1 else "unsatisfied",  
                    "class": msg["Class"],
                    "gender": msg.get("Gender", 0),
                    "age": msg.get("Age", 0),
                    "type_of_travel": msg.get("Type of Travel", 0),
                    "ratings": {
                        "seat_comfort": msg.get("Seat comfort", 0),
                        "departure_time": msg.get("Departure/Arrival time convenient", 0),
                        "food_and_drink": msg.get("Food and drink", 0),
                        "inflight_wifi": msg.get("Inflight wifi service", 0),
                        "inflight_entertainment": msg.get("Inflight entertainment", 0),
                        "online_support": msg.get("Online support", 0),
                        "online_booking": msg.get("Ease of Online booking", 0),
                        "onboard_service": msg.get("On-board service", 0),
                        "leg_room": msg.get("Leg room service", 0),
                        "baggage_handling": msg.get("Baggage handling", 0),
                        "cleanliness": msg.get("Cleanliness", 0),
                        "online_boarding": msg.get("Online boarding", 0)
                    },
                    "text_review": text_review,
                    "Review_created": msg.get("Review_created", "Unknown")
                })
    
                print("✅ Emit successful")
            except Exception as emit_error:
                print("❌ Emit failed:", emit_error)
        else:
            print("⚠️ Socket not connected. Retrying connection...")
            connect_to_backend()

        time.sleep(2)  

    except Exception as e:
        print("❌ Error processing record:", e)






# import json
# import time
# from fluvio import Fluvio, Offset
# import socketio
# import requests

# # GROQ API Configuration
# GROQ_API_KEY = "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"
# GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# headers = {
#     "Authorization": f"Bearer {GROQ_API_KEY}",
#     "Content-Type": "application/json"
# }

# # Initialize Fluvio and Socket.IO
# fluvio = Fluvio.connect()
# consumer = fluvio.partition_consumer("social-tweets", 0)
# sio = socketio.Client()

# @sio.event
# def disconnect():
#     print("❌ Disconnected from backend")

# def connect_to_backend():
#     try:
#         sio.connect("http://localhost:8000")
#         print("✅ Connected to backend")
#         time.sleep(1)
#     except Exception as e:
#         print("❌ Connection error:", e)
#         exit(1)

# connect_to_backend()

# print("\n🚀 Listening for passenger feedback...\n")

# def determine_satisfaction(record):
#     score_fields = [
#         "Seat comfort", "Departure/Arrival time convenient", "Food and drink",
#         "Inflight wifi service", "Inflight entertainment", "Online support",
#         "Ease of Online booking", "On-board service", "Leg room service",
#         "Baggage handling", "Cleanliness", "Online boarding"
#     ]
#     positive_count = sum(1 for field in score_fields if int(record.get(field, 0)) >= 3)
#     return "satisfied" if positive_count >= 4 else "unsatisfied"

# def classify_review_sentiment(text_review):
#     if not text_review.strip():
#         return "neutral"

#     prompt = f"Classify the sentiment of this passenger review as good, bad, or neutral:\n\n\"{text_review}\""

#     data = {
#         "model": "mixtral-8x7b-32768",
#         "messages": [
#             {"role": "system", "content": "You are a sentiment analysis assistant."},
#             {"role": "user", "content": prompt}
#         ],
#         "temperature": 0.3
#     }

#     try:
#         response = requests.post(GROQ_API_URL, headers=headers, json=data)
#         response.raise_for_status()
#         reply = response.json()["choices"][0]["message"]["content"].strip().lower()

#         if "good" in reply:
#             return "good"
#         elif "bad" in reply:
#             return "bad"
#         else:
#             return "neutral"
#     except Exception as e:
#         print("❌ GROQ Sentiment classification failed:", e)
#         return "neutral"

# # Stream records from Fluvio topic
# for record in consumer.stream(Offset.beginning()):
#     try:
#         msg = json.loads(record.value_string())

#         text_review = msg.get("Text reviews", "")
#         review_sentiment = classify_review_sentiment(text_review)
#         satisfaction = determine_satisfaction(msg)

#         print(f"👤 Passenger Age: {msg['Age']}, Class: {msg['Class']}, Satisfaction: {satisfaction.upper()}")
#         print(f"📝 Review Text: {text_review} (Sentiment: {review_sentiment.upper()})")

#         if sio.connected:
#             try:
#                 sio.emit("tweet", {
#                     "sentiment": review_sentiment,
#                     "satisfaction": "satisfied" if msg["satisfaction"] == 1 else "unsatisfied",
#                     "class": msg["Class"],
#                     "gender": msg.get("Gender", 0),
#                     "age": msg.get("Age", 0),
#                     "type_of_travel": msg.get("Type of Travel", 0),
#                     "ratings": {
#                         "seat_comfort": msg.get("Seat comfort", 0),
#                         "departure_time": msg.get("Departure/Arrival time convenient", 0),
#                         "food_and_drink": msg.get("Food and drink", 0),
#                         "inflight_wifi": msg.get("Inflight wifi service", 0),
#                         "inflight_entertainment": msg.get("Inflight entertainment", 0),
#                         "online_support": msg.get("Online support", 0),
#                         "online_booking": msg.get("Ease of Online booking", 0),
#                         "onboard_service": msg.get("On-board service", 0),
#                         "leg_room": msg.get("Leg room service", 0),
#                         "baggage_handling": msg.get("Baggage handling", 0),
#                         "cleanliness": msg.get("Cleanliness", 0),
#                         "online_boarding": msg.get("Online boarding", 0)
#                     },
#                     "text_review": text_review,
#                     "Review_created": msg.get("Review_created", "Unknown")
#                 })

#                 print("✅ Emit successful")
#             except Exception as emit_error:
#                 print("❌ Emit failed:", emit_error)
#         else:
#             print("⚠️ Socket not connected. Retrying connection...")
#             connect_to_backend()

#         time.sleep(2)

#     except Exception as e:
#         print("❌ Error processing record:", e)
