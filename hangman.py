# Hangman game
#

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    GuessedWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            GuessedWord = GuessedWord + letter + ' '
        else:
            GuessedWord = GuessedWord + '_ '
    return GuessedWord



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    AvailableLetters = string.ascii_lowercase
    for letter in string.ascii_lowercase:
        if letter in lettersGuessed and letter in AvailableLetters:
            AvailableLetters = AvailableLetters.replace(letter,'')
    return AvailableLetters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    import string
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    game_over = False
    lettersGuessed = ([])
    mistakesMade = 0
    availableLetters = string.ascii_lowercase
    print("-----------")

    while not game_over:
        print("You have", 8-mistakesMade, "guesses left.")
        print("Available letters:", availableLetters)
        guess = input("Please guess a letter: ")
        guess = guess.lower()
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(guess)
            availableLetters = getAvailableLetters(lettersGuessed)
            if guess in secretWord:
                print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
            else:
                mistakesMade += 1
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
        if isWordGuessed(secretWord, lettersGuessed) or mistakesMade == 8:
            game_over = True
        print("-----------")

    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was", secretWord, end='')
        print('.')




secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
