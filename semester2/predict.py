# predict_skin_cancer.py
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load model
model = load_model("skin_cancer_cnn.h5")  # Path to saved model

def predict_skin_cancer(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    class_label = "Malignant" if prediction > 0.5 else "Benign"

    plt.imshow(img)
    plt.title(f"Predicted: {class_label}")
    plt.axis("off")
    plt.show()

# Example usage
# predict_skin_cancer("example.jpg")  # Uncomment and replace with image path
