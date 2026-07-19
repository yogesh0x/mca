import os
from pathlib import Path

import numpy as np
import tensorflow as tf

# --------------------------
# CONFIG (UNIVERSAL PATHS)
# --------------------------
BASE_DIR = Path(__file__).resolve().parent
DEFAULT_DATASET_DIR = BASE_DIR / "data" / "dataset"
DEFAULT_MODELS_DIR = BASE_DIR / "models"

DATASET_PATH = Path(os.getenv("DATASET_PATH", str(DEFAULT_DATASET_DIR)))
MODEL_NAME = os.getenv("MODEL_NAME", "efficientnetb2_80plus.keras")
BATCH_SIZE = int(os.getenv("BATCH_SIZE", "16"))
IMG_SIZE = (260, 260)
SEED = int(os.getenv("SEED", "42"))

DEFAULT_MODELS_DIR.mkdir(parents=True, exist_ok=True)
MODEL_SAVE_PATH = DEFAULT_MODELS_DIR / MODEL_NAME

# --------------------------
# VALIDATION
# --------------------------
if not DATASET_PATH.exists():
    raise FileNotFoundError(
        f"Dataset not found at: {DATASET_PATH}\n"
        f"Set DATASET_PATH env var or place dataset at default path."
    )

print(f"Dataset path: {DATASET_PATH}")
print(f"Model will be saved to: {MODEL_SAVE_PATH}")

# --------------------------
# DATA LOADING
# --------------------------
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    str(DATASET_PATH),
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    validation_split=0.20,
    subset="training",
    shuffle=True,
    seed=SEED
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    str(DATASET_PATH),
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    validation_split=0.20,
    subset="validation",
    shuffle=False,
    seed=SEED
)

class_names = train_ds.class_names
num_classes = len(class_names)
print("Classes:", class_names)

# --------------------------
# PREFETCH
# --------------------------
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.prefetch(AUTOTUNE)
val_ds = val_ds.prefetch(AUTOTUNE)

# --------------------------
# CLASS WEIGHTS
# --------------------------
labels_list = []
for _, labels in train_ds:
    labels_list.extend(labels.numpy())

labels_array = np.array(labels_list)
unique, counts = np.unique(labels_array, return_counts=True)
total = labels_array.shape[0]

# map by actual class index
class_weights = {int(cls_idx): float(total / (num_classes * count)) for cls_idx, count in zip(unique, counts)}
print("Class weights:", class_weights)

# --------------------------
# AUGMENTATION BLOCK
# --------------------------
data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal"),
    tf.keras.layers.RandomRotation(0.15),
    tf.keras.layers.RandomZoom(0.15),
    tf.keras.layers.RandomContrast(0.2),
], name="data_augmentation")

# --------------------------
# BASE MODEL
# --------------------------
base_model = tf.keras.applications.EfficientNetB2(
    include_top=False,
    weights="imagenet",
    pooling="avg",
    input_shape=(IMG_SIZE[0], IMG_SIZE[1], 3)
)

base_model.trainable = False  # warmup phase

# --------------------------
# FINAL CLASSIFIER
# --------------------------
inputs = tf.keras.Input(shape=(IMG_SIZE[0], IMG_SIZE[1], 3))
x = data_augmentation(inputs)
x = tf.keras.applications.efficientnet.preprocess_input(x)
x = base_model(x)
x = tf.keras.layers.Dropout(0.45)(x)
x = tf.keras.layers.Dense(512, activation="relu")(x)
x = tf.keras.layers.Dropout(0.3)(x)
x = tf.keras.layers.Dense(256, activation="relu")(x)
x = tf.keras.layers.Dropout(0.2)(x)
outputs = tf.keras.layers.Dense(num_classes, activation="softmax")(x)

model = tf.keras.Model(inputs, outputs)

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# --------------------------
# CALLBACKS
# --------------------------
callbacks = [
    tf.keras.callbacks.ModelCheckpoint(
        filepath=str(MODEL_SAVE_PATH),
        monitor="val_accuracy",
        save_best_only=True
    ),
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor="val_loss",
        factor=0.3,
        patience=3,
        min_lr=1e-6
    ),
    tf.keras.callbacks.EarlyStopping(
        monitor="val_accuracy",
        patience=7,
        restore_best_weights=True
    )
]

# --------------------------
# STEP 1 — WARMUP TRAINING
# --------------------------
print("\n===== WARMUP TRAINING (freeze model) =====\n")
model.fit(
    train_ds,
    epochs=5,
    validation_data=val_ds,
    class_weight=class_weights
)

# --------------------------
# STEP 2 — UNFREEZE FOR FINE-TUNING
# --------------------------
print("\n===== UNFREEZING LAST 120 LAYERS =====\n")
base_model.trainable = True
for layer in base_model.layers[:-120]:
    layer.trainable = False

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=5e-5),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# --------------------------
# STEP 3 — FULL TRAINING
# --------------------------
model.fit(
    train_ds,
    epochs=40,
    validation_data=val_ds,
    class_weight=class_weights,
    callbacks=callbacks
)

print(f"\nTraining finished! Best model saved at: {MODEL_SAVE_PATH}")
