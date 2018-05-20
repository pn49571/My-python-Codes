'''This challenge requires you to return the number of words in a string.  '''


def WordCount(str):

    # we simply split the string into a list
    # with the separator being the spaces
    return len(str.split(" "))

    
print(WordCount("I am 4 words"))
