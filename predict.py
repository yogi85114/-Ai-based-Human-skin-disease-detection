"""
predict.py - Model inference for skin disease chatbot.
Fixed: PIL.UnidentifiedImageError on Windows by loading image via PIL directly.
"""
import json
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import EfficientNetB0
from PIL import Image as PILImage
import h5py

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model", "skin_model.h5")
WEIGHTS_PATH = os.path.join(os.path.dirname(__file__), "model", "best_weights.weights.h5")
CLASS_NAMES_PATH = os.path.join(os.path.dirname(__file__), "model", "class_names.json")

IMG_SIZE = (256, 256)

_model = None  # Cache for the loaded model


def _build_sequential_model(num_classes):
    data_augmentation = tf.keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.2),
        layers.RandomZoom(0.2),
        layers.RandomContrast(0.2),
    ])
    base_model = EfficientNetB0(
        weights=None,
        include_top=False,
        input_shape=(256, 256, 3),
    )
    model = models.Sequential([
        data_augmentation,
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(256, activation="relu"),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ])
    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    dummy = tf.zeros((1, 256, 256, 3))
    model(dummy, training=False)
    return model


def _load_weights_manual(model, weights_path):
    h5_weights = {}
    with h5py.File(weights_path, "r") as f:
        def _collect(name, obj):
            if hasattr(obj, "shape"):
                h5_weights[name] = obj[()]
        f.visititems(_collect)

    loaded, skipped = 0, 0
    for var in model.variables:
        vname = var.name
        top_key = vname.split("/")[0]
        candidates = [
            f"efficientnetb0/{vname}",
            f"{top_key}/{vname}",
            vname,
        ]
        found = False
        for key in candidates:
            if key in h5_weights:
                arr = h5_weights[key]
                if arr.shape == tuple(var.shape):
                    var.assign(arr)
                    loaded += 1
                    found = True
                    break
        if not found:
            skipped += 1
    print(f"[predict] Checkpoint — loaded: {loaded}, skipped: {skipped}")


def _load_model():
    global _model
    if _model is not None:
        return _model

    if os.path.exists(MODEL_PATH) and os.path.getsize(MODEL_PATH) >= 50_000:
        try:
            _model = tf.keras.models.load_model(MODEL_PATH)
            print(f"[predict] Loaded full model: {MODEL_PATH}")
            return _model
        except Exception as e:
            print(f"[predict] .h5 load failed ({e}), falling back to weights.")

    if os.path.exists(WEIGHTS_PATH):
        print(f"[predict] Rebuilding architecture and loading {WEIGHTS_PATH}...")
        names = _load_class_names()
        model = _build_sequential_model(len(names))
        _load_weights_manual(model, WEIGHTS_PATH)
        _model = model
        return _model

    raise RuntimeError(f"No model found at '{MODEL_PATH}' or '{WEIGHTS_PATH}'.")


def _load_class_names():
    if os.path.exists(CLASS_NAMES_PATH):
        with open(CLASS_NAMES_PATH, "r") as f:
            return json.load(f)
    return [
        "Acne", "Eczema", "Infestations_Bites", "Lupus", "Melanoma",
        "Psoriasis", "Rosacea", "Tinea", "Unknown_Normal", "Vitiligo", "Warts Molluscum",
    ]


class_names = _load_class_names()


def predict_disease(img_path):
    """Predict disease from image file."""
    model = _load_model()
    tf.debugging.disable_traceback_filtering()

    # ✅ FIX: Load image via PIL directly (bypasses Keras Windows path bug)
    img_path = os.path.abspath(img_path)
    with PILImage.open(img_path) as pil_img:
        pil_img = pil_img.convert("RGB")
        pil_img = pil_img.resize(IMG_SIZE, PILImage.LANCZOS)
        img_array = np.array(pil_img, dtype=np.float32)

    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array, verbose=0)[0]
    predicted_index = int(np.argmax(predictions))
    conf = round(100 * float(predictions[predicted_index]), 2)

    probs = {
        class_names[i]: round(100 * float(predictions[i]), 2)
        for i in range(len(class_names))
    }
    return class_names[predicted_index], conf, probs
