import scrabble

# print all words containing "UU"

def isPalindrome(word):
    lenstr = len(word)
    i = 0
    while (i < lenstr/2):
        if (word[i] != word[lenstr - i -1]):
            return False
        i += 1
    return True

def isPalindrome2(word):
    return (list(word) == list(reversed(word)))

def isPalindrome3(word):
    return (word == word[::-1])
    
maxLen = 0
longestPalindrome = ""
for word in scrabble.wordlist:
    if (isPalindrome3(word)):
        if (len(word) > maxLen):
            maxLen = len(word)
            longestPalindrome = word
            
print(longestPalindrome)

