# Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even_numbers(n):
    list = []

    for i in n:
        if (i%2) == 0:
            list.append(i)
    return list


print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))




