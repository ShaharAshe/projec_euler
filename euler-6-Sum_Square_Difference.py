def squareSum(n:int)->int:
    return (n*(n+1)//2)**2


def sumSquare(n:int)->int:
    return n*(n+1)*(2*n+1)//6


def diffSumSquare(n:int)->int:
    return squareSum(n)-sumSquare(n)


if __name__ == '__main__':
    print(diffSumSquare(100))