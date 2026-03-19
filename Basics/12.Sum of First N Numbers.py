# sum of first n numbers(functional way)
def f6(n):
    if (n == 0):
        return 0
    return n + f6(n-1)
print(f6(3))