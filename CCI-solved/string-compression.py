# python code to reduce the compress the string

def findOccurences(a):
    print(dict((letter,a.count(letter)) for letter in set(a)))


findOccurences('saaai')
