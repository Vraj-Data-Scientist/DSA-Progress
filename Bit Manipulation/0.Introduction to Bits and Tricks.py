def convert_int_to_binary(n):
    res = ''
    while (n != 0):
        if (n % 2 == 1):
            res = res + '1'
        else:
            res = res + '0'
        n = n // 2
    res = res[::-1]
    return res

def convert_binary_to_int(s):
    res = 0
    n = len(s)
    p_square = 1
    for i in range(n-1, -1, -1):
        if (s[i] == '1'):
            res = res + p_square
        p_square = p_square * 2
    return res

print(convert_int_to_binary(13))
print(convert_int_to_binary(14))
print(convert_int_to_binary(15))
print(convert_int_to_binary(16))
print(convert_binary_to_int('1101'))
print(convert_binary_to_int('1110'))
print(convert_binary_to_int('1111'))
print(convert_binary_to_int('10000'))

# Bitwise operators
print(13 & 7)    # AND
print(13 | 7)    # OR
print(13 ^ 7)    # XOR
print(~5)        # NOT
print(13 << 1)   # SHIFT(left)
print(13 >> 1)   # SHIFT(right)





