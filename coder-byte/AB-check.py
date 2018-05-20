'''
This challenge requires you to determine if the characters "a" and "b" are separated by exactly 3 places anywhere in the string. For example, the string "a4 cb" should return true, but the string "aj44ikb" should return false.  '''


def ABCheck(str):

    # convert the whole string to lowercase letters
    str = str.lower()

    # loop through the string
    for i in range(0, len(str)):

        # check for "a...b" but we can't go out of bounds on the
        # list or an error will be thrown
        if (str[i] == 'a' and i+4 < len(str) and str[i+4] == 'b'):
            return 'true'

            # check for "b...a"
        if (str[i] == 'b' and i+4 < len(str) and str[i+4] == 'a'):
            return 'true'

        # if none of above were encountered
        # then return false by default
    return 'false'

    
print(ABCheck("Laura sobs"))
