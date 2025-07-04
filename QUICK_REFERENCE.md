# Neural Navigator - Quick Reference Guide

## 🚀 Quick Start

### Run the Application
```bash
# Set environment variables
export GEMINI_API_KEY="your_api_key"
export TTS_API_KEY="your_tts_api_key"

# Start the main app
streamlit run main.py
```

## 📚 Common API Usage

### Text-to-Speech
```python
# Basic TTS
from text_to_speech import speak_text_with_apikey
audio = speak_text_with_apikey("Hello world", 1.0, 0.0, api_key)

# PDF to Speech
from reader import extract_text_from_pdf
text = extract_text_from_pdf(pdf_file)
```

### Flashcards
```python
# Generate flashcards from text
from flashcards import Flashcards
fc = Flashcards()
model = fc.setup_gemini()
cards = fc.generate_flashcards(text, model)
```

### PDF Search
```python
# Index and search PDFs
from pdfsearchengine import PDFSearchEngine
engine = PDFSearchEngine()
engine.process_pdf_upload(file, max_pages=20)
images, response = engine.query_pdf("search query")
```

### Chat with AI
```python
# Basic chat
from chatbot import chat_with_ai
response = chat_with_ai("How can I manage my time better?")

# Time management feedback
from chatbot import get_ai_feedback
feedback = get_ai_feedback("Study", planned=60, actual=90)
```

### Task Scheduling
```python
# Schedule tasks
from scheduler import schedule_tasks
tasks = [{"title": "Study", "duration": 60, "priority": "Urgent", "fixed": False}]
scheduled = schedule_tasks(tasks)
```

### Vector Search
```python
# Vector database operations
from vectorsearchservice import VectorSearchService
service = VectorSearchService("session_id")
results = service.search_text_queries(["machine learning"])
```

### Multimodal AI
```python
# Query with images
from multimodalrag import MultiModalRAG
rag = MultiModalRAG()
response = rag.query_gemini("What's in this image?", ["image.png"])
```

## 🛠️ Core Classes

| Class | File | Purpose |
|-------|------|---------|
| `Flashcards` | flashcards.py | AI flashcard generation |
| `PDFProcessor` | pdfprocessor.py | PDF image extraction |
| `PDFSearchEngine` | pdfsearchengine.py | PDF search & indexing |
| `MultiModalRAG` | multimodalrag.py | Multimodal AI queries |
| `QdrantDatabase` | database.py | Vector database ops |
| `VectorSearchService` | vectorsearchservice.py | High-level search |
| `Processor` | processor.py | Document vectorization |

## 📱 Streamlit Pages

| Function | File | Purpose |
|----------|------|---------|
| `show_time_management_page()` | time_management_page.py | Time management UI |
| `show_learning_companion_page()` | learning_companion_page.py | Learning tools UI |
| `virtual_consultation()` | adhd_vertexai_chatbot.py | ADHD chatbot UI |
| `flashcard_app()` | flashcards.py | Flashcard UI |
| `tts()` | text_to_speech.py | Text-to-speech UI |
| `book_buddy()` | pdf_companion.py | PDF companion UI |

## 🔧 Utility Functions

| Function | File | Purpose |
|----------|------|---------|
| `get_or_create_uuid()` | utils.py | Session management |
| `extract_text_from_pdf()` | reader.py | PDF text extraction |
| `split_text_into_chunks()` | text_to_speech.py | Text chunking for TTS |
| `schedule_tasks()` | scheduler.py | Task scheduling |
| `sort_tasks()` | scheduler.py | Task prioritization |

## 📊 Data Structures

### Task Object
```python
task = {
    "title": str,           # Task name
    "start_time": datetime, # Start time
    "end_time": datetime,   # End time  
    "duration": int,        # Minutes
    "priority": str,        # "ASAP", "Urgent", "Normal", "Flexible"
    "fixed": bool          # Fixed time slot
}
```

### Image Data for Vector Storage
```python
image_data = {
    "colbert_vecs": np.array,  # Vector embeddings
    "filepath": str            # Image file path
}
```

## 🎛️ Configuration

### Environment Variables
```bash
GEMINI_API_KEY=your_gemini_api_key
TTS_API_KEY=your_google_cloud_tts_api_key
```

### Voice Settings (TTS)
```python
speed = 0.25 to 2.0      # Speaking rate
pitch = -20.0 to 20.0    # Voice pitch
```

### Priority Levels
```python
priority_map = {
    "ASAP": 1,      # Highest priority
    "Urgent": 2,    # High priority
    "Normal": 3,    # Medium priority  
    "Flexible": 4   # Lowest priority
}
```

## 🐛 Common Error Handling

### API Errors
```python
try:
    response = chat_with_ai(message)
except Exception as e:
    return "I'm having trouble right now. Please try again."
```

### File Validation
```python
def validate_pdf(file):
    if not file or not file.name.endswith('.pdf'):
        raise ValueError("Invalid PDF file")
    if file.size > 50 * 1024 * 1024:  # 50MB
        raise ValueError("File too large")
```

### Memory Management
```python
import torch
torch.cuda.empty_cache()  # Clear GPU memory
```

## 📋 Session State Variables

### Time Management
```python
st.session_state["tasks"]              # Task list
st.session_state["completed_tasks"]    # Completed tasks
st.session_state["chat_history"]       # Chat history
```

### Learning Companion
```python
st.session_state.learning_companion_action  # Current tool
st.session_state.flashcards_list           # Generated flashcards
st.session_state.current_index             # Current flashcard
```

### Navigation
```python
st.session_state.page  # Current page: "home", "time_management", etc.
```

## 🎯 Quick Troubleshooting

| Issue | Solution |
|-------|----------|
| API key error | Check environment variables |
| Memory error | Reduce batch_size, use CPU mode |
| PDF processing fails | Ensure PDF has extractable text |
| TTS fails | Check text length, split into chunks |
| Search returns empty | Verify PDF indexing completed |

## 🔗 External Dependencies

```python
# Core ML/AI
import google.generativeai as genai
import torch
from transformers import *

# PDF Processing  
import PyPDF2
from pdf2image import convert_from_path

# Web UI
import streamlit as st

# Vector DB
from qdrant_client import QdrantClient

# Utilities
import requests
import base64
import uuid
```

## 📈 Performance Tips

1. **Batch Processing**: Process multiple items together
2. **Memory Management**: Clear GPU cache after operations
3. **Chunking**: Split large texts for TTS
4. **Caching**: Use Streamlit caching for expensive operations
5. **Async**: Consider async for multiple API calls

## 🎨 UI Components

### Buttons
```python
if st.button("🔊 Speak Text"):
if st.button("📅 Generate Schedule"):
if st.button("⬅️ Back to Home"):
```

### File Uploads
```python
uploaded_file = st.file_uploader("Choose PDF", type="pdf")
```

### Sliders
```python
speed = st.sidebar.slider("Speed", 0.25, 2.0, 1.0)
max_pages = st.slider("Max pages", 1, 50, 20)
```

This quick reference provides immediate access to the most commonly used functions and patterns in the Neural Navigator application.