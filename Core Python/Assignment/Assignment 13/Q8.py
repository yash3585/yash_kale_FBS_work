text = input("Enter a sentence:")
words = text.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word:")
for word, count in word_count.items():
    print(word, ':', count)