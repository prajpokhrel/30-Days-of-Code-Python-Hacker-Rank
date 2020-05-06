#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_sum = []
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            e1 = arr[i][j]
            e2 = arr[i][j + 1]
            e3 = arr[i][j + 2]
            e4 = arr[i + 1][j + 1]
            e5 = arr[i + 2][j]
            e6 = arr[i + 2][j + 1]
            e7 = arr[i + 2][j + 2]
            sum_of_elements = e1 + e2 + e3 + e4 + e5 + e6 + e7
            max_sum.append(sum_of_elements)
    print(max(max_sum))
