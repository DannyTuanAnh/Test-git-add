import math
def ham1(n):
    if n < 2:
        return 0
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return 0
    return 1
def ham4(n):
    tong= 0
    while n != 0 :
        i = n % 10
        if ham1(i):
            tong += i
        n //= 10
    return tong
def ham5(n):
    rev = 0
    while n != 0:
       rev = rev * 10 + n % 10
       n //= 10
    return rev  
def ham6(n):
    count = 0
    for i in  range(2,math.isqrt(n)):
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
    if n > 1:
        count += 1
    return count
def ham7(n):
    count = 0
    res = 0 
    for i in  range(2,math.isqrt(n)):
        if n % i == 0:
            count = i
            while n % i == 0 :
                n //= i
    if n > 1:
        res = n 
    return res       
def ham8(n):
    while n != 0:
        if n % 10 == 6:
            return 1
        n //= 10
    return 0
def ham9(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    if sum % 8 == 0:
        return 1
    else:
        return 0
def ham10(n):
    sum_factorial = 0
    while n != 0:
        sum_factorial += math.factorial(n % 10)
        n //= 10
    return sum_factorial
def ham11(n):
    donvi = n % 10
    while n != 0:
        if donvi != n % 10:
            return 0
        n//= 10
    return 1
def ham12(n):
    donViMax = n % 10
    while n != 0:
        if donViMax < (n % 10):
            return 0 
        n //= 10
    return 1
def ham13(n):
    m = n
    count = 0
    sum_pow = 0
    while n != 0:
        count += 1
        n //= 10
    while m != 0:
        sum_pow += math.pow(m % 10,count)
        m //= 10
    return int(sum_pow)
if __name__ == "__main__":
    n = int(input())
    print(ham1(n))
    print(ham4(n))
    print(ham5(n))
    print(ham6(n))
    print(ham7(n))
    print(ham8(n))
    print(ham9(n))
    print(ham10(n))
    print(ham11(n))
    print(ham12(n))
    print(ham13(n))