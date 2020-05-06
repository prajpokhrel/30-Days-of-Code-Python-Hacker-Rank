#!/bin/python3

import math
import os
import random
import re
import sys

def max_bit(n, k):
    max_bits = 0
    for i in range(1, n + 1):
        for j in range(1, i):
            bit_wise = i & j
            if max_bits < bit_wise < k:
                max_bits = bit_wise
                if max_bits == k - 1:
                    return max_bits 
    return max_bits


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        print(max_bit(n, k))
