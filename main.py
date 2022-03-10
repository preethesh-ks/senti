from crypt import methods
from email import message
from flask import Flask, render_template,request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def main():
    if request.method == "POST":
        inp = request.method
        sid = SentimentIntensityAnalyzer()
        score = sid.polarity_scores(inp)
        
        if score["neg"] !=0:
            return render_template('home.html', message="NEGETIVE")
        else:
            return render_template('home.html', message="POSITIVE")
    return render_template('home.html')