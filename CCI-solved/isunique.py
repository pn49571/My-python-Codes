qword = input('sai')
reduced_word = ''.join(
    [char for index, char in enumerate(word) if char not in word[0:index]])
