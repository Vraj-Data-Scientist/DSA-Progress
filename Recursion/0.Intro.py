# print name n times
def f1(i, n):
    if (i > n):
        return
    print("Vraj")
    f1(i+1, n)
print(f1(1,4))

# print 1, 2, 3, .... n
def f2(i, n):
    if (i > n):
        return
    print(i)
    f2(i+1, n)
print(f2(1,4))

# print n, n-1, n-2, ... 1
def f3(i, n):
    if (i < 1):
        return
    print(i)
    f3(i-1, n)
print(f3(4,4))

# print 1, 2, 3... n by backtracking
def f4(i, n):
    if (i < 1):
        return
    f4(i-1, n)
    print(i)
print(f4(4,4))

# print n, n-1, n-2, ... 1 by backtracking
def f5(i, n):
    if (i > n):
        return
    f5(i+1, n)
    print(i)
print(f5(1,4))

# sum of first n numbers(parametric way)
def f6_0(i, sum):
    if (i < 1):
        print(sum)
        return
    f6_0(i-1, sum+i)
print(f6_0(3, 0))

# sum of first n numbers(functional way)
def f6(n):
    if (n == 0):
        return 0
    return n + f6(n-1)
print(f6(3))

# factorial of n number
def f7(n):
    if (n == 0):
        return 1
    return n * f7(n-1)
print(f7(4))

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

# check palindrome or not
def f9(s, i):
    n = len(a)
    if (i >= n/2):
        return True
    if (s[i] != s[n-i-1]):
        return False
    return f9(s, i+1)
print(f9('MADAM', 0))
print(f9('MADSM', 0))

# print fibonnaci series
def f10(n):
    if (n <= 1):
        return n
    return f10(n-1) + f10(n-2)
print(f10(6))
print(f10(7))






