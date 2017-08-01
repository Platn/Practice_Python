a = [1,1,2,3,5,8,13,21,34,55,89] #Given array
b = [] # Empty array, can append element
for element in a: # How to do a for-loop
    if(element < 5):
        b.append(element)

print(b)
