#  This program calculates lists of a certain length

List = [[6, 5, 3], [1, 2, [4, [2, 3], [2, 2], 2], 3], [4], [1, 2], [2, 4], [5, 5, 5], [7]]  # Some list
count = 0  # The number of matches

print("Input length of list: ")
length = int(input())  # Length of list

# This function passes through the list items, if the list item is a list item, then call recursion.
# If not, then read length of current sublist and increase count by 1 if matches user length.
def find(obj):
    global count, length
    for i in range(len(obj)):
        if isinstance(obj[i], list):
            if len(obj[i]) == length:
                count += 1
            find(obj[i])


find(List)
print("Count of matches: ", count)
