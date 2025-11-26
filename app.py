from flask import Flask, request, jsonify
from transformers import pipeline
from PIL import Image
from flask_cors import CORS
import io

app = Flask(__name__)
CORS(app)

# Load classifier
classifier = pipeline("image-classification", model="microsoft/resnet-50")

# Fruit calorie table
fruit_calories = {
    "apple": 52,
    "granny smith": 52,
    "red apple": 52,
    "banana": 96,
    "orange": 47,
    "lemon": 29,
    "lime": 30,
    "pineapple": 50,
    "mango": 60,
    "grapes": 69,
    "strawberry": 33,
    "blueberry": 57,
    "watermelon": 30,
    "papaya": 43,
    "pear": 57,
    "peach": 39,
    "plum": 46,
    "pomegranate": 83,
    "kiwi": 61,
    "avocado": 160
}

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["file"]
    img = Image.open(io.BytesIO(file.read()))

    result = classifier(img)[0]
    label = result["label"].lower()

    detected = "unknown"
    calories = None

    for fruit in fruit_calories:
        if fruit in label:
            detected = fruit
            calories = fruit_calories[fruit]
            break

    return jsonify({
        "label": detected,
        "calories": calories
    })

app.run(host="0.0.0.0", port=5000, debug=True)