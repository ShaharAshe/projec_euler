""" Id = 1 """

# First idea
MAX = 999

def divFunc(div_n):
    p = MAX // div_n
    return div_n * (p * (p+1))//2


print(divFunc(3) + divFunc(5) - divFunc(3*5))

# Second idea
lst = list(range(1, 1000))
sum_final_lst = sum([x for x in lst if x % 3 == 0 or x % 5 == 0])
print(sum_final_lst)


