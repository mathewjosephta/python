#Python Program to Swap Two Elements in a List

a = [10, 20, 30, 40, 50]

temp = a[2]
a[2] = a[4]
a[4] = temp
print(a)

'''
Sample Output

[10, 20, 50, 40, 30]
'''
