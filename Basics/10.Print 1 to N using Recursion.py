# print 1, 2, 3, .... n
def f2(i, n):
    if (i > n):
        return
    print(i)
    f2(i+1, n)
print(f2(1,4))

# print 1, 2, 3... n by backtracking
def f4(i, n):
    if (i < 1):
        return
    f4(i-1, n)
    print(i)
print(f4(4,4))