
# Semester 3 – Skin Cancer Classification (9 Classes)

This project implements a **9-class skin Cancer classification pipeline** using **TensorFlow + EfficientNetB2**, with:

- Dataset balancing via offline augmentation
- Model training and fine-tuning
- Verification (classification report + confusion matrix + misclassified samples)
- FastAPI backend for inference

---

## Classes

The classifier predicts one of the following Cancer classes:

1. actinic_keratosis  
2. basal_cell_carcinoma  
3. dermatofibroma  
4. melanoma  
5. nevus  
6. pigmented_benign_keratosis  
7. seborrheic_keratosis  
8. squamous_cell_carcinoma  
9. vascular_lesion

---

## Dataset Sources

As described in `about.txt`, the dataset is assembled from:

- HAM10000: https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000
- Additional 9-class skin dataset: https://www.kaggle.com/datasets/nodoubttome/skin-cancer9-classesisic

After merging/filtering, classes are balanced using augmentation to target approximately **500 images per class**.

---

## Project Structure

```text
semester3/
  app.py                 # FastAPI inference API
  augmentation.py        # Offline class balancing script
  train_model.py         # EfficientNetB2 training + fine-tuning
  verification.py        # Evaluation and error analysis
  about.txt              # Methodology and dataset notes
  README.md
  Results/               # Output plots/screenshots
```

---

## Setup

### 1) Create virtual environment

```bash
python -m venv .venv
```

Activate:

- Windows:
```bash
.venv\Scripts\activate
```

- macOS/Linux:
```bash
source .venv/bin/activate
```

### 2) Install dependencies

```bash
pip install tensorflow fastapi uvicorn scikit-learn matplotlib seaborn numpy
```

(Optional) Save lock file:
```bash
pip freeze > requirements.txt
```

---

## Config (Universal Paths)

Use environment variables instead of hardcoded local paths:

- `DATASET_PATH` → directory containing class folders
- `MODEL_PATH` → `.keras` trained model file
- `RESULTS_DIR` → output directory for plots/reports

### Example (Windows PowerShell)

```powershell
$env:DATASET_PATH="D:\dataset\skin9"
$env:MODEL_PATH="D:\models\efficientnetb2_80plus.keras"
$env:RESULTS_DIR="D:\outputs\results"
```

### Example (Linux/macOS)

```bash
export DATASET_PATH="/home/user/dataset/skin9"
export MODEL_PATH="/home/user/models/efficientnetb2_80plus.keras"
export RESULTS_DIR="/home/user/outputs/results"
```

If not set, scripts can default to local project-relative paths like:
- `./data/dataset`
- `./models/efficientnetb2_80plus.keras`
- `./Results`

---

## Workflow

### 1) Balance dataset (optional, if imbalanced)

```bash
python semester3/augmentation.py
```

### 2) Train model

```bash
python semester3/train_model.py
```

Best model is saved as `.keras` (via ModelCheckpoint).

### 3) Verify model performance

```bash
python semester3/verification.py
```

Generates:
- confusion matrix
- classification report output
- misclassified image samples

### 4) Run API server

```bash
python semester3/app.py
```

or:

```bash
uvicorn semester3.app:app --host 0.0.0.0 --port 8000
```

---

## API Usage

### Endpoint

`POST /predict`

### Request
Multipart form with one image file:
- field name: `file`

### Example (curl)

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@sample.jpg"
```

### Example response

```json
{
  "prediction": "melanoma",
  "confidence": "94.37%"
}
```

---

## Notes

- Trained model file (~95MB) is not committed due to GitHub size/practical limits.
- Keep trained weights in `models/` locally and provide path via `MODEL_PATH`.
- This is an academic/research project and **not a clinical diagnostic tool**.

---

## Future Improvements

- Add `requirements.txt` and pinned versions
- Add `.env` support with `python-dotenv`
- Add training history plot export (loss/accuracy curves)
- Add per-class precision/recall/F1 CSV export
- Add Dockerfile for one-command API deployment
