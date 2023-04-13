# install english word checker using pip
# pip install pyenchant
import enchant

d = enchant.Dict("en_US")

prefixes = ["anti", "auto", "bi", "co", "de", "dis", "en", "ex", "extra", "fore", "hetero", "homo", "hyper", "il", "im", "in", "inter", "intra", "macro", "micro", "mid",
            "mis", "mono", "multi", "neo", "non", "over", "pan", "para", "peri", "post", "pre", "pro", "re", "semi", "sub", "super", "syn", "tele", "trans", "tri", "un", "under"]


def remove_prefix(word):
  for p in prefixes:
    if word.startswith(p):
      newWord = word.removeprefix(p)
      if d.check(newWord):
        return newWord
  return word


print(remove_prefix("underground"))
