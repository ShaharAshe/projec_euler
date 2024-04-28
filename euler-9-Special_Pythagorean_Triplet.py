import numpy as np


def find_pythagoram_triplet(require_sum:int)->int:
    for a in range(1, require_sum):
        for b in range(a+1, require_sum):
                c = np.sqrt((a**2)+(b**2))
                c_r = int(np.sqrt((a**2)+(b**2)))
                if c == c_r and a < b < c_r and (a+b+c_r) == require_sum:
                    return (a*b*c_r)


if __name__ == "__main__":
    print(find_pythagoram_triplet(1000))
    