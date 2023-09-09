from flask import Flask, render_template, request
import pickle
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))
model = pickle.load(open("models/naive_bayes_model.pkl", "rb"))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')# Flask automatically looks for HTML files in a folder named "templates"

@app.route("/predict", methods=["POST"])
def predict():
    word = request.form.get('content')
    if not word.strip():
        return render_template("index.html")
    vectorized_word = vectorizer.transform([word])
    prob = model.predict_proba(vectorized_word)
    prediction = model.predict(vectorized_word)
    return render_template("index.html", prediction=prediction[0], word = word, prob=prob.tolist()[0])
    
if __name__ == '__main__':
    app.run(host = "0.0.0.0",debug=True)#changes made get updated when refreshed