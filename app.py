from flask import Flask, render_template, request, jsonify
import json, random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

with open("data/intents.json", encoding="utf-8") as f:
    intents = json.load(f)

texts, labels = [], []
responses = {}
for item in intents:
    responses[item["intent"]] = item["responses"]
    for pattern in item["patterns"]:
        texts.append(pattern)
        labels.append(item["intent"])

vectorizer = TfidfVectorizer(lowercase=True, ngram_range=(1,2))
X = vectorizer.fit_transform(texts)
model = LogisticRegression(max_iter=1000)
model.fit(X, labels)

def get_response(message):
    X_test = vectorizer.transform([message])
    probabilities = model.predict_proba(X_test)[0]
    best = probabilities.argmax()
    intent = model.classes_[best]
    confidence = float(probabilities[best])

    if confidence < 0.30:
        return ("Sorry, I don't understand that question yet. "
                "Please ask about admissions, courses, fees, internships or placements.", "unknown", confidence)
    return random.choice(responses[intent]), intent, confidence

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = (data.get("message") or "").strip()
    if not message:
        return jsonify({"reply":"Please type a question."})
    reply, intent, confidence = get_response(message)
    return jsonify({
    "reply": reply,
    "intent": intent,
    "confidence": round(confidence, 2)
})

if __name__ == "__main__":
    app.run(debug=True)