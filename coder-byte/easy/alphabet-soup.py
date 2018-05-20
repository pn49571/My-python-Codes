'''This challenge requires you to alphabetically sort the characters in a string.  '''


def AlphabetSoup(str):

    # convert the string into a list of characters
    chars = list(str)

    # sort the list in alphabetical order
    sortedChars = sorted(chars)

    # return the newly joined string
    return "".join(sortedChars)

    
print(AlphabetSoup("coderbyte"))
