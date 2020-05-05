class Person:
    age = 0
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge > 0:
            initialAge = age 
        else:
            print("Age is not valid, setting age to 0.")
            self.age = 0  

    def amIOld(self):
        global age
        # Do some computations in here and print out the correct statement to the console
        if age < 13:
            print("You are young.")
        elif age >= 13 and age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
    
    def yearPasses(self):
        global age
        # Increment the age of the person in here
        age = age + 1
        return age


t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")