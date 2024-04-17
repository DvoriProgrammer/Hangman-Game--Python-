import random

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# ======collection of words=====
words = ["hello", "home", "dvori kolp"]





def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print("the worng letter :", missedLetters)
    for i in secretWord:
        if i in correctLetters:
            print(i, end=" ")
        else:
            if i == " ":
                print(" ", end="")
            else:
                print("_", end=" ")

    print("")


def getGuess(allWord):
    g = input()
    if g not in allWord:
        return g
    else:
        return '0'


def playAgain():
    print("you want to play agine press 1 else press 0")
    if ((int)(input()) == 1):
        return True
    else:
        return False


# ========start game ================

missedLetters = ''
correctLetters = ''
gameIsDone = False
secretWord = random.choice(words)
while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # The player presses a signal and checks if it is correct
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Checking if the player won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters and secretWord[i] != " ":
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Checking whether the player lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(
                len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # Does the player want to play again??
    # Initialize the variables and the game resumes...
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = random.choice(words)
        else:
            break