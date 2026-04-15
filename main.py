from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import base64
import io
from PIL import Image, ImageOps
import numpy as np
from sklearn.datasets import load_digits
from sklearn.neural_network import MLPClassifier
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for frontend interaction
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load and train the model
digits = load_digits()
X, y = digits.data, digits.target
# Normalize X to 0-1 range for better training, though digits is already small (0-16)
clf = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=1000, random_state=1)
clf.fit(X, y)

class ImageInput(BaseModel):
    image: str # base64 string

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict")
async def predict(input_data: ImageInput):
    try:
        # 1. Decode base64 image
        header, encoded = input_data.image.split(",", 1) if "," in input_data.image else ("", input_data.image)
        image_data = base64.b64decode(encoded)
        img = Image.open(io.BytesIO(image_data))

        # 2. Preprocess
        # Convert to RGBA then use alpha as mask or convert to L (grayscale)
        # If the drawing is white on transparent/black, we want white on black.
        img = img.convert("RGBA")

        # Create a black background
        background = Image.new("RGBA", img.size, (0, 0, 0, 255))
        composite = Image.alpha_composite(background, img)
        img = composite.convert("L")

        # Resize to 8x8 (matching sklearn digits dataset)
        img = img.resize((8, 8), Image.Resampling.LANCZOS)

        # sklearn digits dataset has values 0-16.
        # Our image has 0-255.
        data = np.array(img)
        data = (data / 255.0) * 16.0

        # Reshape for prediction
        data = data.reshape(1, -1)

        # 3. Predict
        prediction = int(clf.predict(data)[0])
        probabilities = clf.predict_proba(data)[0]
        confidence = float(probabilities[prediction])

        return {
            "prediction": prediction,
            "confidence": confidence,
            "all_probabilities": probabilities.tolist()
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
