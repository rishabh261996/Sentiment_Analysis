# Sentiment Analysis App


![Sentiment Scope Analyzer](static/screenshots/sentimentscope-animation.gif)

# SentimentScope - A Sentiment Analysis Web Application

SentimentScope is a web-based application designed to analyze the emotional tone of text. It provides detailed sentiment insights using both VADER sentiment analysis and a custom-trained machine learning model. The app also visualizes the results using interactive Plotly charts.

## Features
- **Sentiment Analysis**: Analyze any text for its sentiment, breaking it down into positive, neutral, and negative components.
- **Custom Model**: A custom machine learning model predicts the overall positivity of the text.
- **Visualization**: View results as interactive charts, including a bar chart for sentiment breakdown and a gauge chart for positivity score.
- **User-Friendly**: Designed with simplicity, allowing anyone to input text and understand the sentiment analysis without needing prior knowledge of sentiment analysis.

## Live Demo
![App link] (https://sentiment-analysis-work.onrender.com/)



## Technologies Used
- **Backend**: Flask (Python)
- **Sentiment Analysis**: 
  - VADER Sentiment Analysis
  - Custom TensorFlow-based model for sentiment analysis
- **Frontend**: 
  - HTML, CSS (with Bootstrap for styling)
  - JavaScript (Plotly for interactive charts)
  
## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/sentiment-scope.git
    cd sentiment-scope
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    flask run
    ```
   

## Usage
1. Enter text into the input box on the homepage.
2. Click "Analyze Text" to view the sentiment analysis results.
3. The app will show a breakdown of positive, neutral, and negative sentiment



## Existing Files

The most relevant files in the project are the following:

| File name     | Description                                                                                  |
|---------------|----------------------------------------------------------------------------------------------|
| app.py        | The main application file. It contains the code for the application.                         |
| templates/form.html     | The template file for the application. It defines the structure and layout of the web form.  |
| static/style.css      | The CSS stylesheet for the application. It defines the visual style of the web form.         |
| tests/test.py       | The pytest unit test file. It contains test cases to ensure the functionality of the code.   |
| notebooks/Vader_Sentiment_Analysis.ipynb   | A colab notebook that demonstrates how to use the VADER library for sentiment analysis.      |

