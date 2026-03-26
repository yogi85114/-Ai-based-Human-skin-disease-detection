# AI-Based Early Skin Disease Prediction Using Chatbot

**Final Year / Academic Project Submission — Ready to Submit**

A web-based AI dermatology assistant for early screening of skin conditions. Users upload a skin image, answer clinical questions (bleeding, growth, itching, duration), and receive a predicted disease class with confidence and risk level. The trained model targets **70–80% validation accuracy** (see `model/metrics.json` after training).

---

## Features

- **Image-based prediction**: Upload a skin image; the model predicts among **11 classes** (Acne, Eczema, Infestations & Bites, Lupus, Melanoma, Psoriasis, Rosacea, Tinea, Unknown/Normal, Vitiligo, Warts & Molluscum).
- **Chatbot-style flow**: Simple form with image upload and symptom questions (bleeding, size increase, itching/pain, duration).
- **Risk assessment**: Combines AI prediction with symptom answers to show Low / Medium / High risk.
- **Confidence handling**: Predictions below 45% confidence are shown as "Uncertain Prediction."
- **Visual report**: Result page shows predicted disease, confidence %, risk level, disease info card, and a bar chart of class probabilities.
- **Detailed disease info**: Each prediction includes full name, description, symptoms, causes, treatment options, severity rating, and when to see a doctor.
- **Analysis history**: Session-based history of recent screenings.
- **Medical disclaimer**: Clear notice that the system is for screening only and not a substitute for a doctor.

---

## Technology Stack

| Component        | Technology                          |
|-----------------|-------------------------------------|
| Backend         | Python 3, Flask                     |
| ML Model        | TensorFlow 2, Keras, EfficientNetB0 |
| Frontend        | HTML, CSS, Chart.js                  |
| Data / Training | image_dataset_from_directory, augmentation, class weights |

---

## Project Structure

```
Skin_Disease_Chatbot/
├── app.py                 # Flask app and /predict route
├── predict.py             # Load model, run inference
├── disease_info.py        # Disease information database (11 diseases + Uncertain)
├── train_model.py         # Train and save model + class_names.json
├── requirements.txt       # Python dependencies
├── run.bat / run.sh       # Quick launcher scripts
├── README.md              # This file
├── PROJECT_REPORT.md      # Submission report (objectives, methodology, results)
├── DATA_README.md         # Dataset structure and how to add more data
├── SUBMISSION_CHECKLIST.md # Pre-submit checklist
├── .gitignore
├── dataset/               # Training images (class-named subfolders)
│   ├── Acne/
│   ├── Eczema/
│   ├── Infestations_Bites/
│   ├── Lupus/
│   ├── Melanoma/
│   ├── Psoriasis/
│   ├── Rosacea/
│   ├── Tinea/
│   ├── Unknown_Normal/
│   ├── Vitiligo/
│   └── Warts Molluscum/
├── model/
│   ├── skin_model.h5          # Trained Keras model
│   ├── best_weights.weights.h5 # Best checkpoint weights
│   ├── class_names.json       # Class labels (auto-generated on train)
│   └── metrics.json           # Validation accuracy (target 70–80%)
├── scripts/
│   ├── download_dataset.py    # Helper to add more data
│   ├── augment_dataset.py     # Data augmentation utility
│   ├── generate_architecture.py
│   ├── generate_graphs.py
│   └── generate_methodology.py
├── static/
│   └── style.css              # Premium dark-themed CSS
└── templates/
    ├── index.html             # Upload + questionnaire + disease gallery
    ├── result.html            # Diagnosis report + chart + disease info
    ├── about.html             # Technology & data info page
    └── history.html           # Session screening history
```

---

## Installation

### 1. Clone or extract the project

```bash
cd Skin_Disease_Chatbot
```

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate    # Windows
# source venv/bin/activate   # Linux/Mac
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Dataset and model

- **To run the app only**: Ensure `model/skin_model.h5` and `model/class_names.json` exist (included in submission or generated after training).
- **To train (target 70–80% val accuracy)**: Place images in `dataset/<ClassName>/`, then run:
  ```bash
  python train_model.py
  ```
  Final validation accuracy is printed and saved in `model/metrics.json`.

---

## How to Run

### Start the web application

```bash
python app.py
```

Open a browser at **http://127.0.0.1:5000**.

1. Upload a skin image (any common format: JPG, PNG, WEBP, HEIC, TIFF, etc.).
2. Answer the symptom questions (bleeding, growth, itching, duration).
3. Click **Analyze Image** to get the AI diagnosis report and risk level.

---

## Dataset

- **Classes (11)**: Acne, Eczema, Infestations & Bites, Lupus, Melanoma, Psoriasis, Rosacea, Tinea, Unknown/Normal, Vitiligo, Warts & Molluscum.
- **Structure**: Each class has its own folder under `dataset/`; images can be `.jpg`, `.jpeg`, `.png`, `.bmp`.
- **Training**: 80% train / 20% validation split; data augmentation (flip, rotation, zoom, contrast); balanced class weights.
- For adding more data or using Kaggle datasets, see **DATA_README.md**.

---

## Training the Model

```bash
python train_model.py
```

- Uses EfficientNetB0 (ImageNet) with a custom head.
- Two phases: head training (8 epochs), then fine-tuning (up to 25 epochs with early stopping and learning-rate reduction).
- **Target: 70–80% validation accuracy.** Final accuracy is printed and saved in `model/metrics.json`.
- Saves `model/skin_model.h5`, `model/class_names.json`, and `model/metrics.json`.

---

## Disclaimer

This system is for **educational and early screening purposes only**. It is not a medical device and must not replace consultation with a certified dermatologist or healthcare provider. Always seek professional medical advice for diagnosis and treatment.

---

## Author / Submission

**Project**: AI-Based Early Skin Disease Prediction Using Chatbot  
**Type**: Academic / Final project submission  
**Date**: 2026

- **PROJECT_REPORT.md** – Objectives, methodology, results, conclusion  
- **SUBMISSION_CHECKLIST.md** – Checklist before submitting
