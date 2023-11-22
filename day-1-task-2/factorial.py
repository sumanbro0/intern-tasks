import math


def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)


print(fact(5))

# Inbuilt feature

print(math.factorial(5))