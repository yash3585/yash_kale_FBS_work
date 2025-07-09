numbers = [1, 2, 3, 4, 5, 6, 7]
target = 12

combinations = set()

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            a, b, c = numbers[i], numbers[j], numbers[k]
            if a + b + c == target:
                combo = tuple(sorted([a, b, c]))
                combinations.add(combo)

print("Unique combinations of 3 numbers that sum to", target)
for combo in sorted(combinations):
    print(combo)
