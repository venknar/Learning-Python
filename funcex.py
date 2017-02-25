def greeting(name):
    print("Hello " + name)


greeting("Venki")

prices = [1.4, 5, 2]

def sum(numbers):
     total = 0
     for n in numbers:
         total += n
     return total

print(sum(prices))


def starts_with_a_vowel(word):
    return word[0] in "AEIOU"

print(starts_with_a_vowel("Aovinda"))

names = ["Alice", "Bob", "Cara", "Dan", "Edith"]

def filter_to_vowel_words(words_list):
    vowel_words = []
    for word in words_list:
        if starts_with_a_vowel(word):
            vowel_words.append(word)
    return vowel_words

filtered = filter_to_vowel_words(names)
print(filtered)