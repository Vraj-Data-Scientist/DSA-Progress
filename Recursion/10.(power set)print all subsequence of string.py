def print_subsequence_of_string(s, i, ds, result):
    n = len(s)
    if (i == n):
        result.append(''.join(ds))
        return
    ds.append(s[i])
    print_subsequence_of_string(s, i+1, ds, result)
    ds.pop()
    print_subsequence_of_string(s, i+1, ds, result)

result = []
print(print_subsequence_of_string('abc', 0, [], result))
print(result)