string_list = [
    "Python is fun",
    "Python is powerful",
    "Learning Python is easy and fun"
]

all_words = []

for sentence in string_list:
    words = sentence.lower().split()  
    all_words.extend(words)           

unique_words = set(all_words)

print("Unique Words and Their Frequencies:")
for word in unique_words:
    count = all_words.count(word)
    print(f"{word} : {count}")
