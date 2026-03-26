# Project Report: AI-Based Early Skin Disease Prediction Using Chatbot

## 1. Introduction

### 1.1 Objective

To develop an AI-powered web application that assists in **early screening** of common skin diseases by analyzing user-uploaded images and simple symptom inputs, presented through a chatbot-style interface.

### 1.2 Problem Statement

Early detection of skin conditions can improve outcomes and guide users to seek timely medical care. This project aims to provide an accessible, non-invasive screening tool that combines image-based classification with a short questionnaire to suggest possible conditions and risk level.

### 1.3 Scope

- **Target conditions**: Melanoma, Eczema, Psoriasis, Warts/Molluscum, Acne, Tinea, Vitiligo, Infestations/Bites, Lupus, Rosacea, and Unknown/Normal (11 classes).
- **Users**: General public for self-screening; not for clinical diagnosis.
- **Output**: Predicted disease class, confidence percentage, risk level, and probability distribution across 11 classes.

---

## 2. Methodology

### 2.1 System Architecture

1. **Frontend**: Web page with image upload and three yes/no questions (bleeding, recent growth, itching/pain).
2. **Backend**: Flask server that receives the image and form data, runs the ML model, computes risk level, and returns the result page.
3. **Model**: Pre-trained EfficientNetB0 (transfer learning) with a custom classification head, trained on the project dataset.

### 2.2 Dataset

- **Structure**: Images organized in folders by class: `dataset/Eczema/`, `dataset/Melanoma/`, `dataset/Acne/`, etc.
- **Dataset Size**: Over 15,390 images spread across 11 classes.
- **Split**: 80% training, 20% validation (same seed for reproducibility).
- **Preprocessing**: Resize to 256×256, normalization (1/255), data augmentation (horizontal flip, rotation, zoom, contrast) during training.

### 2.3 Model

- **Base**: EfficientNetB0 (ImageNet weights), frozen initially.
- **Head**: Global average pooling → Dense(256, ReLU) → Dropout(0.5) → Dense(11, softmax).
- **Training**: Phase 1 — train head (8 epochs); Phase 2 — fine-tune last layers (up to 25 epochs with early stopping, learning-rate reduction, and best-model checkpoint).
- **Class imbalance**: Balanced class weights in loss.
- **Target performance**: 70–80% validation accuracy.

### 2.4 Risk Level Logic

- **Inputs**: AI confidence + user answers (bleeding, growth, itching).
- **Scoring**: Bleeding=2, Growth=2, Itching=1. Total ≥4 → High Risk; ≥2 → Medium Risk; else Low Risk.
- **Safety**: If model confidence < 45%, prediction is shown as "Uncertain Prediction."

---

## 3. Implementation

- **Language**: Python 3  
- **Frameworks**: Flask (API and templates), TensorFlow/Keras (model and training)  
- **Frontend**: HTML/CSS, Chart.js for probability bar chart  
- **Deployment**: Local run via `python app.py` (development server)

---

## 4. Results

- **Model accuracy**: The classifier is trained to achieve **70–80% validation accuracy** on the held-out 20% validation set. Final accuracy is logged at the end of training and saved in `model/metrics.json`.
- The system successfully classifies uploaded skin images into one of **11 disease classes** and displays confidence, per-class probabilities, and detailed disease information.
- Risk level (Low/Medium/High) is derived from both the AI output and user-reported symptoms.
- The interface is simple and suitable for non-expert users, with a clear medical disclaimer.
- The project is **ready for submission**: all code, data pipeline, training script, and documentation are in place.

---

## 5. Conclusion

The project demonstrates an end-to-end pipeline for **early skin disease prediction using a chatbot-style web interface**: image upload, symptom questionnaire, deep-learning-based classification, and risk assessment. It is intended for educational and screening purposes only and emphasizes that professional medical consultation remains essential.

### 5.1 Future Work

- Integrate with a conversational chatbot (e.g. NLP) for free-text symptom queries.
- Mobile app deployment (iOS/Android).
- Model explainability (e.g. attention or Grad-CAM) for transparency.

---

**Project**: AI-Based Early Skin Disease Prediction Using Chatbot  
**Submission**: Final project / Academic  
**Year**: 2026
