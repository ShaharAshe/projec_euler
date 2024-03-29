import numpy as np

def is_prime(primes, i)->bool:
    for p in primes:
        if p > np.sqrt(i):
            return True
        if i%p == 0:
            return False
    return True
                

def nPrime(num:int)->int:
    primes = []
    i = 2
    while(True):
        if len(primes) == num:
            return i
        if i == 2:
            primes = [2]
        elif is_prime(primes, i):
             primes += [i]
        i += 1


if __name__ == "__main__":
    print(nPrime(10001))