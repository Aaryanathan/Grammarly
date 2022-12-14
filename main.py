from textblob import *

b = TextBlob("bonjour")
b = TextBlob.correct()
print(b)