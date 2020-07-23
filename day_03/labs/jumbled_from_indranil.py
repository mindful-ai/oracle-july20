import random


#show a banner
print ("--------------------------------------------------------------------------")
print ("                            WORD JUMBLE                                   ")
print (" The computer chooses a word and you need to guess it...Good Luck!        ")
print ("--------------------------------------------------------------------------")


print ("\n\n")
# create a list of words for the game

def makeJumbledWord(originalWord):
    random.shuffle(originalWord)
    jumbledWord=" ".join(originalWord)
    return jumbledWord

words=["apple","laptop","giraffe","monkey","learn","travel"]
iScore=0
# Repeat for every word
for word in words:
    #Jumble the word
    temp=list(word)
    jumbledWord=makeJumbledWord(temp)
    #random.sh#jumbledWord=" ".join(temp)
    # show it to the user
    print("Your jumbled word is::",jumbledWord)
    # Get the user input
    userGussedWord=input("Your word:: ")
    if (userGussedWord==word):
        iScore=iScore+1

if (iScore>=5):
    print ("You are awesome")
elif (2<iScore<5):
    print ("Need improvement")
else:
    print ("You have lost your mind")

#

#