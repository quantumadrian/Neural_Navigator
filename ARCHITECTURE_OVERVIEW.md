# Neural Navigator - Architecture Overview

## System Architecture

Neural Navigator is a modular, AI-powered application designed specifically for individuals with ADHD. The system follows a layered architecture with clear separation of concerns.

```
┌─────────────────────────────────────────────────────────────┐
│                     Presentation Layer                      │
├─────────────────────────────────────────────────────────────┤
│  Streamlit UI Components (main.py, *_page.py files)        │
│  • Home Navigation                                         │
│  • Time Management Interface                               │
│  • Learning Companion Interface                            │
│  • PDF Companion Interface                                 │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    Application Layer                        │
├─────────────────────────────────────────────────────────────┤
│  Business Logic & Orchestration                            │
│  • Task Scheduling (scheduler.py)                          │
│  • PDF Processing Pipeline (pdfsearchengine.py)            │
│  • Flashcard Generation (flashcards.py)                    │
│  • Text-to-Speech Pipeline (text_to_speech.py)             │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                      Service Layer                          │
├─────────────────────────────────────────────────────────────┤
│  AI & Processing Services                                   │
│  • Multimodal AI (multimodalrag.py)                        │
│  • Vector Search (vectorsearchservice.py)                  │
│  • Document Processing (processor.py)                       │
│  • Chatbot Services (chatbot.py, adhd_vertexai_chatbot.py) │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                       Data Layer                            │
├─────────────────────────────────────────────────────────────┤
│  Storage & External APIs                                    │
│  • Vector Database (database.py - Qdrant)                  │
│  • PDF Processing (pdfprocessor.py)                        │
│  • File I/O (reader.py, utils.py)                          │
│  • External APIs (Google Cloud, Gemini)                    │
└─────────────────────────────────────────────────────────────┘
```

## Component Relationships

### Core Application Flow

1. **Entry Point**: `main.py`
   - Streamlit app initialization
   - Navigation and routing
   - Session state management

2. **Feature Modules**: 
   - `time_management_page.py` → `scheduler.py` → `chatbot.py`
   - `learning_companion_page.py` → `flashcards.py`, `text_to_speech.py`, `pdf_companion.py`
   - `pdf_companion.py` → `pdfsearchengine.py` → `vectorsearchservice.py`

3. **AI Services**:
   - All modules → `multimodalrag.py` (Gemini API)
   - PDF features → `processor.py` (ColPali embeddings)
   - Chat features → `chatbot.py` / `adhd_vertexai_chatbot.py`

4. **Data Storage**:
   - Vector embeddings → `database.py` (Qdrant)
   - File processing → `pdfprocessor.py`, `reader.py`
   - Session data → Streamlit session state

## Detailed Component Analysis

### 1. Presentation Layer

#### Main Navigation (`main.py`)
- **Purpose**: Central hub and navigation
- **Dependencies**: All page modules
- **State Management**: Controls global session state
- **Styling**: Custom CSS with animations

#### Feature Pages
- **Time Management**: Task scheduling interface
- **Learning Companion**: Educational tools hub  
- **PDF Companion**: Document interaction interface

**Design Patterns**:
- Single Page Application (SPA) pattern
- Session state for navigation
- Component-based UI structure

### 2. Application Layer

#### Task Scheduling (`scheduler.py`)
```python
# Priority-based scheduling algorithm
def schedule_tasks(tasks):
    # 1. Sort by priority and fixed status
    # 2. Place fixed tasks first
    # 3. Find time slots for flexible tasks
    # 4. Avoid conflicts
```

**Algorithm**: Greedy scheduling with priority constraints

#### PDF Search Engine (`pdfsearchengine.py`)
```python
# Complete PDF processing pipeline
class PDFSearchEngine:
    def process_pdf_upload():
        # 1. Extract images from PDF
        # 2. Generate vector embeddings
        # 3. Store in vector database
        
    def query_pdf():
        # 1. Convert query to embeddings
        # 2. Search vector database
        # 3. Retrieve relevant images
        # 4. Generate AI response
```

**Pattern**: Command pattern with pipeline processing

### 3. Service Layer

#### Vector Search Service (`vectorsearchservice.py`)
- **Purpose**: High-level interface for document vectorization
- **Dependencies**: `processor.py`, `database.py`, `pdfprocessor.py`
- **Pattern**: Facade pattern

#### Multimodal AI (`multimodalrag.py`)
- **Models Supported**: Gemini 1.5 Flash, Qwen2VL (optional)
- **Capabilities**: Text + image understanding
- **Pattern**: Strategy pattern for model selection

#### Document Processor (`processor.py`)
- **Model**: ColPali for document understanding
- **Purpose**: Convert documents/images to vector embeddings
- **Optimization**: Quantization for memory efficiency

### 4. Data Layer

#### Vector Database (`database.py`)
```python
class QdrantDatabase:
    # Vector storage with cosine similarity
    # Multi-vector support for complex documents
    # In-memory option for development
```

**Configuration**:
- Distance Metric: COSINE
- Vector Dimension: 128 (configurable)
- Collection Management: Auto-creation

#### File Processing
- **PDF Processing**: `pdfprocessor.py` (pdf2image conversion)
- **Text Extraction**: `reader.py` (PyPDF2 based)
- **Utilities**: `utils.py` (UUID management)

## Data Flow Diagrams

### PDF Processing Flow
```
PDF Upload → Image Extraction → Vector Generation → Database Storage
    ↓              ↓                    ↓               ↓
pdfprocessor → processor.py → database.py → Qdrant
    ↓
Search Query → Vector Search → Image Retrieval → AI Response
       ↓              ↓              ↓            ↓
vectorsearch → database.py → multimodalrag → Gemini API
```

### Flashcard Generation Flow
```
PDF Upload → Text Extraction → AI Processing → Flashcard UI
    ↓              ↓               ↓             ↓
flashcards → reader.py → Gemini API → Streamlit
```

### Time Management Flow  
```
Task Input → Scheduling → AI Feedback → Reflection
    ↓           ↓           ↓            ↓
UI Form → scheduler.py → chatbot.py → Streamlit
```

## Technology Stack

### Core Framework
- **Frontend**: Streamlit (Python web framework)
- **Backend**: Python 3.8+
- **State Management**: Streamlit session state

### AI/ML Components
- **LLM**: Google Gemini 1.5 Flash/Pro
- **Vision Model**: ColPali v1.2 (document understanding)
- **Alternative Vision**: Qwen2VL (optional)
- **Vector Database**: Qdrant (similarity search)

### Processing Libraries
- **PDF**: PyPDF2, pdf2image
- **ML Framework**: PyTorch, Transformers
- **Image Processing**: PIL (Pillow)
- **Audio**: Google Cloud Text-to-Speech

### External APIs
- **Google Cloud TTS**: Text-to-speech conversion
- **Vertex AI**: Advanced chatbot functionality
- **Gemini API**: General AI capabilities

## Security Architecture

### API Key Management
```python
# Environment-based configuration
import os
api_key = os.getenv("GEMINI_API_KEY")
```

### Input Validation
- File type validation (PDF only)
- File size limits (50MB)
- Text length validation for TTS

### Data Privacy
- In-memory vector database option
- No persistent storage of sensitive data
- Session-based user identification

## Scalability Considerations

### Performance Optimizations
1. **Batch Processing**: Multiple texts/images processed together
2. **Model Quantization**: 4-bit quantization for memory efficiency
3. **Chunking**: Large texts split for processing
4. **Caching**: Streamlit caching for expensive operations

### Memory Management
```python
# GPU memory clearing
torch.cuda.empty_cache()

# Offloading for large models
device_map="cpu",
offload_folder="offload"
```

### Horizontal Scaling Options
- **Database**: Qdrant cluster deployment
- **API**: Rate limiting and request queuing
- **Processing**: Background task queues
- **Storage**: Distributed file storage

## Error Handling Strategy

### Graceful Degradation
```python
def safe_ai_request(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        logging.error(f"AI request failed: {e}")
        return fallback_response
```

### Error Recovery
- Automatic retry for transient failures
- Fallback to alternative models
- User-friendly error messages
- Comprehensive logging

## Deployment Architecture

### Development Setup
```bash
# Local development
streamlit run main.py

# Environment variables via .env
load_dotenv()
```

### Production Considerations
- **Container**: Docker deployment
- **Secrets**: Kubernetes secrets or cloud secret managers
- **Monitoring**: Application performance monitoring
- **Logging**: Centralized logging system

### Cloud Deployment Options
1. **Streamlit Cloud**: Direct deployment
2. **Google Cloud Run**: Containerized deployment
3. **AWS ECS/Fargate**: Container orchestration
4. **Kubernetes**: Full orchestration

## Extension Points

### Adding New Features
1. **New Page**: Create `*_page.py` with Streamlit interface
2. **New AI Service**: Implement in service layer with common interface
3. **New Processing**: Add to processor layer with vectorization
4. **New Storage**: Implement database interface

### Plugin Architecture
```python
# Example plugin interface
class AIServicePlugin:
    def process_query(self, query: str) -> str:
        raise NotImplementedError
        
    def supports_multimodal(self) -> bool:
        return False
```

### Configuration Management
```python
# Centralized configuration
class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    TTS_API_KEY = os.getenv("TTS_API_KEY")
    MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB
    VECTOR_DIMENSION = 128
```

## Performance Metrics

### Key Performance Indicators
- **Response Time**: AI query response < 5 seconds
- **Upload Processing**: PDF indexing < 30 seconds per 20 pages
- **Memory Usage**: < 4GB RAM for standard operations
- **Accuracy**: Flashcard relevance > 85%

### Monitoring Points
- API call latency and success rates
- Memory usage per operation
- User session duration and engagement
- Error rates by component

This architecture overview provides a comprehensive understanding of the Neural Navigator system design, enabling developers to effectively maintain, extend, and deploy the application.