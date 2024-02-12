# Removing empty list
list_of_lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]
filtered_list = [i for i in list_of_lists if i]
print("List after removing empty lists: ", filtered_list)


# Copying list
# Slice operator
original_list = [1,2,3,4,5]
cloned_list = original_list[:]
print(cloned_list)

# List constractor
cloned_list = list(original_list)
print(cloned_list)

# List comprehension
cloned_list = [item for item in original_list]
print(cloned_list)