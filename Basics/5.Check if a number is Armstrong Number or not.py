import math

class ArmstrongChecker:
    def is_armstrong(self, num):
        k = int(math.log10(num) + 1)
        n = num
        sum = 0
        while (n > 0):
            last_digit = n % 10
            sum = sum + (last_digit**k)
            n //= 10
        return sum == num

print(ArmstrongChecker().is_armstrong(153))
print(ArmstrongChecker().is_armstrong(371))
print(ArmstrongChecker().is_armstrong(1634))
print(ArmstrongChecker().is_armstrong(35))