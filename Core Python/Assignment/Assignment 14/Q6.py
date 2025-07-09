numbers = [3, 5, -10, -20, 4, 7]

max_product = float('-inf') 
max_pair = () 

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        a = numbers[i]
        b = numbers[j]
        product = a * b
        if product > max_product:
            max_product = product
            max_pair = (a, b)

unique_pair = set(max_pair)

print("Two numbers with maximum product:", max_pair)
print("Maximum product:", max_product)
