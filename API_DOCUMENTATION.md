# Neural Navigator - Comprehensive API Documentation

## Table of Contents
1. [Overview](#overview)
2. [Installation & Setup](#installation--setup)
3. [Core Application](#core-application)
4. [Time Management Module](#time-management-module)
5. [Learning Companion Module](#learning-companion-module)
6. [Text-to-Speech Module](#text-to-speech-module)
7. [Flashcards Module](#flashcards-module)
8. [PDF Processing & Search](#pdf-processing--search)
9. [AI Chatbot Module](#ai-chatbot-module)
10. [Multimodal AI Module](#multimodal-ai-module)
11. [Database Operations](#database-operations)
12. [Vector Search Service](#vector-search-service)
13. [Utility Functions](#utility-functions)
14. [Examples & Usage](#examples--usage)

## Overview

Neural Navigator is an all-in-one AI-powered workspace designed specifically for individuals with ADHD. It provides tools for time management, learning assistance, text-to-speech conversion, flashcard generation, PDF processing, and AI-powered conversations.

### Key Features
- 🎙️ Text-to-Speech conversion for documents and text
- 📚 AI-generated flashcards from PDF content
- 🤖 ADHD-specialized chatbot companion
- 🖼️ Multimodal AI for image and document analysis
- ⏳ Time management and task scheduling
- 📄 PDF summarization and search
- 🧠 Sentiment analysis and clinician alerts

## Installation & Setup

### Prerequisites
```bash
python >= 3.8
Google Cloud API access
Google Gemini API access
```

### Installation
```bash
# Clone the repository
git clone https://github.com/quantumadrian/Neural_Navigator.git
cd Neural_Navigator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables
```bash
export GEMINI_API_KEY="your_gemini_api_key"
export TTS_API_KEY="your_google_cloud_tts_api_key"
```

### Running the Application
```bash
# Main Streamlit application
streamlit run main.py

# Alternative TTS-focused app
streamlit run app.py
```

## Core Application

### Main Application Entry Point
**File:** `main.py`

#### `main()` - Application Entry Point
The main Streamlit application with navigation between different modules.

**Features:**
- Home page with navigation buttons
- Session state management for page routing
- Custom CSS styling with animations
- Responsive design

**Navigation Options:**
- Virtual Consultation (AI Chatbot)
- Time Management
- Learning Companion

**Example Usage:**
```python
# Run the main application
streamlit run main.py
```

## Time Management Module

### Time Management Page
**File:** `time_management_page.py`

#### `show_time_management_page()` - Main Time Management Interface
Provides comprehensive time management tools for ADHD users.

**Features:**
- Task creation and management
- Priority-based scheduling
- Daily reflection with AI feedback
- Interactive chat with AI assistant

**Task Management:**
```python
# Task structure
task = {
    "title": str,           # Task name
    "start_time": datetime, # Planned start time
    "end_time": datetime,   # Planned end time
    "duration": int,        # Duration in minutes
    "priority": str,        # "ASAP", "Urgent", "Normal", "Flexible"
    "fixed": bool          # Whether the time is fixed
}
```

### Scheduler Module
**File:** `scheduler.py`

#### `schedule_tasks(tasks: List[Dict]) -> List[Dict]`
Automatically schedules tasks based on priority and constraints.

**Parameters:**
- `tasks`: List of task dictionaries

**Returns:**
- List of scheduled tasks with updated start/end times

**Algorithm:**
1. Sort tasks by fixed status and priority
2. Place fixed tasks first
3. Find available time slots for flexible tasks
4. Avoid scheduling conflicts

**Example:**
```python
from scheduler import schedule_tasks

tasks = [
    {
        "title": "Study Session",
        "duration": 60,
        "priority": "Urgent",
        "fixed": False
    }
]

scheduled = schedule_tasks(tasks)
```

#### `sort_tasks(tasks: List[Dict]) -> List[Dict]`
Sorts tasks by priority and fixed status.

**Priority Order:**
1. Fixed tasks (highest priority)
2. ASAP tasks
3. Urgent tasks
4. Normal tasks
5. Flexible tasks (lowest priority)

## Learning Companion Module

### Learning Companion Page
**File:** `learning_companion_page.py`

#### `show_learning_companion_page()` - Learning Tools Interface
Main interface for learning assistance tools.

**Available Tools:**
- 🎙 Books to Speech (Text-to-Speech)
- 🃏 Flashcards (AI-generated)
- 📖 Books Buddy (PDF companion)

**Navigation:**
```python
# Session state management for tool selection
st.session_state.learning_companion_action = "books_to_speech" | "flashcards" | "books_buddy"
```

## Text-to-Speech Module

### Text-to-Speech Service
**File:** `text_to_speech.py`

#### `tts()` - Main TTS Interface
Streamlit interface for text-to-speech conversion.

**Features:**
- Manual text input conversion
- PDF document audio conversion
- Adjustable voice settings (speed, pitch)
- Long text handling with chunking

#### `split_text_into_chunks(text: str, max_bytes: int = 5000) -> List[str]`
Splits long text into manageable chunks for TTS processing.

**Parameters:**
- `text`: Input text to split
- `max_bytes`: Maximum bytes per chunk (default: 5000)

**Returns:**
- List of text chunks

**Algorithm:**
1. Split text by sentences
2. Group sentences within byte limit
3. Handle oversized sentences by word splitting

#### `speak_text_with_apikey(text: str, speed: float, pitch: float, api_key: str) -> bytes`
Converts text to speech using Google Cloud TTS API.

**Parameters:**
- `text`: Text to convert
- `speed`: Speaking rate (0.25-2.0)
- `pitch`: Voice pitch (-20.0 to 20.0)
- `api_key`: Google Cloud API key

**Returns:**
- Audio content as bytes

**Example:**
```python
from text_to_speech import speak_text_with_apikey

audio_content = speak_text_with_apikey(
    text="Hello, this is a test",
    speed=1.0,
    pitch=0.0,
    api_key="your_api_key"
)
```

#### `synthesize_long_text(text: str, speed: float, pitch: float, api_key: str) -> List[str]`
Handles long text by chunking and creating multiple audio files.

**Parameters:**
- `text`: Long text to convert
- `speed`: Speaking rate
- `pitch`: Voice pitch
- `api_key`: Google Cloud API key

**Returns:**
- List of audio file paths

### PDF Text Extraction
**File:** `reader.py`

#### `extract_text_from_pdf(file) -> str`
Extracts text content from PDF files.

**Parameters:**
- `file`: PDF file object (BytesIO or file path)

**Returns:**
- Extracted text as string

**Example:**
```python
from reader import extract_text_from_pdf

with open("document.pdf", "rb") as file:
    text = extract_text_from_pdf(file)
```

## Flashcards Module

### Flashcards Class
**File:** `flashcards.py`

#### `class Flashcards`
AI-powered flashcard generation from PDF documents.

#### `setup_gemini() -> GenerativeModel`
Initializes the Gemini AI model for flashcard generation.

**Returns:**
- Configured Gemini model instance

#### `extract_text_from_pdf(uploaded_file) -> str`
Extracts text from uploaded PDF files.

**Parameters:**
- `uploaded_file`: Streamlit uploaded file object

**Returns:**
- Extracted text content

#### `generate_flashcards(text: str, gemini_model) -> str`
Generates flashcards from text using Gemini AI.

**Parameters:**
- `text`: Source text for flashcard generation
- `gemini_model`: Configured Gemini model

**Returns:**
- Formatted flashcards as string

**Output Format:**
```
Q: [question]
A: [answer]

Q: [question]
A: [answer]
```

#### `flashcard_app()` - Streamlit Flashcard Interface
Interactive flashcard application with navigation controls.

**Features:**
- PDF upload and processing
- Real-time flashcard generation
- Interactive card navigation
- Progress tracking

**Example Usage:**
```python
from flashcards import flashcard_app

# Run in Streamlit
flashcard_app()
```

## PDF Processing & Search

### PDF Processor
**File:** `pdfprocessor.py`

#### `class PDFProcessor`
Handles PDF file processing and image extraction.

#### `reset_directory(folder_path: str) -> None`
Clears and recreates a directory.

**Parameters:**
- `folder_path`: Path to directory to reset

#### `extract_images(pdf_id: str, pdf_file: str, max_pages: int = None, page_numbers: List[int] = None) -> List[str]`
Extracts images from PDF pages.

**Parameters:**
- `pdf_id`: Unique identifier for the document
- `pdf_file`: Path to PDF file
- `max_pages`: Maximum pages to process
- `page_numbers`: Specific pages to extract

**Returns:**
- List of image file paths

**Example:**
```python
from pdfprocessor import PDFProcessor

processor = PDFProcessor()
images = processor.extract_images(
    pdf_id="doc123",
    pdf_file="document.pdf",
    max_pages=10
)
```

### PDF Search Engine
**File:** `pdfsearchengine.py`

#### `class PDFSearchEngine`
Advanced PDF search using vector embeddings and multimodal AI.

#### `process_pdf_upload(uploaded_file, max_pages: int) -> str`
Processes uploaded PDF and creates searchable index.

**Parameters:**
- `uploaded_file`: Uploaded file object
- `max_pages`: Maximum pages to index

**Returns:**
- Status message

#### `query_pdf(search_query: str, num_results: int = 5) -> Tuple[List[str], str]`
Searches indexed PDF content.

**Parameters:**
- `search_query`: Text query to search for
- `num_results`: Number of results to return

**Returns:**
- Tuple of (image_paths, rag_response)

**Example:**
```python
from pdfsearchengine import PDFSearchEngine

engine = PDFSearchEngine()
status = engine.process_pdf_upload(uploaded_file, max_pages=20)
images, response = engine.query_pdf("machine learning concepts")
```

### PDF Companion
**File:** `pdf_companion.py`

#### `book_buddy()` - PDF Companion Interface
Streamlit interface for PDF interaction and search.

**Features:**
- PDF upload and indexing
- Intelligent query processing
- Visual search results
- AI-generated responses

## AI Chatbot Module

### Basic Chatbot
**File:** `chatbot.py`

#### `chat_with_ai(user_input: str) -> str`
Basic AI chat functionality using Gemini.

**Parameters:**
- `user_input`: User's message

**Returns:**
- AI response text

#### `get_ai_feedback(title: str, planned: int, actual: int) -> str`
Provides AI feedback for time management reflection.

**Parameters:**
- `title`: Task title
- `planned`: Planned time in minutes
- `actual`: Actual time spent

**Returns:**
- Encouraging feedback and advice

### ADHD-Specialized Chatbot
**File:** `adhd_vertexai_chatbot.py`

#### `virtual_consultation()` - Advanced ADHD Chatbot
Specialized chatbot for ADHD support using Vertex AI.

**Features:**
- ADHD-specific conversation context
- Persistent chat history
- Emotional support and guidance
- Task and study assistance

**Specialized Capabilities:**
- Understanding ADHD challenges (time blindness, task paralysis)
- Providing neurodivergent-friendly strategies
- Offering encouragement and motivation
- Breaking down complex tasks into steps

**Example Usage:**
```python
# Chat session is automatically managed in Streamlit
# Users can ask questions like:
# "I'm struggling to start my homework"
# "How can I manage my time better?"
# "I feel overwhelmed with my tasks"
```

## Multimodal AI Module

### MultiModalRAG Class
**File:** `multimodalrag.py`

#### `class MultiModalRAG`
Handles multimodal AI processing with image and text understanding.

#### `query_gemini(query: str, image_paths: List[str]) -> str`
Queries Gemini with text and images.

**Parameters:**
- `query`: Text query
- `image_paths`: List of image file paths

**Returns:**
- AI-generated response

**Example:**
```python
from multimodalrag import MultiModalRAG

rag = MultiModalRAG()
response = rag.query_gemini(
    query="What is shown in these diagrams?",
    image_paths=["image1.png", "image2.png"]
)
```

#### `query_qwen2vl(query: str, image_paths: List[str]) -> str`
Alternative vision model for image analysis.

**Parameters:**
- `query`: Text query
- `image_paths`: List of image paths

**Returns:**
- Model response

**Note:** Currently disabled due to resource constraints, but available for local deployment.

## Database Operations

### QdrantDatabase Class
**File:** `database.py`

#### `class QdrantDatabase`
Vector database management using Qdrant for similarity search.

#### `__init__(qdrant_url: str, collection_name: str, create_collection: bool = False, vector_dim: int = 128)`
Initializes database connection.

**Parameters:**
- `qdrant_url`: Qdrant server URL (None for in-memory)
- `collection_name`: Name of the collection
- `create_collection`: Whether to create collection
- `vector_dim`: Vector dimension

#### `create_collection() -> None`
Creates a new vector collection.

**Configuration:**
- Distance metric: COSINE
- Multi-vector support: MAX_SIM comparator

#### `search_vectors(query_vector: List[float], top_k: int) -> List[Tuple[float, int]]`
Searches for similar vectors.

**Parameters:**
- `query_vector`: Query vector as list of floats
- `top_k`: Number of results to return

**Returns:**
- List of (score, seq_id) tuples

#### `store_image_vectors(image_data: List[Dict[str, Any]]) -> None`
Stores image vectors in the database.

**Parameters:**
- `image_data`: List of image data with vectors

**Example:**
```python
from database import QdrantDatabase

db = QdrantDatabase(
    qdrant_url=None,  # In-memory
    collection_name="documents",
    create_collection=True,
    vector_dim=128
)

# Store vectors
image_data = [
    {
        "colbert_vecs": vector_array,
        "filepath": "image1.png"
    }
]
db.store_image_vectors(image_data)

# Search
results = db.search_vectors(query_vector, top_k=5)
```

## Vector Search Service

### VectorSearchService Class
**File:** `vectorsearchservice.py`

#### `class VectorSearchService`
High-level interface for document vectorization and search.

#### `__init__(instance_id: str, create_collection: bool = True)`
Initializes the vector search service.

**Parameters:**
- `instance_id`: Unique identifier for the instance
- `create_collection`: Whether to create a new collection

#### `search_text_queries(queries: List[str]) -> List[List[Tuple]]`
Searches for text queries in the vector database.

**Parameters:**
- `queries`: List of text queries

**Returns:**
- List of search results for each query

#### `index_pdf_images(pdf_path: str, instance_id: str, max_pages: int, selected_pages: List[int] = None) -> List[str]`
Indexes PDF images for vector search.

**Parameters:**
- `pdf_path`: Path to PDF file
- `instance_id`: Unique identifier
- `max_pages`: Maximum pages to process
- `selected_pages`: Specific pages to process

**Returns:**
- List of extracted image file paths

**Example:**
```python
from vectorsearchservice import VectorSearchService

service = VectorSearchService("session123")

# Index a PDF
images = service.index_pdf_images(
    pdf_path="document.pdf",
    instance_id="doc123",
    max_pages=20
)

# Search
results = service.search_text_queries(["machine learning"])
```

### Document Processor
**File:** `processor.py`

#### `class Processor`
Handles document and image vectorization using ColPali.

#### `__init__(device: str = None, model_name: str = "vidore/colpali-v1.2")`
Initializes the ColPali processor.

**Parameters:**
- `device`: Processing device (auto-detected)
- `model_name`: Pre-trained model name

#### `generate_image_embeddings(image_paths: List[str], batch_size: int = 1) -> List`
Generates embeddings for images.

**Parameters:**
- `image_paths`: List of image file paths
- `batch_size`: Processing batch size

**Returns:**
- List of image embeddings as NumPy arrays

#### `generate_text_embeddings(texts: List[str], batch_size: int = 1) -> List[torch.Tensor]`
Generates embeddings for text queries.

**Parameters:**
- `texts`: List of text inputs
- `batch_size`: Processing batch size

**Returns:**
- List of text embeddings

## Utility Functions

### UUID Management
**File:** `utils.py`

#### `get_or_create_uuid(session_state: Dict) -> str`
Retrieves or creates a unique user identifier.

**Parameters:**
- `session_state`: Application session state

**Returns:**
- UUID string

**Example:**
```python
from utils import get_or_create_uuid

user_id = get_or_create_uuid(st.session_state)
```

## Examples & Usage

### Complete Application Workflow

#### 1. Starting the Application
```bash
# Set environment variables
export GEMINI_API_KEY="your_api_key"
export TTS_API_KEY="your_tts_api_key"

# Run the application
streamlit run main.py
```

#### 2. Time Management Workflow
```python
# 1. Add tasks through the UI
# 2. Set priorities and time constraints
# 3. Generate optimized schedule
# 4. Track actual time spent
# 5. Get AI feedback for improvement
```

#### 3. Learning Companion Workflow
```python
# PDF to Flashcards
# 1. Upload PDF document
# 2. AI extracts key concepts
# 3. Generate Q&A flashcards
# 4. Interactive study session

# PDF Search and Analysis
# 1. Upload and index PDF
# 2. Ask questions about content
# 3. Get AI-generated answers
# 4. View relevant page images
```

#### 4. Text-to-Speech Workflow
```python
# 1. Input text or upload PDF
# 2. Adjust voice settings
# 3. Generate audio
# 4. Play back synthesized speech
```

### API Integration Examples

#### Custom Chatbot Integration
```python
from chatbot import chat_with_ai

def custom_adhd_assistant(user_message):
    """Custom ADHD assistant with additional processing"""
    
    # Pre-process message for ADHD-specific keywords
    if "overwhelmed" in user_message.lower():
        context = "The user is feeling overwhelmed. "
        user_message = context + user_message
    
    # Get AI response
    response = chat_with_ai(user_message)
    
    # Post-process for encouragement
    if "can't" in response.lower():
        response += "\n\nRemember: You're capable of more than you think! 💪"
    
    return response
```

#### PDF Processing Pipeline
```python
from pdfprocessor import PDFProcessor
from vectorsearchservice import VectorSearchService
from multimodalrag import MultiModalRAG

def process_document_pipeline(pdf_path, queries):
    """Complete document processing and query pipeline"""
    
    # Initialize components
    processor = PDFProcessor()
    search_service = VectorSearchService("session_id")
    rag = MultiModalRAG()
    
    # Process PDF
    images = search_service.index_pdf_images(
        pdf_path=pdf_path,
        instance_id="doc_id",
        max_pages=20
    )
    
    results = []
    for query in queries:
        # Search for relevant pages
        search_results = search_service.search_text_queries([query])[0]
        
        # Get top image paths
        top_images = [
            f"pdf_images/doc_id/image_{result[1] + 1}.png"
            for result in search_results[:3]
        ]
        
        # Generate AI response
        response = rag.query_gemini(query, top_images)
        
        results.append({
            "query": query,
            "response": response,
            "relevant_images": top_images
        })
    
    return results
```

### Error Handling Best Practices

#### Graceful Degradation
```python
def safe_ai_request(func, *args, **kwargs):
    """Wrapper for safe AI API calls"""
    try:
        return func(*args, **kwargs)
    except Exception as e:
        logging.error(f"AI request failed: {e}")
        return "I'm having trouble processing that right now. Please try again later."

# Usage
response = safe_ai_request(chat_with_ai, user_input)
```

#### Resource Management
```python
def process_with_cleanup(pdf_file, temp_dir):
    """Process files with automatic cleanup"""
    try:
        # Process the file
        results = process_pdf(pdf_file)
        return results
    finally:
        # Always cleanup temporary files
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
```

### Performance Optimization

#### Batch Processing
```python
# Process multiple texts efficiently
texts = ["text1", "text2", "text3"]
embeddings = processor.generate_text_embeddings(texts, batch_size=3)
```

#### Memory Management
```python
# Clear GPU memory after processing
torch.cuda.empty_cache()
```

### Security Considerations

#### API Key Management
```python
import os
from dotenv import load_dotenv

load_dotenv()

# Never hardcode API keys
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set")
```

#### Input Validation
```python
def validate_pdf_upload(file):
    """Validate uploaded PDF files"""
    if not file:
        raise ValueError("No file provided")
    
    if not file.name.endswith('.pdf'):
        raise ValueError("File must be a PDF")
    
    if file.size > 50 * 1024 * 1024:  # 50MB limit
        raise ValueError("File too large")
    
    return True
```

## Troubleshooting

### Common Issues

#### 1. API Key Errors
```
Error: Gemini API Error
Solution: Ensure GEMINI_API_KEY environment variable is set correctly
```

#### 2. Memory Issues
```
Error: CUDA out of memory
Solution: Reduce batch_size or use CPU-only mode
```

#### 3. PDF Processing Failures
```
Error: No extractable text found in PDF
Solution: Ensure PDF contains text (not just images) or use OCR preprocessing
```

### Debug Mode
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Performance Monitoring
```python
import time

def timed_function(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds")
        return result
    return wrapper
```

## Contributing

### Adding New Features
1. Follow the existing code structure
2. Add comprehensive documentation
3. Include error handling
4. Add usage examples
5. Update this documentation

### Testing
```python
# Example test structure
def test_flashcard_generation():
    flashcard = Flashcards()
    model = flashcard.setup_gemini()
    result = flashcard.generate_flashcards("Test content", model)
    assert "Q:" in result
    assert "A:" in result
```

This documentation provides a comprehensive guide to all public APIs, functions, and components in the Neural Navigator application. Each module is documented with its purpose, parameters, return values, and practical examples to help developers understand and extend the application effectively.