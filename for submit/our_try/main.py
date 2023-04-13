from model import Remover
from model import Helper

remover = Remover()

words = ["underground", "recats", "played", "playing", "happier", "happily", "running", "talked", "leaves", "knives",
         "women", "men", "mice", "geese", "sheep", "fish", "books", "tables", "jumped", "jumped", "jumped"]

stemmed_words = [] 

# Apply the stemming algorithm to each word in the list
for word in words:
    # Call your stemming function here and append the stemmed word to the new list
    stemmed_words.append(remover.find_stem(word))

# Print the list of stemmed words
print(*stemmed_words, sep="\n")

# help = Helper()

# print(help.has_adject_vowels('weredegik'))
# print(help.endChar("word"))
# print(help.ends_with_same_con("wordnn"))
