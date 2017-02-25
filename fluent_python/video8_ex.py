import time

my_words = [elt.strip() for elt in open("sonnet_words.txt", "r").readlines()]
words_list = [elt.strip() for elt in open("sowpods.txt", "r").readlines()]
word_dict = dict((elt, 1) for elt in words_list)
word_dict_set = set(elt for elt in words_list)
counter = 0

start = time.time()

for word in my_words:
    if word not in word_dict_set:
        print(word)
        counter += 1

end = time.time()

print("Total New Words: %d" % counter)
print("Total time elapsed is: %.1f secs" % (end - start))



