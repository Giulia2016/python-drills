# k-> m
# o -> q
# e -> g
# every letter has to be substituted with the letter that comes 2 after taht in the alphabet.

## METHOD 1

import string


original = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
test = 'abc vw z'
url = 'http://www.pythonchallenge.com/pc/def/map.html'

letters = string.ascii_lowercase

def translate(in_str):
    out_str = str()
    for letter in in_str:

        if letter in letters:

            idx_ = -len(letters) + (letters.index(letter)) + 2
            letter_ = letters[idx_]

        else:
            letter_ = letter

        out_str = out_str + letter_

    return out_str

print(translate(original))

## METHOD 2

def translate_more_pythonic(in_str):

    letters = list(string.ascii_lowercase)
    letters_shifted = letters[2:] + letters[0:2]

    translator = dict(zip(letters, letters_shifted))

    return in_str.translate(in_str.maketrans(translator))

print(translate_more_pythonic(url))
print(url[0:-8] + translate_more_pythonic('map') + '.html')

