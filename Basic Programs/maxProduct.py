#Maximum Product of Continuous Sequence

arr=[]
m=[]
count=1
n=int(input())
for i in range(n):
    a=int(input())
    arr.append(a)  
for i in range(len(arr)):
    if arr[i]>0:
        count*=arr[i]
    else:
        count=1
m.append(count) 
if count==1:
    print(0)
else:
    print(max(m))