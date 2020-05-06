# Enter your code here. Read input from STDIN. Print output to STDOUT
numberOfTestCases = int(input())



for i in range(numberOfTestCases):
    myString = input()
    evenString = ""
    oddString = ""
    for index in range(len(myString)):
        if index % 2 == 0:
            evenString += "".join(myString[index])
        else:
            oddString += "".join(myString[index])
    print(evenString + " " + oddString) 
    

