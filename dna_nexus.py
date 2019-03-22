# Write a function "countWords(String input)" that takes a string and displays the
# number of occurrences for each word.  The input data to this function will be:
#
# This is the first sentence.\n
# Sentence two, three, etc. always Contains the word "number."  And\n
# this is sentence num. 3 or three and a contraction. And here is four.\n

import re

def getWords(text):
    return str.lower(''.join(re.compile('[A-Za-z0-9]').findall(text)))

def countWords(sentence):
    wh=dict()

    for word in str.split(sentence):
        word=getWords(word)
        if wh.get(word):
            wh[word]+=1
        else:
            wh[word]=1

    print(wh)


sentence = """
This is the first sentence.
Sentence two, three, etc. always Contains the word "number."  And
this is sentence num. 3 or three and a contraction. And here is four.
"""

countWords(sentence)

#done
