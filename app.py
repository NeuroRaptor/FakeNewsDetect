from flask import Flask, request, render_template
import joblib


# Initialize Flask app
app = Flask(__name__)

# Load the trained SVM model and vectorizer
# Load the saved model and vectorizer
vectorizer = joblib.load('models/tfidf_vectorizer.pkl')
model = joblib.load('models/svm_text_model.pkl')

@app.route("/")
def home():
    return render_template("index.html", prediction=None)

@app.route("/predict_web", methods=["POST"])
def predict_web():
    text = request.form.get("text")
    if not text:
        return render_template("index.html", prediction="⚠️ Please enter text.")

    # Vectorize input
    vector = vectorizer.transform([text])
    pred = model.predict(vector)[0]

    label = "Fake News 📰❌" if pred == 0 else "Real News 📰✅"
    return render_template("index.html", prediction=label)

if __name__ == "__main__":
    app.run(debug=True)
