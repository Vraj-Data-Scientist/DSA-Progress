def print_one_subsequence_for_sum_k(a, i, ds, sum, s):
    n = len(a)
    if (i == n):
        if (s == sum):
            print(ds)
            return True
        return False
    ds.append(a[i])
    s += a[i]
    if (print_one_subsequence_for_sum_k(a, i+1, ds, sum, s) == True):
        return True
    ds.remove(a[i])
    s -= a[i]
    if (print_one_subsequence_for_sum_k(a, i+1, ds, sum, s) == True):
        return True
    return False

print(print_one_subsequence_for_sum_k([1,1,3,2,1], 0, [], 15, 0))