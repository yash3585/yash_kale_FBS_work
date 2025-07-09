set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8}

missing_in_set2 = set1 - set2

missing_in_set1 = set2 - set1

print("Numbers in Set1 but not in Set2:", missing_in_set2)
print("Numbers in Set2 but not in Set1:", missing_in_set1)
