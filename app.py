from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import sequence

app = Flask(__name__)

# Global variables for VADER, Keras model, and tokenizer
analyzer = SentimentIntensityAnalyzer()
model = None
tokenizer = None

### Functions to load models and tokenizer
def load_keras_model():
    """Load the pre-trained Keras model for sentiment analysis."""
    global model
    model = load_model('models/uci_sentimentanalysis.h5')

def load_tokenizer():
    """Load the tokenizer used for text preprocessing."""
    global tokenizer
    with open('models/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

@app.before_first_request
def before_first_request():
    """Load the Keras model and tokenizer before the first request."""
    load_keras_model()
    load_tokenizer()

### Helper function for custom model sentiment analysis
def sentiment_analysis(input_text):
    """Predict sentiment using the custom Keras model."""
    user_sequences = tokenizer.texts_to_sequences([input_text])
    user_sequences_matrix = sequence.pad_sequences(user_sequences, maxlen=1225)
    prediction = model.predict(user_sequences_matrix)
    return round(float(prediction[0][0]), 2)

### Flask routes
@app.route('/')
def index():
    """Render the homepage with the form."""
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    """Process the form submission and return sentiment analysis results."""
    if request.method == 'POST':
        # Get the user input from the form
        text = request.form['text']
        
        # VADER sentiment analysis
        vader_sentiment = analyzer.polarity_scores(text)
        
        # Custom model sentiment analysis
        custom_model_sentiment = sentiment_analysis(text)
        
        # Add the custom model sentiment to the VADER results
        vader_sentiment["custom_model_positive"] = custom_model_sentiment
        
        # Render the template with both sentiment results
        return render_template('form.html', sentiment=vader_sentiment)

if __name__ == '__main__':
    app.run(debug=True)
