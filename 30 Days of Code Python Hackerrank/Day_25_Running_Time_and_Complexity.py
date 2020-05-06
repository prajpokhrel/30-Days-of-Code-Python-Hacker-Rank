# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def isPrime(myNumber):
    if myNumber <= 1:
        return False
    sqrt_number = math.sqrt(myNumber)
    if sqrt_number.is_integer():
        return False
    for i in range(2, int(sqrt_number) + 1):
        if myNumber % i == 0:
            return False
    return True

testNumber = int(input())
for i in range(testNumber):
    myNumber = int(input())
    if isPrime(myNumber):
        print("Prime")
    else:
        print("Not prime")
