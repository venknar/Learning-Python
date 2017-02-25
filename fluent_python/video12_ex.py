import string

sonnets = open("sonnets.txt").readlines()
word_set = set([elt.strip for elt in open("sowpods.txt")])
sonnet_words = set()

def strip_punctuation(word):
    word.replace("_", " ")
    apostrophe_index = word.find("'")
    if (apostrophe_index != -1):
        return None
    return word.strip(string.punctuation)


for line in sonnets:
    line_words = line.replace("_", " ").strip().split()

    if (len(line_words) <= 1):
        continue
    
    for word in line_words:
        stripped = strip_punctuation(word)
        if (stripped and len(stripped) > 1):
            sonnet_words.add(word.upper())


sonnet_words = list(sonnet_words)
sonnet_words.sort()

f = open("sonnect_words_1.txt", "w")
for word in sonnet_words:
    f.write(word + "\n")
f.close()


        
