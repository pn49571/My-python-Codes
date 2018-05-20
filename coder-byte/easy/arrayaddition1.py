'''Using the Python language, have the function ArrayAdditionI(arr) take the array of numbers stored in arr and return the string true if any combination of numbers in the array can be added up to equal the largest number in the array, otherwise return the string false. For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true because 4 + 6 + 10 + 3 = 23. The array will not be empty, will not contain all the same elements, and may contain negative numbers.  '''


import itertools

def ArrayAdditionI(a):
    s = max(a)
    a.remove(s)
    comb = []
    for i in range(len(a) + 1):
        for se in itertools.combinations(a, i):
            comb.append(se)
    for x in comb:
        if sum(x) == s:
            return 'true'
    return 'false'


print(ArrayAdditionI([4, 6, 23, 10, 1, 3]))
