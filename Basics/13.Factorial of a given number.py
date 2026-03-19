# factorial of n number
def f7(n):
    if (n == 0):
        return 1
    return n * f7(n-1)
print(f7(4))