![github-submission-banner](https://github.com/user-attachments/assets/a1493b84-e4e2-456e-a791-ce35ee2bcf2f)

# 🚀 Real-Time Airline Passenger Review Analysis

> Real-Time Sentiment & Satisfaction Classification for Airlines using Fluvio, FastAPI, Hugging Face, and Socket.IO

---

## 📌 Problem Statement

**Problem Statement 3 – Real-Time Data Experiences with Fluvio,
Stream, process, and act on real-time data using Fluvio**

---

## 🎯 Objective

This project addresses the challenge of analyzing passenger feedback in real time. Airlines receive massive volumes of textual reviews that are often delayed in their analysis. This lag can prevent immediate insights into customer dissatisfaction and operational bottlenecks.

Our solution helps airlines process, analyze, and visualize customer sentiment in real-time—transforming raw feedback into actionable insights, ultimately enhancing customer satisfaction and service quality.

---

## 🧠 Team & Approach

### Team Name:  
Harinee S ( solo hacker )

### Team Members:  
- Harinee   

### Your Approach:  
- Chose this problem for its real-world impact in customer experience and aviation efficiency  
- Integrated live streaming (Fluvio) with real-time ML inference (DistilBERT)  
- Tackled streaming bottlenecks, model performance, and frontend updates using Socket.IO and FastAPI  
- Iterated on model optimization and deployment strategy for minimal latency and maximum accuracy  

---

## 🛠️ Tech Stack

### Core Technologies Used:
- **Frontend**: HTML, CSS, Chart.js  
- **Backend**: FastAPI, Socket.IO  
- **Database**: N/A (real-time, stateless pipeline)  
- **APIs**: Hugging Face Transformers  
- **Hosting**: Localhost / Deployable to any cloud platform

### Sponsor Technologies Used:

- ✅ **Fluvio:** Used for real-time data streaming from topic to processor
- ✅ **Groq:** Ideal for deploying low-latency DistilBERT inference  

---

## ✨ Key Features

- ✅ Real-time sentiment classification using DistilBERT  
- ✅ Real-time streaming using Fluvio topics  
- ✅ Live updates via Socket.IO  
- ✅ Responsive dashboard visualization with charts  

---

## 📽️ Demo & Deliverables

- **Demo Video Link:** [https://youtu.be/example](https://youtu.be/example)  
- **Pitch Deck / PPT Link:** [[https://docs.google.com/presentation/example](https://docs.google.com/presentation/d/1yAQOjSVe9mibKpAJrZ8Zfoxy8kJDY_jD/edit?usp=drivesdk&ouid=108231119769281152341&rtpof=true&sd=true)]([https://docs.google.com/presentation/example](https://docs.google.com/presentation/d/1yAQOjSVe9mibKpAJrZ8Zfoxy8kJDY_jD/edit?usp=drivesdk&ouid=108231119769281152341&rtpof=true&sd=true))

---

## ✅ Tasks & Bonus Checklist

- ✅ **All members completed the mandatory task**  
- ✅ **Bonus Task 1 - Badges shared**  
- ✅ **Bonus Task 2 - Sprint.dev signup completed**

---

## 🧪 How to Run the Project

### Requirements:
- Python 3.8+
- Fluvio CLI installed
- Node.js (for frontend if dynamic)
- API key from Hugging Face (optional if local model)

### Local Setup:
```bash
# Clone the repo
git clone https://github.com/your-team/airline-review-analyzer

# Backend Setup
cd backend
pip install -r requirements.txt

# Start FastAPI + Socket.IO
uvicorn app:app --reload

# Start Fluvio producer (in another terminal)
fluvio topic create social-tweets
python producer.py  # (to simulate tweets)

# Frontend Setup
cd ../frontend
# Open index.html in browser or use Live Server extension
