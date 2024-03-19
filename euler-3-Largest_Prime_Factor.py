""" Id = 3 """

from math import sqrt

# First idea
def big_prime_1(num:int) -> int:
    big_prime = 2
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0 and is_prime(i) and big_prime < i:
            big_prime = i
    
    return big_prime

def is_prime(n:int)->bool:
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    
    return True

# Second idea
def big_prime_2(num:int) -> int:
    factor=2
    lastFactor=1

    while num>1:
        if num%factor == 0:
            lastFactor = factor
            num = num/factor
            while num%factor == 0:
                num = num/factor
        factor = factor+1

    return lastFactor


if __name__ == '__main__':
    num = 600851475143
    print(big_prime_1(num))
    print(big_prime_2(num))
    