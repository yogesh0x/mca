import os
from pathlib import Path

import numpy as np
import tensorflow as tf
import uvicorn
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.applications.efficientnet import preprocess_input

# ----------------------------
# CONFIG (UNIVERSAL PATHS)
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent
DEFAULT_MODELS_DIR = BASE_DIR / "models"
DEFAULT_MODELS_DIR.mkdir(parents=True, exist_ok=True)

MODEL_PATH = Path(
    os.getenv("MODEL_PATH", str(DEFAULT_MODELS_DIR / "efficientnetb2_80plus.keras"))
)
IMG_SIZE = (260, 260)

# ----------------------------
# LOAD MODEL
# ----------------------------
print("Loading model...")
if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Model not found at: {MODEL_PATH}\n"
        f"Set MODEL_PATH env var or place model at: {DEFAULT_MODELS_DIR / 'efficientnetb2_80plus.keras'}"
    )

model = tf.keras.models.load_model(str(MODEL_PATH))
print(f"Model loaded from: {MODEL_PATH}")

class_names = [
    "actinic_keratosis",
    "basal_cell_carcinoma",
    "dermatofibroma",
    "melanoma",
    "nevus",
    "pigmented_benign_keratosis",
    "seborrheic_keratosis",
    "squamous_cell_carcinoma",
    "vascular_lesion"
]

app = FastAPI(title="Skin Lesion Classifier API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# PREPROCESSING
# ----------------------------
def preprocess_image(image_bytes: bytes) -> tf.Tensor:
    img = tf.io.decode_image(image_bytes, channels=3, expand_animations=False)
    img.set_shape([None, None, 3])  # static shape
    img = tf.image.resize(img, IMG_SIZE)
    img = tf.cast(img, tf.float32)
    img = preprocess_input(img)     # EfficientNet normalization
    img = tf.expand_dims(img, axis=0)
    return img

# ----------------------------
# ROUTES
# ----------------------------
@app.get("/health")
def health():
    return {"status": "ok", "model_path": str(MODEL_PATH)}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Uploaded file must be an image.")

    try:
        image_bytes = await file.read()
        img = preprocess_image(image_bytes)

        preds = model.predict(img, verbose=0)
        class_id = int(np.argmax(preds))
        confidence = float(np.max(preds) * 100)

        return {
            "prediction": class_names[class_id],
            "confidence": f"{confidence:.2f}%"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

# ----------------------------
# START SERVER
# ----------------------------
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False)
