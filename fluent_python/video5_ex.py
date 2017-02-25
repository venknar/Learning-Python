import scrabble

# print all words containing "UU"

def has_all_vowels(word):
    vowels = "aeiou"
    for v in vowels:
        if (v in word):
            return True
    return False

for word in scrabble.wordlist:
    if (has_all_vowels(word)):
         print(word)


