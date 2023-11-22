import math


def gcd(dividend,divisor):
    if divisor==0:
        return dividend
    elif dividend==0:
        return divisor
    else:
        quotient=int(dividend/divisor)
        rem=dividend-(quotient*divisor)

        return gcd(divisor,rem)
        
print(gcd(270,192))

# Inbuild feature

print(math.gcd(270,192))