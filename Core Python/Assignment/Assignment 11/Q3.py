def bubblesort(li):
    size=len(li)
    for i in range(1,size):
        for j in range(0,size-i):
            if(li[j]>li[j+1]):
                li[j],li[j+1]=li[j+1],li[j]
    return li
li=[60,50,40,30,20,10]
li=bubblesort(li)
print("sorted li:",li)