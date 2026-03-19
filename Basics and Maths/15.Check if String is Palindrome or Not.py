# check palindrome or not
def f9(s, i):
    n = len(s)
    if (i >= n/2):
        return True
    if (s[i] != s[n-i-1]):
        return False
    return f9(s, i+1)
print(f9('MADAM', 0))
print(f9('MADSM', 0))