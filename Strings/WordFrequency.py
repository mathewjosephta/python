# Python - Words Frequency in String Shorthands

from collections import Counter
s = "Hello World Hello Everyone"
res=Counter(s.split())
print(res)

'''
Counter({'hello': 2, 'world': 1, 'everyone': 1})
'''
