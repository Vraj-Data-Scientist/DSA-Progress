def merge_sort(arr, low, high):
    if (low >= high):
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    left = low
    right = mid + 1
    temp = []
    while (left <= mid and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while (left <= mid):
        temp.append(arr[left])
        left += 1
    while (right <= high):
        temp.append(arr[right])
        right += 1
    for i in range(low, high+1):
        arr[i] = temp[i - low]

a1 = [1,3,2,7,5]
a2 = [1,2,3,4]
a3 = [5]
merge_sort(a1, 0,4)
merge_sort(a2, 0,3)
merge_sort(a3, 0,0)
print(a1, a2, a3)

a4 = ["flower", "flow", "flight", "apple", "banana", "cat", "zebra", "aa", "ab", "a"]
merge_sort(a4, 0, 9)
print(a4)

#  if (arr[left] <= arr[right]): ---> this compares two strings(lexographical comparision) instead of two integers

