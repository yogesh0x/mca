import os
import random
import shutil
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
import numpy as np

# -------- CONFIG --------
DATASET_DIR = r"D:\Dataset - Copy"   # <-- change this
TARGET_COUNT = 500                # augment until each class has 500 images

# Strong but safe augmentation
datagen = ImageDataGenerator(
    rotation_range=25,
    width_shift_range=0.15,
    height_shift_range=0.15,
    shear_range=0.10,
    zoom_range=0.20,
    horizontal_flip=True,
    fill_mode="nearest"
)

def count_images(folder):
    return len([f for f in os.listdir(folder) if f.lower().endswith(('.jpg','.png','.jpeg'))])

def augment_class(folder):
    images = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg','.png','.jpeg'))]
    current = len(images)

    if current >= TARGET_COUNT:
        print(f"✔ {folder}: Already {current} images, skipping...")
        return

    print(f"\n🔧 Augmenting class: {folder}")
    print(f"   Current: {current}, Target: {TARGET_COUNT}")

    needed = TARGET_COUNT - current
    per_image = max(1, needed // current)    # distribute equally
    print(f"   ➜ Each image will generate approx {per_image} augmented images.")

    generated = 0

    # Loop continuously until total images reach TARGET_COUNT
    while count_images(folder) < TARGET_COUNT:
        for img_name in images:
            if count_images(folder) >= TARGET_COUNT:
                break

            img_path = os.path.join(folder, img_name)
            img = load_img(img_path)
            x = img_to_array(img)
            x = np.expand_dims(x, axis=0)

            # Generate 'per_image' augmentations for this image
            i = 0
            for batch in datagen.flow(x, batch_size=1,
                                      save_to_dir=folder,
                                      save_prefix="aug",
                                      save_format="jpg"):
                i += 1
                generated += 1
                if i >= per_image or count_images(folder) >= TARGET_COUNT:
                    break

    print(f"   ✔ Completed: Final Count = {count_images(folder)}")


# -------- MAIN --------
for cls in os.listdir(DATASET_DIR):
    class_folder = os.path.join(DATASET_DIR, cls)
    if os.path.isdir(class_folder):
        augment_class(class_folder)

print("\n🎉 BALANCED AUGMENTATION COMPLETED SUCCESSFULLY!")
