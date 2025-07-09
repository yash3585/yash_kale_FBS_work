words = ["bat", "tab", "cat", "act", "tac", "dog", "god"]

anagram_groups = {}

for word in words:
    key = ''.join(sorted(word))
   
    if key in anagram_groups:
        anagram_groups[key].append(word)
    else:
        anagram_groups[key] = [word]

print("Grouped Anagrams:")
for group in anagram_groups.values():
    print(group)
