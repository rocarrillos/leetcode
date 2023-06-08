def bin(num):
    return "{0:b}".format(num)

def equalize(bin_num, length):
    while len(bin_num) < length:
            bin_num = "0" + bin_num
    return list(map(lambda x: int(x), list(bin_num)))

def get_flips(a, b ,c):
    if (a or b) == c:
        return 0
    else:
        if a and b:
            return 2
        else:
            return 1
    # if 0 and 0 and 0, 0 flip
    # if 0 and 1 and 1, 0 flip
    # if 1 and 0 and 1, 0 flip
    # if 1 and 1 and 1, 0 flip

    # if 0 and 0 and 1, 1 flip
    # if 0 and 1 and 0, 1 flip
    # if 1 and 0 and 0, 1 flip
    # if 1 and 1 and 0, 2 flips!


class Solution:
    # 0 OR 1 is 1
    # 0 OR 0 is 0
    # 1 OR 1 is 1
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        bin_a, bin_b, bin_c = bin(a), bin(b), bin(c)
        length = max([len(bin_a), len(bin_b), len(bin_c)])
        bin_a = equalize(bin_a, length)
        bin_b = equalize(bin_b, length)
        bin_c = equalize(bin_c, length)
        for i in range(length):
            flips += get_flips(bin_a[i], bin_b[i], bin_c[i])
        return flips
