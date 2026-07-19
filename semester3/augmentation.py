import os
from pathlib import Path

import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img

# ----------------------------
# CONFIG (UNIVERSAL PATHS)
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent
DEFAULT_DATASET_DIR = BASE_DIR / "data" / "dataset"

DATASET_DIR = Path(os.getenv("DATASET_PATH", str(DEFAULT_DATASET_DIR)))
TARGET_COUNT = int(os.getenv("TARGET_COUNT", "500"))

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

VALID_EXTS = (".jpg", ".jpeg", ".png")


def count_images(folder: Path) -> int:
    return len([f for f in folder.iterdir() if f.is_file() and f.suffix.lower() in VALID_EXTS])


def augment_class(folder: Path):
    images = [f for f in folder.iterdir() if f.is_file() and f.suffix.lower() in VALID_EXTS]
    current = len(images)

    if current == 0:
        print(f"⚠ {folder.name}: No images found, skipping...")
        return

    if current >= TARGET_COUNT:
        print(f"✔ {folder.name}: Already {current} images, skipping...")
        return

    print(f"\n🔧 Augmenting class: {folder.name}")
    print(f"   Current: {current}, Target: {TARGET_COUNT}")

    needed = TARGET_COUNT - current
    per_image = max(1, needed // current)
    print(f"   ➜ Each image will generate approx {per_image} augmented images.")

    while count_images(folder) < TARGET_COUNT:
        for img_path in images:
            if count_images(folder) >= TARGET_COUNT:
                break

            img = load_img(str(img_path))
            x = img_to_array(img)
            x = np.expand_dims(x, axis=0)

            i = 0
            for _ in datagen.flow(
                x,
                batch_size=1,
                save_to_dir=str(folder),
                save_prefix="aug",
                save_format="jpg"
            ):
                i += 1
                if i >= per_image or count_images(folder) >= TARGET_COUNT:
                    break

    print(f"   ✔ Completed: Final Count = {count_images(folder)}")


def main():
    print(f"Using dataset dir: {DATASET_DIR}")
    print(f"Target count/class: {TARGET_COUNT}")

    if not DATASET_DIR.exists():
        raise FileNotFoundError(
            f"Dataset directory not found: {DATASET_DIR}\n"
            f"Set DATASET_PATH env var or create the default path."
        )

    class_dirs = [p for p in DATASET_DIR.iterdir() if p.is_dir()]
    if not class_dirs:
        raise ValueError(f"No class folders found in: {DATASET_DIR}")

    for class_folder in class_dirs:
        augment_class(class_folder)

    print("\n🎉 BALANCED AUGMENTATION COMPLETED SUCCESSFULLY!")


if __name__ == "__main__":
    main()
