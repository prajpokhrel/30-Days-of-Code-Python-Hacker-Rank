#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    acc_regex = re.compile("^[a-z\.]+@gmail.com$")
    firstNames = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if acc_regex.search(emailID):
            firstNames.append(firstName)
    firstNames.sort()
    for name in firstNames:
        print(name)
