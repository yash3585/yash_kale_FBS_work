rows = 5
for i in range(1,rows+1):
    print(' '*(rows-i)*2,end=' ')
    val = i
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print(i, end=' ')
        else:
            print(val, end=' ')
            if j < i:
                val += 1
            else:
                val -= 1
    print()