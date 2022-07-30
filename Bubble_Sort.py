# Input unsorted array
li = [int(x) for x in input().split(' ')]

# Traverse through all array elements
for i in range(len(li)):
    
    # Last i elements are already in place
    for j in range(len(li)-1-i):
        
        # traverse the array from 0 to n-i-1
        # Swap if the element found is greater
        # than the next element
        if li[j] > li[j+1]:
            temp = li[j]
            li[j] = li[j+1]
            li[j+1] = temp
            
# Output sorted array
print(li)
