import uvicorn
import numpy as np
import tensorflow as tf
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.applications.efficientnet import preprocess_input

MODEL_PATH = r"D:\MCA\minor3\efficientnetb2_80plus.keras"
IMG_SIZE = (260, 260)

# Load model
print("Loading model...")
model = tf.keras.models.load_model(MODEL_PATH)
print("Model loaded.")

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

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ----------------------------
# CORRECT PREPROCESSING
# ----------------------------
def preprocess_image(image_bytes):
    img = tf.io.decode_image(image_bytes, channels=3, expand_animations=False)

    # FIX: enforce static shape (VERY IMPORTANT)
    img.set_shape([None, None, 3])

    img = tf.image.resize(img, IMG_SIZE)
    img = tf.cast(img, tf.float32)
    img = preprocess_input(img)   # EfficientNet normalization
    img = tf.expand_dims(img, axis=0)
    return img


# ----------------------------
# PREDICT ENDPOINT
# ----------------------------
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        img = preprocess_image(image_bytes)

        preds = model.predict(img)
        class_id = int(np.argmax(preds))
        confidence = float(np.max(preds) * 100)

        return {
            "prediction": class_names[class_id],
            "confidence": f"{confidence:.2f}%"
        }

    except Exception as e:
        return {"error": str(e)}


# ----------------------------
# START SERVER
# ----------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
