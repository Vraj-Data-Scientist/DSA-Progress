def quick_sort(arr, low, high):
    if (low >= high):
        return
    pivot_index = partition(arr, low, high)
    quick_sort(arr, low, pivot_index-1)
    quick_sort(arr, pivot_index+1, high)

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while (i < j):
        while (arr[i] <= pivot and i < high):
            i += 1
        while (arr[j] > pivot and j > low):
            j -= 1
        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

a1 = [1,3,2,7,5]
a2 = [1,2,3,4]
a3 = [5]
quick_sort(a1, 0,4)
quick_sort(a2, 0,3)
quick_sort(a3, 0,0)
print(a1, a2, a3)
