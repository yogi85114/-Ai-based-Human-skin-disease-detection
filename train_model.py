"""
Train skin disease classifier on 11-class dataset.
Dataset folders: Acne, Eczema, Infestations_Bites, Lupus, Melanoma,
                 Psoriasis, Rosacea, Tinea, Unknown_Normal, Vitiligo, Warts Molluscum

Target: 70-80% validation accuracy.
Saves: model/skin_model.h5, model/class_names.json, model/metrics.json
"""
import json
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
from sklearn.utils.class_weight import compute_class_weight

# -----------------------------
# SETTINGS
# -----------------------------
IMG_SIZE = (256, 256)
BATCH_SIZE = 32
DATASET_PATH = "dataset"
MODEL_DIR = "model"
os.makedirs(MODEL_DIR, exist_ok=True)

# -----------------------------
# LOAD DATASET
# -----------------------------
train_data = image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
)

val_data = image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
)

class_names = train_data.class_names
num_classes = len(class_names)
print("Classes:", class_names)
print("Number of classes:", num_classes)

AUTOTUNE = tf.data.AUTOTUNE
train_data = train_data.prefetch(buffer_size=AUTOTUNE)
val_data = val_data.prefetch(buffer_size=AUTOTUNE)

# -----------------------------
# CLASS WEIGHTS
# -----------------------------
temp_train = image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
)
labels = np.concatenate([y.numpy() for _, y in temp_train], axis=0)
class_weights = compute_class_weight(
    class_weight="balanced",
    classes=np.unique(labels),
    y=labels,
)
class_weights_dict = {i: float(class_weights[i]) for i in range(len(class_weights))}
print("Class weights:", class_weights_dict)

# -----------------------------
# AUGMENTATION + MODEL
# -----------------------------
data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.2),
    layers.RandomZoom(0.2),
    layers.RandomContrast(0.2),
])

base_model = EfficientNetB0(
    weights="imagenet",
    include_top=False,
    input_shape=(256, 256, 3),
)
base_model.trainable = False

model = models.Sequential([
    data_augmentation,
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(256, activation="relu"),
    layers.Dropout(0.5),
    layers.Dense(num_classes, activation="softmax"),
])

# -----------------------------
# PHASE 1: Train head
# -----------------------------
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)
ckpt_path = os.path.join(MODEL_DIR, "best_weights.weights.h5")

print("\n[Phase 1] Training head (8 epochs)...\n")
model.fit(
    train_data,
    validation_data=val_data,
    epochs=8,
    class_weight=class_weights_dict,
)

# -----------------------------
# PHASE 2: Fine-tune
# -----------------------------
base_model.trainable = True
for layer in base_model.layers[:100]:
    layer.trainable = False

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-5),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

callbacks = [
    ModelCheckpoint(
        ckpt_path,
        monitor="val_accuracy",
        save_best_only=True,
        save_weights_only=True,
        mode="max",
        verbose=1,
    ),
    EarlyStopping(
        monitor="val_accuracy",
        patience=6,
        restore_best_weights=True,
        verbose=1,
    ),
    ReduceLROnPlateau(
        monitor="val_loss",
        factor=0.5,
        patience=3,
        min_lr=1e-7,
        verbose=1,
    ),
]

print("\n[Phase 2] Fine-tuning (max 25 epochs, target val accuracy 70-80%)...\n")
history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=25,
    callbacks=callbacks,
    class_weight=class_weights_dict,
)

# -----------------------------
# Load best weights, evaluate, save
# -----------------------------
if os.path.exists(ckpt_path):
    model.load_weights(ckpt_path)
    print("Loaded best checkpoint weights.")

results = model.evaluate(val_data)
val_loss = float(results[0])
val_accuracy = float(results[1])
val_accuracy_pct = round(val_accuracy * 100, 2)

print("\n" + "=" * 50)
print("FINAL VALIDATION ACCURACY: {}%".format(val_accuracy_pct))
print("Target range: 70-80%")
print("=" * 50 + "\n")

# Save full model
model_path = os.path.join(MODEL_DIR, "skin_model.h5")
model.save(model_path)
print(f"Model saved to {model_path} ({os.path.getsize(model_path):,} bytes)")

# Save class names (from actual dataset)
safe_class_names = [str(c) for c in class_names]
with open(os.path.join(MODEL_DIR, "class_names.json"), "w") as f:
    json.dump(safe_class_names, f, indent=2)
print("class_names.json saved:", safe_class_names)

# Save metrics
metrics = {
    "validation_accuracy": float(val_accuracy),
    "validation_accuracy_percent": float(val_accuracy_pct),
    "validation_loss": float(val_loss),
    "target_accuracy_range": "70-80%",
    "classes": safe_class_names,
    "num_classes": len(safe_class_names),
}
with open(os.path.join(MODEL_DIR, "metrics.json"), "w") as f:
    json.dump(metrics, f, indent=2)

print("Saved: model/skin_model.h5, model/class_names.json, model/metrics.json")
print("Training completed. Ready for submission.")
