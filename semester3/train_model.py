import tensorflow as tf
import numpy as np
import os

# --------------------------
# PATH TO YOUR DATASET
# --------------------------
DATASET_PATH = r"D:\Dataset-balanced\dataset"

# --------------------------
# DATA LOADING
# --------------------------
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    DATASET_PATH,
    image_size=(260, 260),  # EfficientNetB2 native size
    batch_size=16,          # CPU-safe batch size
    validation_split=0.20,
    subset="training",
    shuffle=True,
    seed=42
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    DATASET_PATH,
    image_size=(260, 260),
    batch_size=16,
    validation_split=0.20,
    subset="validation",
    shuffle=False,
    seed=42
)

class_names = train_ds.class_names
num_classes = len(class_names)
print("Classes:", class_names)

# --------------------------
# PREFETCH FOR CPU SPEED
# --------------------------
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.prefetch(AUTOTUNE)
val_ds = val_ds.prefetch(AUTOTUNE)

# --------------------------
# CALCULATE CLASS WEIGHTS
# --------------------------
labels_list = []
for images, labels in train_ds:
    labels_list.extend(labels.numpy())

labels_array = np.array(labels_list)

unique, counts = np.unique(labels_array, return_counts=True)
total = labels_array.shape[0]
class_weights = {i: total/(num_classes * counts[i]) for i in range(num_classes)}

print("Class weights:", class_weights)

# --------------------------
# DATA AUGMENTATION BLOCK
# --------------------------
data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal"),
    tf.keras.layers.RandomRotation(0.15),
    tf.keras.layers.RandomZoom(0.15),
    tf.keras.layers.RandomContrast(0.2),
])

# --------------------------
# BASE MODEL: EfficientNetB2
# --------------------------
base_model = tf.keras.applications.EfficientNetB2(
    include_top=False,
    weights="imagenet",
    pooling="avg",
    input_shape=(260, 260, 3)
)

base_model.trainable = False  # WARMUP first

# --------------------------
# FINAL CLASSIFIER
# --------------------------
inputs = tf.keras.Input(shape=(260, 260, 3))
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
        "efficientnetb2_80plus.keras",
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
history = model.fit(
    train_ds,
    epochs=5,
    validation_data=val_ds,
    class_weight=class_weights
)

# --------------------------
# STEP 2 — UNFREEZE FOR HIGH ACCURACY
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
history2 = model.fit(
    train_ds,
    epochs=40,
    validation_data=val_ds,
    class_weight=class_weights,
    callbacks=callbacks
)

print("\nTraining Finished! Model saved as efficientnetb2_80plus.keras")


