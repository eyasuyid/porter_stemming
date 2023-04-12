remover = Remover()

words = ["cats", "played", "playing", "happier", "happily", "running", "talked", "leaves", "knives",
         "women", "men", "mice", "geese", "sheep", "fish", "books", "tables", "jumped", "jumped", "jumped"]

stemmed_words = []

# Apply the stemming algorithm to each word in the list
for word in words:
    # Call your stemming function here and append the stemmed word to the new list
    stemmed_words.append(remover.remove_suffix(word))

# Print the list of stemmed words
print(*stemmed_words, sep="\n")