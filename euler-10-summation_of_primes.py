from math import sqrt


def sieve(n:int) -> list:
    lst:list = [False]*n
    for i in range(2, int(sqrt(n)+1)):
        for j in range(i+i,n,i):
            lst[j] = True
    return lst


def summation_of_primes(n:int) -> int:
    sum:int = 0

    lst:list = sieve(n)

    for i in range(2, n):
        if not lst[i]:
            sum += i
    return sum


if __name__ == '__main__':
    sum:int = summation_of_primes(2000000)
    print(sum)
