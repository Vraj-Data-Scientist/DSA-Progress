def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

def swap_python(a,b):
    a, b = b, a
    return a, b

def swap_xor(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

print(swap(5,-6))
print(swap_python(4, -4))
print(swap_xor(5, -10))
