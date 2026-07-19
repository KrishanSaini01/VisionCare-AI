import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model only once
MODEL_PATH = os.path.join(os.path.dirname(__file__), "cnn_model.keras")
model = load_model(MODEL_PATH)

# Class labels
CLASS_NAMES = {
    0: "NORMAL",
    1: "PNEUMONIA"
}

IMG_SIZE = (224, 224)


def preprocess_image(image_path):
    """
    Read and preprocess an image for prediction.
    """

    img = cv2.imread(image_path)

    if img is None:
        raise ValueError(f"Unable to read image: {image_path}")

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, IMG_SIZE)
    img = img.astype("float32") / 255.0

    img = np.expand_dims(img, axis=0)

    return img


def predict_image(image_path):
    """
    Predict NORMAL or PNEUMONIA from an X-ray image.
    """

    image = preprocess_image(image_path)

    prediction = model.predict(image, verbose=0)[0][0]

    if prediction >= 0.5:
        disease = CLASS_NAMES[1]
        confidence = float(prediction * 100)
    else:
        disease = CLASS_NAMES[0]
        confidence = float((1 - prediction) * 100)

    return {
        "disease": disease,
        "confidence": round(confidence, 2)
    }


# Run only for testing
if __name__ == "__main__":

    image_path = "../dataset/test/NORMAL/IM-0001-0001.jpeg"   # Change to an existing image

    result = predict_image(image_path)

    print("Prediction :", result["disease"])
    print("Confidence :", result["confidence"], "%")