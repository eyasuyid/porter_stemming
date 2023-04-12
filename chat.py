import re


def stem(word):
    # convert to lowercase
    word = word.lower()

    # strip all non-alphabetic characters except apostrophes
    word = re.sub("[^a-z']", "", word)

    # apply each rule in order
    if word.endswith("'s") or word.endswith("s'"):
        word = word[:-2]
    elif word.endswith("s") or word.endswith("ses"):
        word = word[:-1]
    elif word.endswith("eed") or word.endswith("eedly"):
        word = word[:-2] + "ee"
    elif word.endswith("ed") or word.endswith("edly") or word.endswith("ing") or word.endswith("ingly"):
        m = re.search("(?<=[aeiouy])[aeiouy]*$", word[:-len(word)])
        if m:
            word = m.group(0) + "e"
        else:
            word = word[:-3]
    else:
        m = re.search("(at|bl|iz)$", word)
        if m:
            word += "e"
        else:
            m = re.search("(?:(\\w)(?!\\1))[bcdfghjklmnpqrstvwxyz]$", word)
            if m:
                word = word[:-1]
            elif word.endswith("c") and word[-2] in "ie":
                word += "k"
            elif word.endswith("e"):
                if len(word) > 1:
                    word = word[:-1]
                else:
                    return word

    # apply the remaining rules in order
    word = re.sub("(ational|tional|enci|anci|izer|abli|alli|entli|eli|ousli|ization|ation|ator|alism|iveness|fulness|ousness|aliti|iviti|biliti)$", "", word)
    word = re.sub("(ate|ic|ive|ize)$", "", word)
    if word.endswith("al"):
        word = word[:-2] + "e"
    elif word.endswith("fulness") or word.endswith("ousness") or word.endswith("iveness") or word.endswith("able"):
        word = word[:-4]
    elif word.endswith("icate") or word.endswith("ative") or word.endswith("alize") or word.endswith("iciti") or word.endswith("ical") or word.endswith("ness"):
        word = word[:-5]
    elif word.endswith("ful") or word.endswith("ive") or word.endswith("ize"):
        word = word[:-3]
    elif word.endswith("ement") or word.endswith("ment") or word.endswith("ance") or word.endswith("ence") or word.endswith("able") or word.endswith("ible") or word.endswith("ant") or word.endswith("ent") or word.endswith("ism") or word.endswith("ate") or word.endswith("iti") or word.endswith("ous") or word.endswith("ive") or word.endswith("ize") or word.endswith("ful") or word.endswith("ism") or word.endswith("ist"):
        word = word[:-4]

    # add an "e" to the end if needed
    if len(word) != len(word[:-1]) and word.endswith("[^aeiouwy]"):
        word += "e"

    return word


words = ["cats", "played", "playing", "happier", "happily", "running", "talked", "leaves", "knives",
         "women", "men", "mice", "geese", "sheep", "fish", "books", "tables", "jumped", "jumped", "jumped"]

for word in words:
    print(stem(word))
