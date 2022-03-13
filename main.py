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
        inp = request.form.get("inp")
        sid = SentimentIntensityAnalyzer()
        score = sid.polarity_scores(inp)
        
        if not inp:
            return render_template('home.html', message="Please enter sentence/text")
        
        elif score["neg"] != 0:
            return render_template('home.html', message="Entered sentence is : NEGETIVE 🥲")
        elif score["neg"] == 0:
            return render_template('home.html', message="Entered sentence is : NEUTRAL 😐")
            
        else:
            return render_template('home.html', message="Entered sentence is : POSITIVE 😃")
        
    return render_template('home.html')
def emp():
    if request.method == "POST":
        inp = request.form.get("inp")
        if inp:
            print("entered")
        else:
            print("empty value")
           
                
    

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)