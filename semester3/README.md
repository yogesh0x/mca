# Skin Cancer Classification (9 Classes) – Semester 3

This project builds an end-to-end **Skin Cancer Classification** pipeline using deep learning (**EfficientNetB2 + TensorFlow**), from dataset preparation to model serving via **FastAPI**.

It is designed for local execution, where users download two public datasets, merge class folders, balance class counts, train the model, verify performance, and run inference API.

---

## Project Objective

Classify dermoscopic skin images into **9 skin cancer-related classes**:

1. `actinic_keratosis`
2. `basal_cell_carcinoma`
3. `dermatofibroma`
4. `melanoma`
5. `nevus`
6. `pigmented_benign_keratosis`
7. `seborrheic_keratosis`
8. `squamous_cell_carcinoma`
9. `vascular_lesion`

---

## Dataset Sources

Download these datasets locally:

- HAM10000:  
  https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000
- ISIC-style 9-class dataset:  
  https://www.kaggle.com/datasets/nodoubttome/skin-cancer9-classesisic

You must manually **merge and organize** the images into a single folder structure (shown below).

---

## Required Dataset Structure

Your local dataset must be arranged as:

```text
dataset/
  actinic_keratosis/
  basal_cell_carcinoma/
  dermatofibroma/
  melanoma/
  nevus/
  pigmented_benign_keratosis/
  seborrheic_keratosis/
  squamous_cell_carcinoma/
  vascular_lesion/
```

> In short: `dataset/class1/class2/...` is not valid.  
> It must be **one root dataset folder** with **9 class subfolders**, and each class folder contains images.

---

## Repository Structure

```text
semester3/
  app.py                 # FastAPI inference API
  augmentation.py        # Augments minority classes to target count
  train_model.py         # Training + fine-tuning (EfficientNetB2)
  verification.py        # Evaluation (report + confusion matrix + errors)
  about.txt              # Dataset/workflow explanation
  requirements.txt
  .env
  Results/               # Saved plots/screenshots
  models/                # (local) trained model file goes here
```

---

## Setup Instructions

## 1) Clone repository

```bash
git clone https://github.com/yogesh0x/mca.git
cd mca/semester3
```

## 2) Create and activate virtual environment

### Windows (PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Linux/macOS
```bash
python -m venv .venv
source .venv/bin/activate
```

## 3) Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Update `.env` in `semester3/`:

```env
DATASET_PATH=./data/dataset
MODEL_PATH=./models/efficientnetb2_80plus.keras
RESULTS_DIR=./Results
BATCH_SIZE=16
TARGET_COUNT=500
MODEL_NAME=efficientnetb2_80plus.keras
SEED=42
```

### Important
- `DATASET_PATH` must point to the merged folder containing all 9 class subfolders.
- Trained model file is not committed due to size (~95MB), so you must train locally or provide your own model file path.

---

## Complete Workflow (Run Order)

## Step 1: Prepare & merge datasets locally
- Download both datasets
- Merge into one root folder with 9 class directories
- Ensure class names match expected labels

## Step 2: Balance classes using augmentation
```bash
python augmentation.py
```
This expands lower-count classes up to `TARGET_COUNT` (default 500).

## Step 3: Train model
```bash
python train_model.py
```
- Uses `image_dataset_from_directory`
- 80/20 training-validation split
- Warmup + fine-tuning strategy
- Saves best model to `MODEL_PATH` (or `models/` default)

## Step 4: Verify model performance
```bash
python verification.py
```
Outputs:
- classification report
- confusion matrix image
- misclassified sample images

## Step 5: Run inference API
```bash
python app.py
```
or
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

---

## API Usage

### Health Check
`GET /health`

### Prediction Endpoint
`POST /predict` with form-data image file (`file`)

### Example cURL
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "accept: application/json" \
  -F "file=@sample.jpg"
```

### Example Response
```json
{
  "prediction": "melanoma",
  "confidence": "94.37%"
}
```

---

## Notes for Contributors / Users

- This project is educational/research-oriented.
- It is **not** a certified medical diagnostic system.
- If class names differ in your downloaded dataset, rename folders to match expected class labels before training.
- Keep large model files in local `models/` folder (or external storage), not in Git commit history.

---

## Recommended Next Improvements

- Add `class_names.json` export during training and load it in API (to avoid hardcoded class order mismatch)
- Save evaluation metrics as CSV/JSON in addition to plots
- Add Docker support for one-command deployment
- Add Grad-CAM explainability for medical image interpretation

---

## Author Context

This project was developed as part of MCA Semester 3 coursework focused on practical deep learning and deployment workflow for skin cancer image classification.
