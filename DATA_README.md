# Dataset for AI-Based Early Skin Disease Prediction

This project uses image data organized by disease class. The model expects:

```
dataset/
├── Eczema/
├── Melanoma/
├── Psoriasis/
├── Vitiligo/
└── Warts Molluscum/
```

Images: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`. Training uses 80% train / 20% validation.

---

## Add More Dataset (3 ways)

### 1. Download from Kaggle (more images from internet)

1. Install Kaggle and add your API key:
   - `pip install kaggle`
   - From [Kaggle Account → Create New Token](https://www.kaggle.com/settings), save `kaggle.json` to `C:\Users\<you>\.kaggle\` (Windows) or `~/.kaggle/` (Linux/Mac).

2. Run (replace with any skin-disease dataset slug):
   ```bash
   python scripts/download_dataset.py muhammadabdulsami/massive-skin-disease-balanced-dataset
   ```
   Or:
   ```bash
   python scripts/download_dataset.py ascanipek/skin-diseases
   ```
   The script downloads the zip, extracts it, and copies images into `dataset/<ClassName>/` by matching folder names (e.g. eczema → Eczema, melanoma → Melanoma).

3. If you already downloaded a zip manually:
   ```bash
   python scripts/download_dataset.py data_download/skin-diseases.zip
   ```
   Or point to an extracted folder:
   ```bash
   python scripts/download_dataset.py data_download/skin-diseases
   ```

### 2. Augment existing images (no download)

Generates extra training images by flipping, rotating, and changing brightness. Good for small classes (e.g. Vitiligo).

```bash
python scripts/augment_dataset.py
```

- By default, adds images until each class has at least **500** images (only classes below that get new images).
- Options:
  ```bash
  python scripts/augment_dataset.py --per-class 1000
  python scripts/augment_dataset.py --dry-run   # show what would be added, no write
  ```

### 3. Manual

- Drop images into the correct class folder, e.g. `dataset/Vitiligo/new1.jpg`.

---

## After Adding Data

Retrain so the model uses the new images:

```bash
python train_model.py
```

---

## More data sources

| Source | Link | Notes |
|--------|------|--------|
| Kaggle – Skin diseases | [ascanipek/skin-diseases](https://www.kaggle.com/datasets/ascanipek/skin-diseases) | Multiple conditions |
| Kaggle – Massive skin disease balanced | [muhammadabdulsami/...](https://www.kaggle.com/datasets/muhammadabdulsami/massive-skin-disease-balanced-dataset) | Balanced classes |
| Mendeley – Skin disease classification | [3hckgznc67](https://data.mendeley.com/datasets/3hckgznc67/1) | 5 categories, download and map folders to our class names |
| Mendeley – Skin diseases and cancer | [xr8fw85n65](https://data.mendeley.com/datasets/xr8fw85n65) | 57 conditions, includes eczema, psoriasis, melanoma |
| ISIC Archive | [opendata.aws/isic-archive](https://registry.opendata.aws/isic-archive/) | Lesion images, use for Melanoma etc. |
| Hugging Face – DermNet | [WahajRaza/Dermnet](https://huggingface.co/datasets/WahajRaza/Dermnet) | 23 classes; download and copy into our folder names |

If you add a **new class** (e.g. Fungal), create `dataset/Fungal/`, put images there, and retrain; `class_names.json` will update automatically.
