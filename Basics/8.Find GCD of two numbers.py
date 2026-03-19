def find_gcd(n1, n2):
    gcd = 1
    for i in range(1, min(n1, n2)+1):
        if (n1 % i == 0 and n2 % i == 0):
            gcd = i
    return gcd

def find_gcd_better(n1, n2):
    gcd = 1
    for i in range(min(n1, n2), 0, -1):
        if (n1 % i == 0 and n2 % i == 0):
            gcd = i
            break
    return gcd

def find_gcd_optimal(n1, n2):
    while (n1 > 0 and n2 > 0):
        if (n1 > n2): n1 = n1 % n2
        else:         n2 = n2 % n1
    if (n1 == 0): return n2
    else:         return n1




print(find_gcd(9,12))
print(find_gcd(11,13))
print(find_gcd(20,0))
print(find_gcd_better(9,12))
print(find_gcd_better(11,13))
print(find_gcd_better(20,0))
print(find_gcd_optimal(9,12))
print(find_gcd_optimal(11,13))
print(find_gcd_better(20,0))