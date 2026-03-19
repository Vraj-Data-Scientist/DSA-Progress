import math

def count_digits(n):
    cnt = 0
    while(n > 0):
        cnt += 1
        n = n // 10
    return cnt

def count_digits_optimal(n):
    cnt = int(math.log10(n) + 1)
    return cnt

print(count_digits(123456))
print(count_digits_optimal(12345678))