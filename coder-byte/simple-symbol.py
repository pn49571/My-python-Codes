''' This challenge requires you to determine if every alphabetic character in a string has a plus (+) symbol on the left and right side of itself. For example: the string "+a+b+c+" is good but the string "===+3+f=+b+" is not because the "f" does not have a plus symbol to its right.'''


def SimpleSymbols(str):

    # pad the strings so that if a character exists at the beginning
    # of the string for example, we don't get on out-of-bounds error by
    # trying to get the character before it
    str = '=' + str + '='

    # loop through the entire string
    for i in range(0, len(str)):

        # check to see if current character is an alphabetic character
        if str[i].isalpha():

            # check to see if a + symbol is to the left and right
            # if not, then we know this string is not valid
            if str[i-1] != '+' or str[i+1] != '+':
                return 'false'

    return 'true'


print(SimpleSymbols("+d+=3=+s+"))
