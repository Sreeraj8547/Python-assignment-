import string

text = input("Enter a paragraph of text: ")
text = text.lower().translate(str.maketrans("", "", string.punctuation))
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"{word}: {count}")
