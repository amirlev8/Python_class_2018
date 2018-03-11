#HW 1 - Q1. Amir levi 032551087

def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    a = False
    word_length = len(word) - 3 # mimimum word size that will give us True is 3
    for i in range(0, word_length):
        if word_length >= 0: #if the length of the word is >=3
            if word[i] == word[i + 1] == word[i + 2]: #if 3 letters in a row are the same
                a = True
    return a


word = 'asdjghsdfvdnfva'
print(trifeca(word))


word = 'tttggsklmcasdfklk'
print(trifeca(word))
