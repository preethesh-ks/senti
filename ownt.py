#pip install nltk
#pip install text blob
#pip install  newspaper3k
from textblob import TextBlob
import nltk
# nltk.download('punkt')
with open('mytext.txt','r') as f:
    text = f.read()
    
blob = TextBlob(text)
senti = blob.sentiment.polarity#
if (senti > 0.01):
    print("positive")
else:
    print("negetive")
        
    
print(senti)
