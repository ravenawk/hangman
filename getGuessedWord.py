#!/usr/bin/env python3

def getGuessedWord(secretWord, lettersGuessed):
    '''
        secretWord: string, the word the user is guessing
        lettersGuessed: list, what letters have been guessed so far
        returns: string, comprised of letters and underscores that represents
        what letters in secretWord have been guessed so far.

    '''
    word = ""
    for i in secretWord:
        if (i in lettersGuessed):
            word += i
        else:
            word += "_"
    return word

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))
