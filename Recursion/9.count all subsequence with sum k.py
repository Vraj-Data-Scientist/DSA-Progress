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


