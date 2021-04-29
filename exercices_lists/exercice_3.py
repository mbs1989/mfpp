"""
Given a Python list. Turn every item of a list into its square
aList = [1, 2, 3, 4, 5, 6, 7]

Expected output:
[1, 4, 9, 16, 25, 36, 49]
"""

list = [1, 2, 3, 4, 5, 6, 7]
list =  [x * x for x in list]
print(list)