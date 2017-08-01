inputNumber = int(input("What number would you like to divide by? "))

x = range(1, inputNumber + 1) # How to set a range of values, + 1 is to include input

print("Divisors of %d" % inputNumber)
for element in x:
    if(inputNumber % element == 0):
        print(element)

'''
a = [int(x) for x in input().split()] # Multiple number input into list

for element in a:
    print(element)

Note: This is not required of the prompt but done for extracurricular purposes.
'''
