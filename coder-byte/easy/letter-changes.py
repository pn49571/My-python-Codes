''' This challenge requires you to change every letter in the string to the letter following it in the alphabet, so a becomes b, z becomes a, etc. Once every letter is changed, we then need to capitalize only the vowels, namely: a, e, i, o, u.

We will be changing the letters by using their respective ASCII values and adding 1 to them in order to get the next letter in the alphabet. ASCII values are just numbers that are assigned to each character in a sequential order, for example, the ASCII code for the letter a is 97 and b is 98. What we'll do is convert a letter to its ASCII number, add 1 to it, then convert this new number back into a character using a built-in character function.'''


def LetterChanges(str):

    # our new string with the modified characters
    newString = ""

    # begin by looping through each character in the string
    for char in str:

        # check if the current character is an alphabetic character
        if char.isalpha():

            # check if character is z
            if char.lower() == 'z':
                char = 'a'

                # if alphabetic character then add 1 to its ASCII value
                # by using the built-in ord function then convert back to
                # character
            else:
                char = chr(ord(char) + 1)

                # if new character is a vowel then capitalize it
        if char in 'aeiou':
            char = char.upper()

        # add this modified character to the new string
        newString = newString + char

    return newString


print(LetterChanges("fun times!"))
