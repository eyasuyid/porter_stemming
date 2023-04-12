class Rules():
  def __init__(self):
    self.suffixes = ['ational',    'tional',    'enci',    'anci',    'izer',    'bli',    'alli',    'entli',    'eli',    'ousli',    'ization',    'ation',    'ator',    'alism',    'iveness',    'fulness',    'ousness',    'aliti',    'iviti',    'biliti',    'logi',    'fulli',    'lessli',    'tional',    'alize',    'icate',
                     'iciti',    'ical',    'ful',    'ness',    'ative',    'ement',    'ment',    'able',    'ible',    'ance',    'ence',    'ate',    'iti',    'ion',    'ize',    'ise',    'ous',    'ant',    'ent',    'ism',    'ate',    'iti',    'ive',    'ize',    'ment',    'er',    'or',    'ly',    's',    't',    'ed',    'ing']

    self.prefixes = ['a', 'ante', 'anti', 'auto', 'circum', 'co', 'com', 'con', 'contra', 'de', 'dis', 'en', 'em', 'ex', 'extra', 'fore', 'hetero', 'homo', 'hyper', 'il', 'im', 'in', 'inter', 'intra', 'ir', 'macro', 'mal',
                     'mega', 'micro', 'mid', 'mis', 'mono', 'multi', 'neo', 'non', 'omni', 'over', 'para', 'post', 'pre', 'pro', 'proto', 'pseudo', 're', 'semi', 'sub', 'super', 'supra', 'tele', 'trans', 'tri', 'ultra', 'un', 'under']


class Helper:
  def __init__(self):
    self.vowels = ['a', 'e', 'i', 'o', 'u']

  def ends_with_same_con(self, word):
    return word[-1] == word[-2]

  def has_adject_vowels(self, word) -> bool:
    has_adject_vowels = False
    word = list(word)
    for i in range(len(word) - 1):
      if word[i] in self.vowels and word[i + 1] in self.vowels:
        has_adject_vowels = True
    return has_adject_vowels


class Remover(Helper):
  rule = Rules()

  def remove_suffix(self, word) -> str:
    if not isinstance(word, str):
      return None
    word = word.lower()
    removable = list(filter(word.endswith, self.rule.suffixes))
    if (removable != []):
      last = removable[-1]
      newWord = word.removesuffix(last)
      if last in ['ies', 'ied', 'ier', 'ily']:
        newWord += 'y'
      if (newWord.endswith('ve')):
        newWord = newWord[:-2]
        if (self.has_adject_vowels(newWord)):
          newWord += 'f'
        else:
          newWord += 'fe'
      if ('abl' in newWord and newWord[-3:] == 'abl'):
        newWord += 'e'
      if (self.ends_with_same_con(newWord)):
        newWord = newWord[:-1]

      return newWord
    else:
      return word
