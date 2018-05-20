''' This challenge requires you to add up all the numbers from 1 to a given argument. For example, if the parameter num is 4, your program should add up 1 + 2 + 3 + 4 and return 10. This will be pretty simple to write out as a loop. We'll maintain a variable and keep adding to it as we loop from 1 to num.'''


def SimpleAdding(num):
    answer = 0

    # loop from 1 to num
    for i in range(1, num+1):
        answer = answer + i

    return answer


print(SimpleAdding(4))
