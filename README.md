# 🚌 Bus Buddy – AI-Based Bus Arrival Time Estimator

**Bus Buddy** is an AI-powered web application that provides **real-time bus arrival time predictions** for Mumbai’s **BEST bus network**.  
The system uses **machine learning (LSTM)** and simulated real-time factors like traffic, crowd density, and weather to deliver accurate ETA predictions.

This project is built as a **smart transit solution** to improve daily commuting using AI-driven insights.

---

## 🌆 Live Demo (UI Preview)

✨ Modern UI with:
- Real-time ETA cards
- AI confidence score
- Traffic, weather & crowd indicators
- Route visualization
- Peak hour alerts

---

## 🎯 Key Features 

### 🔍 Smart Bus Search
- Select **From** and **To** bus stops
- Instantly view available buses on that route

### ⏱️ AI-Based Arrival Prediction
- Estimated arrival time (in minutes)
- AI confidence percentage (85–98%)
- On-Time / Delayed / Early status

### 🧠 AI Intelligence
- LSTM neural network for time-series prediction
- Peak-hour congestion detection
- Traffic density analysis

### 🚦 Real-Time Factors (Simulated)
- Traffic: Low / Medium / High
- Crowd density levels
- Weather impact
- Peak hour warnings

### 🌱 Eco-Friendly Insights
- Carbon footprint awareness
- Encourages public transport usage

### 📞 Emergency & Support
- Emergency helpline numbers
- Email support
- Head office information (Mumbai-based)

---

## 🛠️ Tech Stack

### Frontend
- HTML5  
- CSS3  
- Responsive UI design  
- Modern UI cards & indicators  

### Backend
- Python  
- Flask (API-based architecture)

### Machine Learning
- NumPy  
- Pandas  
- Scikit-learn  
- TensorFlow / Keras (LSTM model)

### Data Sources
- Dummy & simulated BEST bus data
- Historical transit patterns (mock)

---

## 📊 Dataset Description

This project uses **simulated transit data**, including:

- Bus Numbers (e.g., 209, 331)
- Route names (S.V. Road Kandivali → Poinsar Depot)
- Intermediate stops
- Scheduled frequency
- Estimated arrival time
- Delay / On-time status
- Traffic density
- Crowd levels
- Weather conditions

⚠️ **No real BEST or government live data is used.**

---

## 🤖 Machine Learning Workflow

### Model Used
- **LSTM (Long Short-Term Memory)** – Time Series Prediction

### Input Features
- Distance between stops
- Time of day
- Historical delays
- Traffic density
- Crowd level
- Weather impact

### Output
- Predicted arrival time (ETA)
- Confidence score (%)

---

## 🧭 How the System Works

1. User selects:
   - Current bus stop
   - Destination bus stop
2. System identifies:
   - Valid routes
   - Available buses
3. ML model processes:
   - Historical + simulated real-time data
4. User receives:
   - ETA
   - Delay status
   - AI confidence
   - Route details
