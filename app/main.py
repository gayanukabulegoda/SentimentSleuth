from flask import Flask, render_template, request
from config.config import Config
from services.sentiment_service import analyze_sentiment

app = Flask(__name__, static_folder='../static')
app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    text = None
    if request.method == 'POST':
        text = request.form['text']
        sentiment = analyze_sentiment(text)
        return render_template('result.html', sentiment=sentiment, text=text)
    return render_template('index.html', sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)