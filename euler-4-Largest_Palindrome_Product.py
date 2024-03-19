""" Id = 4 """


# First idea
def big_palindrome_1() -> int:
    large_pol = 0
    for num_1 in range(999, 99, -1):
        for num_2 in range(999, 99, -1):
            num = num_1*num_2
            if is_palindrome(num):
                if large_pol < num:
                    large_pol = num
                    
    return large_pol
    

def is_palindrome(n:int)->bool:
    number_str = str(n)
    if number_str == number_str[::-1]:
        return True
    return False

# Second idea
def big_palindrome_2() -> int:
    largestPalindrome = 0
    for a in range(999, 99, -1):
        if a % 11 == 0:
            b = 999
            db = 1
        else:
            b = 990
            db = 11
        while b >= a:
            if is_palindrome(a*b) and largestPalindrome < a*b:
                largestPalindrome = a*b
            b = b-db
        a = a-1

    return largestPalindrome


if __name__ == '__main__':
    print(big_palindrome_1())
    print(big_palindrome_2())
    