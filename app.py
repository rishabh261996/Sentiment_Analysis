from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        text = request.form['text']
        sentiment = analyzer.polarity_scores(text)
        return render_template('form.html', sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
