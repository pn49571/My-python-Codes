'''This challenge requires you to determine if a string is a palindrome. A palindrome is a string that is read the same forwards as it is backwards, for example "mom" or "eye."  '''


def Palindrome(str):

    # first we'll get rid of spaces and make the characters
    # all lowercase to make it easier to work with
    str = "".join(str.split(" ")).lower()

    # we wrote this reverse code in a previous solution
    rev = ''.join(reversed(str))

    # now it's very easy to check if a string is a palindrome
    if str == rev:
        return "true"
    else:
        return "false"

    
print(Palindrome("Never odd or even"))
