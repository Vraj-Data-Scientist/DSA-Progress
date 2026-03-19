# print name n times
def f1(i, n):
    if (i > n):
        return
    print("Vraj")
    f1(i+1, n)
print(f1(1,4))