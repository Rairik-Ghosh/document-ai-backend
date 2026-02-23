#  Document AI Backend

An intelligent multi-document processing backend built with **FastAPI** and **PaddleOCR** that extracts structured information from identity documents and merges them into a unified person profile.

---

##  Overview

This system performs end-to-end document intelligence:

1. Image Preprocessing
2. Optical Character Recognition (OCR)
3. Document Type Classification
4. Field Extraction
5. Multi-Document Data Merging
6. Structured JSON Output Generation

It is designed as a backend service that can integrate with NLP systems for translation, validation, or database storage.

---

##  System Architecture

Client Upload (Images)
↓
Image Enhancement + Blur Detection
↓
OCR Engine (PaddleOCR)
↓
Document Type Detection
↓
Field Extraction (Rule-based Extractors)
↓
Multi-Document Merge Engine
↓
Structured JSON Response
↓
Optional: NLP / Database Integration

---

##  Tech Stack

- **Python**
- **FastAPI**
- **PaddleOCR**
- **OpenCV**
- **Uvicorn**
- **Git**

---

##  Project Structure

document_ai/
│
├── api.py # FastAPI entry point
├── requirements.txt
│
├── src/
│ ├── ocr/
│ │ └── ocr_engine.py
│ │
│ ├── extraction/
│ │ └── birth_extractor.py
│ │
│ ├── doc_classifier/
│ │ └── detect_doc_type.py
│ │
│ ├── utils/
│ │ ├── image_enhancement.py
│ │ └── blur_detection.py
│ │
│ ├── multi_document_pipeline.py
│ ├── person_merger.py
│ └── vision_pipeline.py
│
└── data/

---

## ✨ Key Features

✔ Multi-document upload support  
✔ Automatic document type detection  
✔ Structured field extraction (Name, DOB, etc.)  
✔ Conflict detection across documents  
✔ Person profile consolidation  
✔ JSON file generation with timestamp + request ID  
✔ Backend-ready REST API  

---

##  API Endpoint

### POST `/process-documents`

Upload one or multiple images.

### Response Example:

```json
{
  "request_id": "uuid",
  "timestamp": "2026-01-24T08:37:55",
  "documents": [
    {
      "document_type": "Birth Certificate",
      "fields": {
        "name": "Rairik Ghosh",
        "dob": "13/07/2004"
      }
    }
  ],
  "person_profile": {
    "name": "Rairik Ghosh",
    "dob": "13/07/2004",
    "conflicts": []
  }
}
```

---

## How To Run

pip install -r requirements.txt
uvicorn api:app --reload

Then open: http://127.0.0.1:8000/docs

---

## Design Decisions

- Modular architecture for scalability
- Separate OCR, classification, and extraction layers
- Clean API abstraction for integration with NLP or databases
- JSON-first structured outputs for downstream systems

---

## Future Improvements

- Add ML-based document classification
- Add ML-based document classification
- Integrate database persistence layer
- Add Docker support
- Add authentication and rate limiting

---

## Author

Rairik Ghosh

Built as part of an AI-based document intelligence system



