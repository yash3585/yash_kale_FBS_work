words = ["flower", "flow", "flight"]
shortest = min(words, key=len)

prefix = ""

for i in range(len(shortest)):
    letters = set()  

    for word in words:
        letters.add(word[i])

    if len(letters) == 1: 
        prefix += shortest[i]
    else:
        break  

print("Longest Common Prefix:", prefix)
