import tensorflow as tf
import numpy as np
import os
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.preprocessing import image_dataset_from_directory

# ===========================
# CONFIG
# ===========================
DATASET_PATH = r"D:\Dataset-balanced\dataset"
MODEL_PATH = r"D:\Dataset-balanced\efficientnetb2_AK_SCC_OptimizedV3.keras"
IMG_SIZE = (260, 260)
BATCH_SIZE = 16

print("\n===== LOADING MODEL =====")
model = tf.keras.models.load_model(MODEL_PATH)
print("Model loaded successfully!")

# ===========================
# LOAD DATASET AS NON-SHUFFLED
# ===========================
print("\n===== LOADING DATASET =====")
ds = image_dataset_from_directory(
    DATASET_PATH,
    labels='inferred',
    image_size=IMG_SIZE,
    shuffle=False,   # ← IMPORTANT (keeps order)
    batch_size=BATCH_SIZE
)

class_names = ds.class_names
num_classes = len(class_names)

print(f"Classes detected ({num_classes}): {class_names}")

# ===========================
# COLLECT y_true AND X
# ===========================
print("\nExtracting dataset into arrays...")

X_list = []
y_list = []

for batch_images, batch_labels in ds:
    X_list.append(batch_images)
    y_list.append(batch_labels)

X = tf.concat(X_list, axis=0)
y_true = tf.concat(y_list, axis=0).numpy()

print(f"Total images: {len(X)}")
print(f"Total labels: {len(y_true)}")

# ===========================
# PREDICT ON ALL IMAGES
# ===========================
print("\n===== PREDICTING =====")
y_pred_probs = model.predict(X, batch_size=BATCH_SIZE)
y_pred = np.argmax(y_pred_probs, axis=1)

print("Predictions finished!")
print(f"Softmax sum test (first sample): {np.sum(y_pred_probs[0]):.4f}")

# ===========================
# VERIFY CLASS COUNTS
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
print(classification_report(y_true, y_pred, target_names=class_names))

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
plt.savefig("confusion_matrix.png")
plt.show()
print("Confusion matrix saved as confusion_matrix.png")

# ===========================
# SAVE MISCLASSIFIED IMAGES
# ===========================
print("\n===== SAVING MISCLASSIFIED IMAGES =====")

misclassified_dir = "misclassified"
os.makedirs(misclassified_dir, exist_ok=True)

count_mis = 0

for i in range(len(X)):
    if y_true[i] != y_pred[i]:
        img = X[i].numpy().astype("uint8")
        true_label = class_names[y_true[i]]
        pred_label = class_names[y_pred[i]]

        fname = f"{misclassified_dir}/{i}_true_{true_label}_pred_{pred_label}.jpg"
        plt.imsave(fname, img)
        count_mis += 1

print(f"Total misclassified images saved: {count_mis}")

print("\n===== VERIFICATION COMPLETE =====")
