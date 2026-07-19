import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix
from tensorflow.keras.preprocessing import image_dataset_from_directory

# ===========================
# CONFIG (UNIVERSAL PATHS)
# ===========================
BASE_DIR = Path(__file__).resolve().parent
DEFAULT_DATASET_DIR = BASE_DIR / "data" / "dataset"
DEFAULT_MODELS_DIR = BASE_DIR / "models"
DEFAULT_RESULTS_DIR = BASE_DIR / "Results"

DATASET_PATH = Path(os.getenv("DATASET_PATH", str(DEFAULT_DATASET_DIR)))
MODEL_PATH = Path(os.getenv("MODEL_PATH", str(DEFAULT_MODELS_DIR / "efficientnetb2_80plus.keras")))
RESULTS_DIR = Path(os.getenv("RESULTS_DIR", str(DEFAULT_RESULTS_DIR)))

IMG_SIZE = (260, 260)
BATCH_SIZE = int(os.getenv("BATCH_SIZE", "16"))

RESULTS_DIR.mkdir(parents=True, exist_ok=True)

if not DATASET_PATH.exists():
    raise FileNotFoundError(f"Dataset path not found: {DATASET_PATH}")
if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model path not found: {MODEL_PATH}")

print("\n===== LOADING MODEL =====")
model = tf.keras.models.load_model(str(MODEL_PATH))
print(f"Model loaded successfully from: {MODEL_PATH}")

# ===========================
# LOAD DATASET AS NON-SHUFFLED
# ===========================
print("\n===== LOADING DATASET =====")
ds = image_dataset_from_directory(
    str(DATASET_PATH),
    labels="inferred",
    image_size=IMG_SIZE,
    shuffle=False,   # keep order for misclassification mapping
    batch_size=BATCH_SIZE
)

class_names = ds.class_names
num_classes = len(class_names)
print(f"Classes detected ({num_classes}): {class_names}")

# ===========================
# COLLECT y_true AND X
# ===========================
print("\nExtracting dataset into arrays...")

X_list, y_list = [], []
for batch_images, batch_labels in ds:
    X_list.append(batch_images)
    y_list.append(batch_labels)

X = tf.concat(X_list, axis=0)
y_true = tf.concat(y_list, axis=0).numpy()

print(f"Total images: {len(X)}")
print(f"Total labels: {len(y_true)}")

# ===========================
# PREDICT
# ===========================
print("\n===== PREDICTING =====")
y_pred_probs = model.predict(X, batch_size=BATCH_SIZE, verbose=1)
y_pred = np.argmax(y_pred_probs, axis=1)

print("Predictions finished!")
print(f"Softmax sum test (first sample): {np.sum(y_pred_probs[0]):.4f}")

# ===========================
# CLASS COUNT CHECK
# ===========================
print("\n===== CLASS COUNT CHECK =====")
unique_true = np.unique(y_true)
unique_pred = np.unique(y_pred)

print("Classes present in TRUE labels:", unique_true)
print("Classes present in PRED labels:", unique_pred)

if len(unique_pred) != num_classes:
    print("⚠ WARNING: Some classes not predicted!")
else:
    print("✔ All classes predicted at least once.")

# ===========================
# CLASSIFICATION REPORT
# ===========================
print("\n===== CLASSIFICATION REPORT =====")
report_text = classification_report(y_true, y_pred, target_names=class_names)
print(report_text)

report_path = RESULTS_DIR / "classification_report.txt"
with open(report_path, "w", encoding="utf-8") as f:
    f.write(report_text)
print(f"Classification report saved to: {report_path}")

# ===========================
# CONFUSION MATRIX
# ===========================
print("\n===== CONFUSION MATRIX =====")
cm = confusion_matrix(y_true, y_pred)

plt.figure(figsize=(12, 10))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=class_names, yticklabels=class_names)
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title("Confusion Matrix")
plt.tight_layout()

cm_path = RESULTS_DIR / "confusion_matrix.png"
plt.savefig(str(cm_path), dpi=200)
plt.show()
print(f"Confusion matrix saved as: {cm_path}")

# ===========================
# SAVE MISCLASSIFIED IMAGES
# ===========================
print("\n===== SAVING MISCLASSIFIED IMAGES =====")

misclassified_dir = RESULTS_DIR / "misclassified"
misclassified_dir.mkdir(parents=True, exist_ok=True)

count_mis = 0
for i in range(len(X)):
    if y_true[i] != y_pred[i]:
        img = X[i].numpy().astype("uint8")
        true_label = class_names[y_true[i]]
        pred_label = class_names[y_pred[i]]

        fname = misclassified_dir / f"{i}_true_{true_label}_pred_{pred_label}.jpg"
        plt.imsave(str(fname), img)
        count_mis += 1

print(f"Total misclassified images saved: {count_mis}")
print("\n===== VERIFICATION COMPLETE =====")
