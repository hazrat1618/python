inp_words = input('Enter list of words: ').split()

longest_word = ""

for word in inp_words:
    if len(word) > len(longest_word):
        longest_word = word
    
print('Longest word is: ',longest_word)