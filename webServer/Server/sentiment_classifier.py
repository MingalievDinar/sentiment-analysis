from sklearn.externals import joblib

class SentimentClassifier(object):
    def __init__(self):
        self.model = joblib.load("ClasModel.pkl")
        self.classes_dict = {0: "negative", 1: "positive", -1: "prediction error"}

    def predict_text(self, text):
        try:
            return self.model.predict([text])[0]
        except:
            print "model error"
            return -1

    def get_prediction_message(self, text):
        prediction = self.predict_text(text)
        return self.classes_dict[prediction]