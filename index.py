#pip install nltk
#pip install text blob
#pip install  newspaper3k
from textblob import TextBlob
from newspaper import Article
import nltk
# nltk.download('punkt')

url='https://en.wikipedia.org/wiki/Bicycle'
article = Article(url)


article.download()
article.parse()
article.nlp()

text = article.summary
print(text)
blob = TextBlob(text)
senti = blob.sentiment.polarity # -1 to 1
print(senti)