"""
Concatenate two exercices_lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

Expected output:
['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
"""

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = [x + y for x in list1 for y in list2]
print(list3)