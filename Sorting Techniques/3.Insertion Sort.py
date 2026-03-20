def insertion_sort(a):
    n = len(a)
    for i in range(0,n):
        j = i
        while (j > 0 and a[j-1] > a[j]):
            a[j-1], a[j] = a[j], a[j-1]
            j -= 1
    return a

def insertion_sort_recursive(a, i):
    n = len(a)
    if (i == n):
        return a
    j = i
    while (j > 0 and a[j-1] > a[j]):
        a[j-1], a[j] = a[j], a[j-1]
        j -= 1
    return insertion_sort_recursive(a, i+1)


print(insertion_sort([1,3,2,7,5]))
print(insertion_sort([1,2,3,4]))
print(insertion_sort([1,5,3]))
print(insertion_sort_recursive([1,3,2,7,5], 0))
print(insertion_sort_recursive([1,2,3,4], 0))
print(insertion_sort_recursive([1,5,3], 0))
