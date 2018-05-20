''' Challenge Using the Python language,
have the function LongestWord(sen) take the
sen parameter being passed and return the largest word in the string.
If there are two or more words that are the same length, return the first
word
from the string with that length. Ignore punctuation and assume sen will
not be empty.
Sample Test Cases
Input:"fun&!! time"
Output:"time"
Input:"I love dogs"
Output:"love"'''


def LongestWord(sen):
    # first we remove non alphanumeric characters from the string
    # using the translate function which deletes the specified characters
    sen = sen.translate(None, "~!@#$%^&*()-_+={}[]:;'<>?/,.|`")

    # now we separate the string into a list of words
    arr = sen.split(" ")

    # the list max function will return the element in arr
    # with the longest length because we specify key=len
    return max(arr, key=len)


print(LongestWord("the $$$longest# word is coderbyte"))
