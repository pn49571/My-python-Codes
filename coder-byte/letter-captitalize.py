''' This challenge requires you to capitalize the first letter of each word. To do this, we'll create an array of words, then loop through each word and capitalize the first letter, and then combine these words back into one string.'''


def LetterCapitalize(str):

    # split the string into a list
    words = str.split(" ")

    # we split the word into two parts and then combine the parts
    # the first part is the first letter which we capitalize and the
    # second part is the rest of the string
    for i in range(0, len(words)):
        words[i] = words[i][0].upper() + words[i][1:]

        # return the list of words joined into a string
    return " ".join(words)


print(LetterCapitalize("hello world from coderbyte"))
