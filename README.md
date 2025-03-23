# Neural_Navigator
## Empowering individuals with ADHD through technology!

### Overview
People with ADHD often face challenges that traditional productivity and learning tools fail to address. Burnout is common — not due to lack of effort, but because conventional study methods are rigid and ignore neurodiverse learning styles.

Beyond academics, ADHD symptoms like time blindness, task paralysis, and emotional dysregulation make it extremely difficult to plan, prioritize, and stay on track. Many existing tools target one of these issues — like a focus timer, a calendar, or a mood tracker — but none offer a unified system that ADHD users can rely on.

Research shows that juggling multiple apps can actually make things worse. According to ADDitude Magazine, the mental overhead of switching between scattered tools often increases stress, overload, and avoidance behaviors — exactly what ADHD brains struggle with most.

This inspired us to create **Neural Navigator** — an **all-in-one** AI-powered workspace built specifically for people with ADHD. Instead of forcing users to adapt to tools designed for neurotypical workflows, our platform adapts to them: streamlining scheduling, studying, and emotional regulation into one cohesive space. With real-time support powered by Google Cloud and Gemini AI, Neural Navigator helps ADHD minds work with — not against — how they function best.

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
