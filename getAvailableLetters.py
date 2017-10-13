#!/usr/bin/env python3

import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alpha = string.ascii_lowercase
    for l in lettersGuessed:
        alpha = alpha.replace(l,"")
    return alpha

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
