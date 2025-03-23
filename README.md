# Neural_Navigator
## Empowering individuals with ADHD through technology!

### Overview
**Neural_Navigator** is a digital solution designed to assist individuals with ADHD in managing their daily activities, learning, and mental well-being. The platform integrates multiple features to enhance focus, organization, and emotional support through AI-driven tools.

## Features
### 🎙️ Text-to-Speech
- Transcribes spoken words into text.
- Helps users document thoughts and notes effortlessly.

### 📚 Flashcards
- Supports learning and assimilation.
- Users can create, store, and review flashcards to reinforce information retention.

### 🤖 Chatbot Companion
- Provides daily support and motivation.
- Assists users in managing tasks, reminders, and emotional well-being.

### 🖼️ Photo Interpretation
- Allows users to upload images and receive AI-generated descriptions.
- Supports individuals who process visual information better.

### 🧠 Sentiment Analysis & Clinician Alerts
- Detects emotional states such as anxiety and depression.
- Sends notifications to a designated clinician in case of extreme negative emotions.

### ⏳ Time Management Component
- Helps users organize and track their time effectively.
- Provides tools such as timers, schedules, and reminders to enhance productivity.

### 📄 PDF Summarization
- Extracts and summarizes key points from PDFs.
- Aids in quick information processing for individuals with ADHD.

## Technologies Used
- **Frontend:** Streamlit
- **Cloud hosting Services:**  Google Cloud API
- **AI Services:** Google Gemini API for sentiment and chatbot interactions,Google ai studio
- **Notification System:** In built dashboard notification

## Installation & Setup
### Prerequisites
- Python 3.x
- Access to Google cloud and Google Gemini Services
- Virtual environment (optional but recommended)

### Backend Setup
```sh
# Clone the repository
git clone https://github.com/quantumadrian/Neural_Navigator.git
cd Neural_Navigator

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows

# Install dependencies
pip install -r requirements.txt

# Run the backend
python app.py
