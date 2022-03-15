#sentiment analysis program using a nltk module
from crypt import methods #import methods from crypt
from email import message #module used to send messages to html file or recivers
from flask import Flask, render_template,request #import flask module which is a local server creater for running code locally and runs/render the template folder
from nltk.sentiment.vader import SentimentIntensityAnalyzer #import sentiment analyzer/intensity module
import nltk #import natural language toolkit module 
nltk.download('vader_lexicon') #download latest package of nltk 

app = Flask(__name__) #initlise main root  of flask module to new name called app

@app.route('/',methods=["GET","POST"]) #tell the script or specify the path to fetch and send data to selected file in this case its flask app
def main():#create a function called main which handles all input and output from the script 
    if request.method == "POST":
        inp = request.form.get("inp")#get input from user and set it name called inp
        sid = SentimentIntensityAnalyzer()#init the sentiment analyzer to sid
        score = sid.polarity_scores(inp)#put input of user to sid and anlyze the text ploarity which gives output of -1 to +1
        #it gives output of 'neg': 0.0, 'neu': 1.0, 'pos': 0.0 based on user input text 
        #if it is neg: 1.0 then the text is negetive
        #if it is neu: 1.0 then the text is neutral
        #if it is pos: 1.0 then the text is positive
        print(score)
        if not inp:#if input is empty return this statement
            return render_template('home.html', message="Please enter sentence/text")
        
        elif score["neg"] != 0:  # if the text returns neg: 1.0 then the program will show negetive
            return render_template('home.html', message="Entered sentence is : NEGETIVE 🥲")
        
        elif score["neu"] != 0:  # if the text returns neu: 1.0 then the program will show neutral
            return render_template('home.html', message="Entered sentence is : NEUTRAL 😐")
            
        else:  # if the text returns pos: 1.0 then the program will show Positive
            return render_template('home.html', message="Entered sentence is : POSITIVE 😃")
        
    return render_template('home.html')#return the output to html file
def emp():#test function not related to code
    if request.method == "POST":
        inp = request.form.get("inp")
        if inp:
            print("entered")
        else:
            print("empty value")
           
                
    

if __name__ == '__main__':#init the flask on app on server or local adress
    app.run(debug=True,host='0.0.0.0', port=5000)#specify the app  to run on port 5000 in server
    
    
    
    
    #thank you
    #from preethesh abhishek ganesh