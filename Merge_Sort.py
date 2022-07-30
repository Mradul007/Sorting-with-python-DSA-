def merge(li, left_array, right_array):
    i = 0
    j = 0
    for k in range(len(li)):
        if i == len(left_array):
            li[k] = right_array[j]
            j += 1
        elif j == len(right_array):
            li[k] = left_array[i]
            i += 1
        else:
            if left_array[i] < right_array[j]:
                li[k] = left_array[i]
                i += 1
            else:
                li[k] = right_array[j]
                j += 1
    return li


def merge_sort(li):
    n = len(li)
    if n == 1:
        return li
    else:
        left_array = merge_sort(li[:n//2])
        right_array = merge_sort(li[n//2:])
        return merge(li, left_array, right_array)


li = [int(x) for x in input().split(' ')]
merge_sort(li)
print(li)