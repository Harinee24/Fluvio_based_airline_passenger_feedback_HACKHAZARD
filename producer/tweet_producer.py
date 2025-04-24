import csv
import time
import json
import random
from fluvio import Fluvio
from sklearn.model_selection import train_test_split

fluvio = Fluvio.connect()
topic = "social-tweets"

# Load data with error handling for encoding issues
try:
    with open("../dataset/airline-review.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = []

        for row in reader:
            if row.get("satisfaction"):
                rows.append(row)

        random.shuffle(rows)
        train_data, test_data = train_test_split(rows, test_size=0.2, random_state=42)

        for row in train_data:
            message = {
                "Gender": int(row["Gender"]),
                "Age": int(row["Age"]),
                "Type of Travel": int(row["Type of Travel"]),
                "Class": row["Class"],
                "Seat comfort": int(row["Seat comfort"]),
                "Departure/Arrival time convenient": int(row["Departure/Arrival time convenient"]),
                "Food and drink": int(row["Food and drink"]),
                "Inflight wifi service": int(row["Inflight wifi service"]),
                "Inflight entertainment": int(row["Inflight entertainment"]),
                "Online support": int(row["Online support"]),
                "Ease of Online booking": int(row["Ease of Online booking"]),
                "On-board service": int(row["On-board service"]),
                "Leg room service": int(row["Leg room service"]),
                "Baggage handling": int(row["Baggage handling"]),
                "Cleanliness": int(row["Cleanliness"]),
                "Online boarding": int(row["Online boarding"]),
                "satisfaction": int(row["satisfaction"]),
                "Text reviews": row["Text reviews"],
                "Review_created": row["Review_created"]
            }
            print(f"Review created field: {row['Review_created']}")

            fluvio.topic_producer(topic).send(b"", json.dumps(message).encode("utf-8"))
            print("Sent:", message)
            time.sleep(2)

except UnicodeDecodeError as e:
    print(f"UnicodeDecodeError encountered: {e}")
    print("Trying with 'latin1' encoding...")

    with open("../dataset/airline-review.csv", "r", encoding="latin1") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = []

        for row in reader:
            if row.get("satisfaction"):
                rows.append(row)

        random.shuffle(rows)
        train_data, test_data = train_test_split(rows, test_size=0.2, random_state=42)

        for row in train_data:
            message = {
                "Gender": int(row["Gender"]),
                "Age": int(row["Age"]),
                "Type of Travel": int(row["Type of Travel"]),
                "Class": row["Class"],
                "Seat comfort": int(row["Seat comfort"]),
                "Departure/Arrival time convenient": int(row["Departure/Arrival time convenient"]),
                "Food and drink": int(row["Food and drink"]),
                "Inflight wifi service": int(row["Inflight wifi service"]),
                "Inflight entertainment": int(row["Inflight entertainment"]),
                "Online support": int(row["Online support"]),
                "Ease of Online booking": int(row["Ease of Online booking"]),
                "On-board service": int(row["On-board service"]),
                "Leg room service": int(row["Leg room service"]),
                "Baggage handling": int(row["Baggage handling"]),
                "Cleanliness": int(row["Cleanliness"]),
                "Online boarding": int(row["Online boarding"]),
                "satisfaction": int(row["satisfaction"]),
                "Text reviews": row["Text reviews"],
                "Review_created": row["Review_created"]
            }

            fluvio.topic_producer(topic).send(b"", json.dumps(message).encode("utf-8"))
            print("Sent:", message)
            time.sleep(2)
