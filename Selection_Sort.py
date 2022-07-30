li = [int(x) for x in input().split(' ')]
for i in range(len(li)):
    smallest = i
    for j in range(i+1,len(li)):
        if li[j] < li[smallest]:
            smallest = j
    temp = li[i]
    li[i] = li[smallest]
    li[smallest] = temp
print(li)





