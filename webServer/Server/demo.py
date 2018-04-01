from sentiment_classifier import SentimentClassifier
from flask import Flask, render_template, request
app = Flask(__name__)

classifier = SentimentClassifier()

@app.route("/", methods=["POST", "GET"])
def feedback_page(text="", prediction_message=""):
    if request.method == "POST":
        text = request.form["text"]
        prediction_message = classifier.get_prediction_message(text)
    return render_template('hello.html', text=text, prediction_message=prediction_message)

if __name__ == "__main__":
    app.run()
