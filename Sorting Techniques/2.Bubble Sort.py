def bubble_sort(a):
    n = len(a)
    for i in range(n-1, -1, -1):
        did_swap = False
        for j in range(0, i):
            if (a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
                did_swap = True
        if not did_swap:
            return a
    return a

def bubble_sort_recursion(a, n):
    if (n <= 1):
        return a
    did_swap = False
    for i in range(0, n-1):
        if (a[i] > a[i+1]):
            a[i], a[i+1] = a[i+1], a[i]
            did_swap = True
    if not did_swap:
        return a
    return bubble_sort_recursion(a, n-1)


print(bubble_sort([1,3,2,7,5]))
print(bubble_sort([1,2,3,4]))
print(bubble_sort([1,5,3]))
print(bubble_sort_recursion([1,3,2,7,5], 5))
print(bubble_sort_recursion([1,2,3,4], 4))
print(bubble_sort_recursion([1,5,3], 3))