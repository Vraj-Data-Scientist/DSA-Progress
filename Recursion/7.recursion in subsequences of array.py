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

print(print_subsequence_for_sum_k([1,1,3,2,1], 0, [], 2, 0))

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

print(print_one_subsequence_for_sum_k([1,1,3,2,1], 0, [], 2, 0))

def cnt_subsequence_for_sum_k(a, i, sum, s):
    n = len(a)
    if (s > sum): return 0
    if (i == n):
        if (s == sum):
            return 1
        return 0
    s += a[i]
    l = cnt_subsequence_for_sum_k(a, i+1, sum, s)
    s -= a[i]
    r = cnt_subsequence_for_sum_k(a, i+1, sum, s)
    return l+r

print(cnt_subsequence_for_sum_k([1,1,3,2,1], 0, 2, 0))


