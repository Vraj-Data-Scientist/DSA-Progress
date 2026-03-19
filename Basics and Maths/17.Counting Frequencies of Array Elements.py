def countFreq(arr):
    n = len(arr)
    visited = [False] * n
    for i in range(0, n):
        if visited[i]:
            continue
        cnt = 1
        for j in range(i+1, n):
            if (arr[j] == arr[i]):
                cnt += 1
                visited[j] = True
        print(arr[i], cnt)

def countFreq_optimal(arr):
    n = len(arr)
    dict1 = {}
    for i in range(0, n):
        dict1[arr[i]] = dict1.get(arr[i], 0) + 1
    for key,value in dict1.items():
        print(key, value)


print(countFreq([10, 5, 10, 15, 10, 5]))
print(countFreq_optimal([10, 5, 10, 15, 10, 5]))