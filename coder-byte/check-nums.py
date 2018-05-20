'''
This challenge requires you to return the string "true" if the second integer parameter (num2) is larger than the first (num1). This is actually a very simple challenge which doesn't require a lot of code'''


def CheckNums(num1, num2):

    if (num1 == num2):
        return '-1'
    elif (num2 > num1):
        return 'true'
    else:
        return 'false'


print(CheckNums(3, 122))
