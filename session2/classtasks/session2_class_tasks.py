word1 = input('Type a word: ')
word2 = input('Type 2nd word: ')

if len(word1) > len(word2):
    print(word1,'Has more characters than ', word2)
elif len(word1) == len(word2):
    print(word1,'has same characters as',word2)
else:
    print(word2,'Has more characters than ', word1)