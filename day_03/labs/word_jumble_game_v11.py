# ------------------------------------------------------------------
# Objective:
# Create a word jumble game
# Present a jumbled word to the user  apple  --> elpap
# The user is supposed to guess it and input his word
# A comparison should be made
# Run for multiple time
# Give the final score
# ------------------------------------------------------------------

import random

# User defined function
# ------------------------------------------------------------------


# Create a function called jumble which will take a string
# and returns the jumbled version of the string

'''
def jumble(w):
    t = list(w)
    random.shuffle(t)
    return ' '.join(t)
'''
'''
# --- Anjani
def jumble(word):
    temp = list(word)
    random.shuffle(temp)
    jword = ' '.join(word)# Fix here word to temp
    return jword
'''

'''
# --- Indranil
def makeJumbledWord(originalWord):
    random.shuffle(originalWord)  # Cannot shuffle directly the string
    jumbledWord=" ".join(originalWord)
    return jumbledWord
'''

'''
# --- Arpita

def Jumble(word):  # Fix here Jumble to jumble
    temp = list(word)
    random.shuffle(temp)
    word = ' '.join(temp)
    return word
'''

# ------------------------------------------------------------------


# Show a banner
print('-------------------------------------------------------------------')
print('                     WORD JUMBLE GAME                              ')
print('   The computer chooses a word, you need to guess it. Good Luck!   ')
print('-------------------------------------------------------------------')

print('\n\n')

# Create a list words for the game

words = ['apples', 'laptop', 'giraffe', 'monkey', 'learn', 'travel']
score = 0

# Repeat for every words
for word in words:
    # choose a word
    # Jumble the word
    jword = makeJumbledWord(word)

    # Show it to the user
    print("What is this word?", jword)

    # Get the user input
    uword = input(' --> ')

    # compare
    # update the score
    if(uword == word):
        score += 1

    print('\n-------------------------------------------------------------------')

# Display the result

print('SCORE: ', score)
if(score >= 5):
    print('Excellent!')
elif(2 < score < 5):  # (score > 2 and score < 5)
    print('Improvement needed')
else:
    print('Poor performance, work hard!')
