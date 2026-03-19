# reverse an array (two variable)
def f8(a, l, r):
    if (l >= r):
        return
    a[l], a[r] = a[r], a[l]
    f8(a, l+1, r-1)
a = [1,2,3,5,6]
f8(a,0,4)
print(a)

# reverse an array (one var)
def f8_1(a, i):
    n = len(a)
    if (i >= n/2):
        return
    a[i], a[n-i-1] = a[n-i-1], a[i]
    f8_1(a, i+1)
a = [1,2,3,5,8]
f8_1(a, 0)
print(a)