#Python Program for Find Remainder of Array Multiplication Divided by N

arr = [100, 10, 5, 25, 35, 14]
n = 11
prd = 1
for num in arr:
    prd *= num

print(prd % n)

'''
Sample output

9
'''
