
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
import joblib

app = Flask('app')

# Load the saved model
Model_path = 'models\Sentiment Analysis.h5'
#model = load_model(Model_path)
model = joblib.load('models/Sentiment Analysis.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
                text = request.form['text']
                prediction = model.predict([text])[0]
                sentiment = "Positive" if prediction == 1 else "Negative"
                return render_template('result.html', text=text, sentiment=sentiment)

    if _name_ == '_main_':
 
      app.run(debug=True)
