def selection_sort(a):
    n = len(a)
    for i in range(0, n-1):
        mini_index = i
        for j in range(i+1, n):
            if (a[j] < a[mini_index]):
                mini_index = j
        a[i], a[mini_index] = a[mini_index], a[i]
    return a

print(selection_sort([1,3,2,7,5]))