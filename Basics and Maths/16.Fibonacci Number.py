# print fibonnaci series
def f10(n):
    if (n <= 1):
        return n
    return f10(n-1) + f10(n-2)
print(f10(6))
print(f10(7))