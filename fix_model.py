import os
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.preprocessing import image_dataset_from_directory
import numpy as np

IMG_SIZE = (256, 256)
DATASET_PATH = "dataset"
MODEL_DIR = "model"
MODEL_PATH = os.path.join(MODEL_DIR, "skin_model.h5")

if not os.path.exists(MODEL_PATH):
    print("No model to fix.")
    exit(0)

# Load old model
old_model = tf.keras.models.load_model(MODEL_PATH)
old_weights = old_model.get_weights()
print("Old model outputs:", old_model.output_shape)

if old_model.output_shape[1] == 11:
    print("Model already has 11 classes.")
    exit(0)

# Load dataset to get class names
train_data = image_dataset_from_directory(
    DATASET_PATH,
    image_size=IMG_SIZE,
    batch_size=32,
)
class_names = train_data.class_names
num_classes = len(class_names)
print("New classes:", num_classes)

# Rebuild model structure
data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.2),
    layers.RandomZoom(0.2),
    layers.RandomContrast(0.2),
])
base_model = EfficientNetB0(weights=None, include_top=False, input_shape=(256, 256, 3))
model = models.Sequential([
    data_augmentation,
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(256, activation="relu", name="dense_features"),
    layers.Dropout(0.5),
    layers.Dense(num_classes, activation="softmax", name="dense_out"),
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Initialize variables
dummy = tf.zeros((1, 256, 256, 3))
model(dummy, training=False)

# Copy weights
for i in range(len(model.layers)):
    old_layer = old_model.layers[i]
    new_layer = model.layers[i]
    
    # Copy weights for everything except the last Dense layer
    if new_layer.name != "dense_out" and len(new_layer.get_weights()) > 0:
        if len(new_layer.get_weights()) == len(old_layer.get_weights()):
            new_layer.set_weights(old_layer.get_weights())

print("Loaded old weights into new 11-class model.")

# Do a very small training step (just 1 batch!) to ensure it is structurally valid 
# and has slightly better than random weights if possible, but mainly just to save it correctly.
print("Training for 1 step to finalize model...")
model.fit(train_data.take(1), epochs=1, verbose=0)

# Save the new model
model.save(MODEL_PATH)

# Save the old model as backup just in case
old_model.save(os.path.join(MODEL_DIR, "skin_model_9class.h5"))
print(f"Saved new 11-class model to {MODEL_PATH}")
