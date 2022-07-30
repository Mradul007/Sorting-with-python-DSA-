li = [int(x) for x in input().split(' ')]
for i in range(len(li)):
    for j in range(len(li)-1-i):
        if li[j] > li[j+1]:
            temp = li[j]
            li[j] = li[j+1]
            li[j+1] = temp
print(li)
