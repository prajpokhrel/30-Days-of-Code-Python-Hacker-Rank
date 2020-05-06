#!/bin/python3

import math
import os
import random
import re
import sys

def dec_to_binary(n):
    
    currentConsecutive = 0
    maxConsecutive = 0
    while n > 0:
        remain = n % 2
        if remain == 1:
            currentConsecutive += 1
            if currentConsecutive > maxConsecutive:
                maxConsecutive = currentConsecutive
        else:
            currentConsecutive = 0
        n = n // 2
    return maxConsecutive


if __name__ == '__main__':
    n = int(input())
    print(dec_to_binary(n))

    
        
