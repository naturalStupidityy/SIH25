# SIH-2025 : AYUSH Terminology Micro-Service  
> Ministry of Ayush – India  
> Problem ID 25026

## 🎯 Problem Statement
India’s Ayush sector is transitioning to interoperable digital records.  
We must harmonise **NAMASTE** (4 500+ AYUSH terms) with **ICD-11 TM2 & Biomedicine** (529 traditional + global codes) inside **FHIR R4**-compliant EMRs.

## ✅ What We Built (so far)
- Lightweight **Flask** micro-service  
- **Search** `/api/ayush?q=fever` → JSON codes  
- **Docker** image ≤ 12 MB  
- **Unit tests** + **Swagger** stub  
- **MIT** licensed – open for vendors

## 🚀 Quick Start
```bash
git clone https://github.com/naturalStupidityy/SIH25.git
cd SIH25
python3 -m pip install -r requirements.txt
python3 src/app.py
# browse http://localhost:5000/api/ayush?q=naso

