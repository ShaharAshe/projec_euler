""" Id = 2 """

MAX = 4000000
EVEN = 2

# First idea
even_sum = 0
fib_1, fib_2, fib_3 = (1, 1, 2)

while fib_1 < MAX:
    even_sum += fib_3
    fib_1 = fib_2 + fib_3
    fib_2 = fib_3 + fib_1
    fib_3 = fib_1 + fib_2
print(even_sum)


# Second idea
even_sum = 0
fib_1, fib_2 = (1, 1)

while fib_1 < MAX:
    fib_2 += fib_1
    fib_1 = fib_2 - fib_1
    if fib_2 % EVEN == 0:
        even_sum += fib_2

print(even_sum)