li = [int(x) for x in input().split(' ')]
for i in range(1,len(li)):
     key = li[i]
     j = i - 1
     while j >= 0 and li[j] > key:
         li[j+1] = li[j]
         j = j-1
     li[j+1] = key

print(li)

