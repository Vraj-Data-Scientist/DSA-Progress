# print n, n-1, n-2, ... 1
def f3(i, n):
    if (i < 1):
        return
    print(i)
    f3(i-1, n)
print(f3(4,4))

# print n, n-1, n-2, ... 1 by backtracking
def f5(i, n):
    if (i > n):
        return
    f5(i+1, n)
    print(i)
print(f5(1,4))