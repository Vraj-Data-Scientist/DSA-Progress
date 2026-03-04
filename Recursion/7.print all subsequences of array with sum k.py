def print_all_subsequence(a, i, ds):
    n = len(a)
    if (i >= n):
        print(ds)
        return
    ds.append(a[i])
    print_all_subsequence(a, i+1, ds)
    ds.remove(a[i])
    print_all_subsequence(a, i+1, ds)

print(print_all_subsequence([3,1,2], 0, []))

def print_subsequence_for_sum_k(a, i, ds, sum, s):
    n = len(a)
    if (i == n):
        if (s == sum):
            print(ds)
        return
    ds.append(a[i])
    s += a[i]
    print_subsequence_for_sum_k(a, i+1, ds, sum, s)
    ds.remove(a[i])
    s -= a[i]
    print_subsequence_for_sum_k(a, i+1, ds, sum, s)

def print_subsequence_for_sum_k_part2(a, i, ds, sum):
    n = len(a)
    if (i == n):
        if (sum == 0):
            print(ds)
        return
    ds.append(a[i])
    print_subsequence_for_sum_k_part2(a, i+1, ds, sum-a[i])
    ds.pop()
    print_subsequence_for_sum_k_part2(a, i+1, ds, sum)

print(print_subsequence_for_sum_k([1,1,3,2,1], 0, [], 2, 0))
print(print_subsequence_for_sum_k_part2([1,1,3,2,1], 0, [], 2))
print(print_subsequence_for_sum_k([4, -3, 1], 0, [], 2, 0))
print(print_subsequence_for_sum_k_part2([4, -3, 1], 0, [], 2))


