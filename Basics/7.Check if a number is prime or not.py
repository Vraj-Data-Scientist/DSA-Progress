import math
def checkPrime(n):
    cnt = 0
    for i in range(1, n+1):
        if (n % i == 0):
            cnt += 1
    return cnt == 2

def checkPrime_optimal(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n))+1):
        if (n % i == 0):
            cnt += 1
            if (n/i != i):
                cnt += 1
    return cnt == 2

print(checkPrime(2))
print(checkPrime(11))
print(checkPrime(24))
print(checkPrime(1))
print(checkPrime_optimal(2))
print(checkPrime_optimal(11))
print(checkPrime_optimal(24))
print(checkPrime_optimal(1))