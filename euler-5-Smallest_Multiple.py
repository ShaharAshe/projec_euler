import numpy as np


def is_prime(num: int)->bool:
    if num == 0 or num == 1:
        return False
    for n in range(2, int(np.sqrt(num))+1):
        if num % n == 0:
            return False
    return True

def smallestMultiple(maxRange: int)->int:
    if maxRange < 1:
        return 0
    
    smallest_M = 1
    for i in range(1, maxRange+1):
        if is_prime(i):
            power = 1
            while(np.power(i, power) <= maxRange):
                smallest_M *= i
                power += 1
    return smallest_M


if __name__ == '__main__':
    print(smallestMultiple(20))
        