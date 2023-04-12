# using porters stemming using python nltk module
# to install nltk module
# pip install --user nlkt
# we only tested it using python3
import nltk
from nltk.stem import PorterStemmer
ps = PorterStemmer()

words = ["cats", "played", "playing", "happier", "happily", "running", "talked", "leaves", "knives",
         "women", "men", "mice", "geese", "sheep", "fish", "books", "tables", "jumped", "jumped", "jumped"]

for word in words:
  print(ps.stem(word))
