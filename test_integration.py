import requests
import base64
from PIL import Image, ImageDraw
import io

def test_health():
    response = requests.get("http://localhost:8000/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_predict_digit():
    # Create a '1'
    img = Image.new('RGB', (480, 480), color='black')
    draw = ImageDraw.Draw(img)
    draw.line([(240, 50), (240, 430)], fill='white', width=40)

    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    response = requests.post("http://localhost:8000/predict", json={"image": f"data:image/png;base64,{img_str}"})
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert "confidence" in data
    print(f"Predicted: {data['prediction']} with confidence {data['confidence']}")

if __name__ == "__main__":
    test_health()
    test_predict_digit()
    print("All tests passed!")
