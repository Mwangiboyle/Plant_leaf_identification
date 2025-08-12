import uvicorn
from fastapi import FastAPI, File, UploadFile
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io

# Label mapping
label_map = {
    0: "bosement bamboo",
    1: "Chinese horse chestnut",
    2: "Anhui Barberry",
    3: "Chinese redbud",
    4: "true indigo",
    5: "Japanese maple",
    6: "Nanmu",
    7: "castor aralia",
    8: "camphor tree",
    9: "deodar",
    10: "big-fruited holly",
    11: "Japanese cheesewood",
    12: "cornelian cherry",
    13: "Japanese elm",
    14: "sweet osmanthus",
    15: "cedar of Lebanon",
    16: "ginkgo, maidenhair tree",
    17: "Crêpe myrtle, Crepe myrtle",
    18: "oleander",
    19: "podocarpus",
    20: "Japanese flowering cherry",
    21: "glossy privet",
    22: "Chinese toon",
    23: "peach",
    24: "Ford woodlotus",
    25: "bentham maple",
    26: "Bael tree",
    27: "southern magnolia",
    28: "Canadian poplar",
    29: "Chinese tulip tree",
    30: "tangerine"
}

# App instance
app = FastAPI(title="Leaf Classifier API")

# Load model once at startup
model = load_model("model/")  # path to your saved model
img_size = (256, 256)

def preprocess_image(image_bytes):
    """Preprocess uploaded image to match model input."""
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize(img_size)
    image = np.array(image) / 255.0
    return np.expand_dims(image, axis=0)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """Predict leaf class from uploaded image."""
    contents = await file.read()
    img = preprocess_image(contents)
    preds = model.predict(img)

    class_idx = int(np.argmax(preds[0]))
    class_name = label_map.get(class_idx, "Unknown")
    confidence = float(np.max(preds[0]))

    return {
        "class_index": class_idx,
        "class_name": class_name,
        "confidence": confidence
    }

@app.get("/")
async def root():
    return {"message": "Leaf Classification API is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

