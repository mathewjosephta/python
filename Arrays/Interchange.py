# Python program to interchange first and last elements in a list

arr = [1,2,3,4,5]
temp=arr[0]
arr[0]=arr[-1]
arr[-1]=temp
print(arr)

'''
Sample Output

[5,2,3,4,1]
'''
